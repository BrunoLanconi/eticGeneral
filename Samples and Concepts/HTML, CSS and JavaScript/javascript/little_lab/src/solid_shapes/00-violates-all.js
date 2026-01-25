"use strict";

// 00-violates-all.js
// Objetivo: um exemplo propositalmente ruim que viola SRP, OCP, LSP, ISP e DIP
// no contexto de formas geométricas.

const fs = require("node:fs"); // DIP violado: dependência concreta hard-coded

class ShapeManager {
  // SRP violado: este "manager" faz de tudo
  constructor() {
    this.pi = 3.14;
    this.shapes = [];
  }

  // OCP violado: para adicionar novo shape, precisa mexer aqui
  createShape(type, a, b) {
    if (type === "circle") {
      return { type, radius: a };
    }
    if (type === "rectangle") {
      return { type, width: a, height: b };
    }
    if (type === "square") {
      return { type, side: a, width: a, height: a };
    }

    throw new Error(`Unknown shape type: ${type}`);
  }

  // ISP violado: força consumidores a dependerem de um conjunto de operações (área, perímetro,
  // circunferência, serialize, draw...) mesmo quando não faz sentido para todos.
  // Aqui a “interface” é implícita e inchada.
  area(shape) {
    switch (shape.type) {
      case "circle":
        return this.pi * shape.radius ** 2;
      case "rectangle":
        return shape.width * shape.height;
      case "square":
        return shape.side ** 2;
      default:
        throw new Error("Unknown shape");
    }
  }

  perimeter(shape) {
    switch (shape.type) {
      case "circle":
        // “perimeter” de círculo aqui vira circunferência (mistura de conceitos)
        return this.pi * 2 * shape.radius;
      case "rectangle":
        return 2 * (shape.width + shape.height);
      case "square":
        return 4 * shape.side;
      default:
        throw new Error("Unknown shape");
    }
  }

  // LSP violado: “Square é um Rectangle” com setters quebra expectativas.
  // Aqui simulamos o problema: quem usa Rectangle espera poder setar width e height independentemente.
  setRectangleWidth(rect, width) {
    rect.width = width;
    if (rect.type === "square") {
      // Square quebra o “contrato” do retângulo e altera height junto
      rect.height = width;
      rect.side = width;
    }
  }

  setRectangleHeight(rect, height) {
    rect.height = height;
    if (rect.type === "square") {
      // Square quebra o “contrato” do retângulo e altera width junto
      rect.width = height;
      rect.side = height;
    }
  }

  add(shape) {
    this.shapes.push(shape);
  }

  // SRP/DIP/OCP/ISP: tudo misturado
  saveToDisk(path) {
    const payload = {
      generatedAt: new Date().toISOString(),
      shapes: this.shapes,
    };

    fs.writeFileSync(path, JSON.stringify(payload, null, 2), "utf8");
  }

  loadFromDisk(path) {
    const raw = fs.readFileSync(path, "utf8");
    const parsed = JSON.parse(raw);
    this.shapes = parsed.shapes;
  }

  printReport() {
    // SRP violado: formata/printa e também calcula
    const sorted = [...this.shapes].sort((a, b) => this.area(b) - this.area(a));

    console.log("Shapes sorted by area:");
    for (const shape of sorted) {
      console.log(
        `${shape.type} | area=${this.area(shape)} | perimeter=${this.perimeter(shape)}`
      );
    }
  }
}

function main() {
  const mgr = new ShapeManager();

  mgr.add(mgr.createShape("circle", 3));
  mgr.add(mgr.createShape("rectangle", 2, 5));
  mgr.add(mgr.createShape("square", 4));

  // Demonstra LSP quebrando expectativa: “retângulo” deveria aceitar width/height independentes
  const squarePretendingRectangle = mgr.createShape("square", 2);
  mgr.setRectangleWidth(squarePretendingRectangle, 5);
  mgr.setRectangleHeight(squarePretendingRectangle, 4);
  // Após isso, o “quadrado” vira um estado inconsistente com a intenção do chamador.

  mgr.add(squarePretendingRectangle);

  mgr.printReport();
  mgr.saveToDisk("/tmp/shapes.bad.json");
}

if (require.main === module) {
  main();
}

module.exports = { ShapeManager, main };
