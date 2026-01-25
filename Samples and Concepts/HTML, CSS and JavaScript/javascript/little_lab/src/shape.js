"use strict"; // This line enables strict mode in JavaScript. That means the code will be executed in a "strict" operating context which helps catch common coding mistakes and "unsafe" actions.

/**
 * This module contains classes that represent different shapes.
 *
 * Ported from: Self-Guided Learning/python/day_04/examples/shape.py
 */

const PI = 3.14;

class Shape {
  /**
   * Calculates the area of the shape.
   *
   * In the Python example, the base implementation prints a message.
   */
  area() {
    console.log(
      "Every shape has an area. But each shape has a different formula to calculate it."
    );
    return NaN;
  }

  toString() {
    return `${this.constructor.name}: ${this.area()} area`;
  }
}

class Circle extends Shape {
  /**
   * @param {number} [radius=1]
   */
  constructor(radius = 1) {
    super();
    this.radius = radius;
  }

  /**
   * @returns {number}
   */
  circumference() {
    return PI * 2 * this.radius;
  }

  /**
   * @returns {number}
   */
  area() {
    return PI * this.radius ** 2;
  }
}

class Rectangle extends Shape {
  /**
   * @param {number} [width=1]
   * @param {number} [height=1]
   */
  constructor(width = 1, height = 1) {
    super();
    this.width = width;
    this.height = height;
  }

  /**
   * @returns {number}
   */
  perimeter() {
    return 2 * (this.width + this.height);
  }

  /**
   * @returns {number}
   */
  area() {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  /**
   * @param {number} [side=1]
   */
  constructor(side = 1) {
    super(side, side);
  }

  /**
   * @returns {number}
   */
  perimeter() {
    return 4 * this.width;
  }

  /**
   * @returns {number}
   */
  area() {
    return this.width ** 2;
  }
}

/**
 * @param {number} min
 * @param {number} max
 * @returns {number} integer in [min, max]
 */
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Creates a list of randomly generated shapes.
 *
 * @param {number} n
 * @returns {Array<Shape>}
 */
function createRandomShapes(n) {
  const shapes = [];
  const constructors = [Circle, Rectangle, Square];

  for (let i = 0; i < n; i += 1) {
    const Ctor = constructors[randomInt(0, constructors.length - 1)];

    if (Ctor === Rectangle) {
      shapes.push(new Rectangle(randomInt(1, 10), randomInt(1, 10)));
    } else if (Ctor === Square) {
      shapes.push(new Square(randomInt(1, 10)));
    } else {
      shapes.push(new Circle(randomInt(1, 10)));
    }
  }

  return shapes;
}

function main() {
  const circle = new Circle();
  console.log(circle.area());
  console.log(circle.circumference());

  const rectangle = new Rectangle();
  console.log(rectangle.area());
  console.log(rectangle.perimeter());

  const shapes = createRandomShapes(5);
  shapes.sort((a, b) => b.area() - a.area());

  console.log("Shapes sorted by area:");
  for (const shape of shapes) {
    console.log(String(shape));
  }
}

module.exports = {
  Shape,
  Circle,
  Rectangle,
  Square,
  createRandomShapes,
  main,
};

if (require.main === module) {
  main();
}
