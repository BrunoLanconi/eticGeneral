"use strict";

// 01-srp.js
// Foco: SRP (Single Responsibility Principle)
// Separar responsabilidades: modelos (shapes) vs geração/ordenação vs I/O vs apresentação.

const fs = require("node:fs"); // ainda DIP violado (vamos corrigir mais tarde)

const PI = 3.14;

class Circle {
  constructor(radius = 1) {
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
  constructor(width = 1, height = 1) {
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

class Square extends Rectangle {
  constructor(side = 1) {
    super(side, side);
    this.side = side;
  }
  area() {
    return this.side ** 2;
  }
  perimeter() {
    return 4 * this.side;
  }
}

class ShapeGenerator {
  createRandomShapes(n) {
    const shapes = [];
    const constructors = [Circle, Rectangle, Square];

    for (let i = 0; i < n; i += 1) {
      const Ctor = constructors[Math.floor(Math.random() * constructors.length)];
      if (Ctor === Rectangle) {
        shapes.push(new Rectangle(randInt(1, 10), randInt(1, 10)));
      } else {
        shapes.push(new Ctor(randInt(1, 10)));
      }
    }

    return shapes;
  }
}

class ShapeSorter {
  sortByAreaDesc(shapes) {
    return [...shapes].sort((a, b) => b.area() - a.area());
  }
}

class ShapeRepositoryFile {
  save(path, shapes) {
    const payload = { generatedAt: new Date().toISOString(), shapes };
    fs.writeFileSync(path, JSON.stringify(payload, null, 2), "utf8");
  }
}

class ShapePrinter {
  printAreaReport(shapes) {
    console.log("Shapes sorted by area:");
    for (const shape of shapes) {
      console.log(`${shape.constructor.name}: area=${shape.area()}`);
    }
  }
}

function randInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function main() {
  const generator = new ShapeGenerator();
  const sorter = new ShapeSorter();
  const printer = new ShapePrinter();
  const repo = new ShapeRepositoryFile();

  const shapes = generator.createRandomShapes(5);
  const sorted = sorter.sortByAreaDesc(shapes);

  printer.printAreaReport(sorted);
  repo.save("/tmp/shapes.srp.json", sorted);
}

if (require.main === module) {
  main();
}

module.exports = {
  Circle,
  Rectangle,
  Square,
  ShapeGenerator,
  ShapeSorter,
  ShapeRepositoryFile,
  ShapePrinter,
  main,
};
