"use strict";

// 02-ocp.js
// Foco: OCP (Open/Closed Principle)
// Em vez de usar if/switch em tipo, usar polimorfismo + registro/factory extensível.

const PI = 3.14;

class Shape {
  area() {
    throw new Error("area() must be implemented");
  }
}

class Circle extends Shape {
  constructor(radius = 1) {
    super();
    this.radius = radius;
  }
  area() {
    return PI * this.radius ** 2;
  }
  circumference() {
    return PI * 2 * this.radius;
  }
}

class Rectangle extends Shape {
  constructor(width = 1, height = 1) {
    super();
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

class Square extends Shape {
  constructor(side = 1) {
    super();
    this.side = side;
  }
  area() {
    return this.side ** 2;
  }
  perimeter() {
    return 4 * this.side;
  }
}

class ShapeFactory {
  constructor() {
    this.registry = new Map();
  }

  register(type, creatorFn) {
    this.registry.set(type, creatorFn);
  }

  create(type, ...args) {
    const creator = this.registry.get(type);
    if (!creator) throw new Error(`Unknown shape type: ${type}`);
    return creator(...args);
  }
}

class ShapeSorter {
  sortByAreaDesc(shapes) {
    return [...shapes].sort((a, b) => b.area() - a.area());
  }
}

function randInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function main() {
  const factory = new ShapeFactory();

  // OCP: para adicionar um novo shape, registramos sem modificar sorter/relatórios.
  factory.register("circle", (r) => new Circle(r));
  factory.register("rectangle", (w, h) => new Rectangle(w, h));
  factory.register("square", (s) => new Square(s));

  const shapes = [
    factory.create("circle", randInt(1, 10)),
    factory.create("rectangle", randInt(1, 10), randInt(1, 10)),
    factory.create("square", randInt(1, 10)),
  ];

  const sorter = new ShapeSorter();
  const sorted = sorter.sortByAreaDesc(shapes);

  console.log("Shapes sorted by area:");
  for (const shape of sorted) {
    console.log(`${shape.constructor.name}: area=${shape.area()}`);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  Shape,
  Circle,
  Rectangle,
  Square,
  ShapeFactory,
  ShapeSorter,
  main,
};
