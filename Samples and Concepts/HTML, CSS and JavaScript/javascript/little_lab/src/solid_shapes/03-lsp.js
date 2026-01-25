"use strict";

// 03-lsp.js
// Foco: LSP (Liskov Substitution Principle)
// Evitar herança que quebra contrato (Square extends Rectangle com setters, por exemplo).
// Aqui: Square e Rectangle são Shapes independentes.

const PI = 3.14;

class Shape {
  area() {
    throw new Error("area() must be implemented");
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
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
  constructor(side) {
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

class Circle extends Shape {
  constructor(radius) {
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

function testShapeArea(shape) {
  // Se é Shape, deve funcionar independente do tipo
  return shape.area();
}

function testRectangleBehavior(rectangle) {
  // Exemplo de “contrato” específico de Rectangle
  // (não chamaremos isso em Square — não precisamos forçar substituição indevida)
  return rectangle.perimeter();
}

function main() {
  const shapes = [new Rectangle(5, 4), new Square(5), new Circle(3)];

  console.log("Areas:");
  for (const shape of shapes) {
    console.log(`${shape.constructor.name}: ${testShapeArea(shape)}`);
  }

  const rect = new Rectangle(5, 4);
  console.log("Rectangle perimeter:", testRectangleBehavior(rect));
}

if (require.main === module) {
  main();
}

module.exports = { Shape, Rectangle, Square, Circle, main };
