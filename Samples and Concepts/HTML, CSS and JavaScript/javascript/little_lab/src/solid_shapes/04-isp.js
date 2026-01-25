"use strict";

// 04-isp.js
// Foco: ISP (Interface Segregation Principle)
// Em JS, fazemos isso com pequenas “interfaces” por convenção/capabilities:
// - HasArea: area()
// - HasPerimeter: perimeter()
// - HasCircumference: circumference()

const PI = 3.14;

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

function supports(fnName, obj) {
  return obj && typeof obj[fnName] === "function";
}

// Cliente que só precisa de area() (depende apenas de HasArea)
function sumAreas(shapes) {
  return shapes.reduce((acc, shape) => {
    if (!supports("area", shape)) {
      throw new Error("Expected shape with area() (HasArea)");
    }
    return acc + shape.area();
  }, 0);
}

// Cliente que precisa de perimeter() (depende só de HasPerimeter)
function listPerimeters(shapes) {
  return shapes
    .filter((s) => supports("perimeter", s))
    .map((s) => ({ name: s.constructor.name, perimeter: s.perimeter() }));
}

// Cliente que precisa de circumference() (depende só de HasCircumference)
function listCircumferences(shapes) {
  return shapes
    .filter((s) => supports("circumference", s))
    .map((s) => ({ name: s.constructor.name, circumference: s.circumference() }));
}

function main() {
  const shapes = [new Circle(3), new Rectangle(2, 5), new Square(4)];

  console.log("Sum areas:", sumAreas(shapes));
  console.log("Perimeters:", listPerimeters(shapes));
  console.log("Circumferences:", listCircumferences(shapes));
}

if (require.main === module) {
  main();
}

module.exports = {
  Circle,
  Rectangle,
  Square,
  sumAreas,
  listPerimeters,
  listCircumferences,
  main,
};
