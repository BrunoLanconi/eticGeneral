"use strict";

// 05-dip.js
// Foco: DIP (Dependency Inversion Principle)
// - Alto nível (use cases) dependem de abstrações (contracts), não de fs/console diretamente.
// - Injetamos dependências: logger, repository, rng.

const PI = 3.14;

class Circle {
  constructor(radius) {
    this.radius = radius;
  }
  area() {
    return PI * this.radius ** 2;
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
}

class Square {
  constructor(side) {
    this.side = side;
  }
  area() {
    return this.side ** 2;
  }
}

// Abstrações (por convenção):
// - rng.int(min,max)
// - logger.info(msg)
// - repo.save(shapes)

class ShapeUseCases {
  constructor({ rng, logger, repo }) {
    this.rng = rng;
    this.logger = logger;
    this.repo = repo;
  }

  createRandomShapes(n) {
    const shapes = [];
    const constructors = [Circle, Rectangle, Square];

    for (let i = 0; i < n; i += 1) {
      const Ctor = constructors[this.rng.int(0, constructors.length - 1)];
      if (Ctor === Rectangle) {
        shapes.push(new Rectangle(this.rng.int(1, 10), this.rng.int(1, 10)));
      } else {
        shapes.push(new Ctor(this.rng.int(1, 10)));
      }
    }

    return shapes;
  }

  sortByAreaDesc(shapes) {
    return [...shapes].sort((a, b) => b.area() - a.area());
  }

  runDemo() {
    const shapes = this.createRandomShapes(5);
    const sorted = this.sortByAreaDesc(shapes);

    this.logger.info("Shapes sorted by area:");
    for (const shape of sorted) {
      this.logger.info(`${shape.constructor.name}: area=${shape.area()}`);
    }

    this.repo.save(sorted);
  }
}

// Implementações concretas (baixo nível)
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
  const useCases = new ShapeUseCases({
    rng: new MathRng(),
    logger: new ConsoleLogger(),
    repo: new InMemoryRepo(),
  });

  useCases.runDemo();
}

if (require.main === module) {
  main();
}

module.exports = {
  Circle,
  Rectangle,
  Square,
  ShapeUseCases,
  MathRng,
  ConsoleLogger,
  InMemoryRepo,
  main,
};
