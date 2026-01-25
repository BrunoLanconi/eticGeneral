"use strict";

// 06-solid.js
// Resultado: exemplo “compliance com SOLID” para o cenário de formas.
// - SRP: modelos / casos de uso / infra separados
// - OCP: adicionar shape via registro (sem alterar sorter/use case)
// - LSP: shapes obedecem ao contrato HasArea; não forçamos heranças quebráveis
// - ISP: consumers dependem apenas de capabilities necessárias
// - DIP: use case depende de abstrações (rng/logger/repo)

const PI = 3.14;

// ---- Capabilities (ISP) ----
// HasArea: area()
// HasPerimeter: perimeter()
// HasCircumference: circumference()

// ---- Modelos (SRP) ----
class Circle {
  constructor(radius) {
    this.radius = radius;
  }
  area() {
    return PI * this.radius ** 2;
  }
  circumference() {
    return PI * 2 * this.radius;
  }
}

class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
  area() {
    return this.width * this.height;
  }
  perimeter() {
    return 2 * (this.width + this.height);
  }
}

class Square {
  constructor(side) {
    this.side = side;
  }
  area() {
    return this.side ** 2;
  }
  perimeter() {
    return 4 * this.side;
  }
}

function has(fnName, obj) {
  return obj && typeof obj[fnName] === "function";
}

// ---- OCP: registro extensível ----
class ShapeRegistry {
  constructor() {
    this.creators = new Map();
  }

  register(type, createFn) {
    this.creators.set(type, createFn);
  }

  create(type, ...args) {
    const createFn = this.creators.get(type);
    if (!createFn) throw new Error(`Unknown shape type: ${type}`);
    return createFn(...args);
  }

  listTypes() {
    return [...this.creators.keys()];
  }
}

// ---- Casos de uso (SRP + DIP) ----
class ShapesReportUseCase {
  constructor({ registry, rng, logger, repo }) {
    this.registry = registry;
    this.rng = rng;
    this.logger = logger;
    this.repo = repo;
  }

  createRandomShapes(n) {
    const types = this.registry.listTypes();
    const shapes = [];

    for (let i = 0; i < n; i += 1) {
      const type = types[this.rng.int(0, types.length - 1)];

      if (type === "rectangle") {
        shapes.push(this.registry.create("rectangle", this.rng.int(1, 10), this.rng.int(1, 10)));
        continue;
      }

      shapes.push(this.registry.create(type, this.rng.int(1, 10)));
    }

    return shapes;
  }

  sortByAreaDesc(shapes) {
    // Consumer depende apenas de HasArea (ISP)
    for (const s of shapes) {
      if (!has("area", s)) throw new Error("Expected HasArea shapes");
    }
    return [...shapes].sort((a, b) => b.area() - a.area());
  }

  run() {
    const shapes = this.createRandomShapes(5);
    const sorted = this.sortByAreaDesc(shapes);

    this.logger.info("Shapes sorted by area:");
    for (const shape of sorted) {
      const extra = has("perimeter", shape)
        ? ` perimeter=${shape.perimeter()}`
        : has("circumference", shape)
          ? ` circumference=${shape.circumference()}`
          : "";

      this.logger.info(`${shape.constructor.name}: area=${shape.area()}${extra}`);
    }

    this.repo.save(sorted);
  }
}

// ---- Infra (DIP) ----
class MathRng {
  int(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
}

class ConsoleLogger {
  info(message) {
    console.log(message);
  }
}

class InMemoryRepo {
  constructor() {
    this.saved = [];
  }
  save(shapes) {
    this.saved.push({ generatedAt: new Date().toISOString(), shapes });
  }
}

function main() {
  const registry = new ShapeRegistry();

  registry.register("circle", (r) => new Circle(r));
  registry.register("rectangle", (w, h) => new Rectangle(w, h));
  registry.register("square", (s) => new Square(s));

  const useCase = new ShapesReportUseCase({
    registry,
    rng: new MathRng(),
    logger: new ConsoleLogger(),
    repo: new InMemoryRepo(),
  });

  useCase.run();
}

if (require.main === module) {
  main();
}

module.exports = {
  Circle,
  Rectangle,
  Square,
  ShapeRegistry,
  ShapesReportUseCase,
  MathRng,
  ConsoleLogger,
  InMemoryRepo,
  main,
};
