// Criem uma classe chamada `Produto`.
// `Categorias` podem ser "eletrodoméstico", "decoração", "materiais de construção", "vestuário"
// Pensem em todos os atributos que um produto pode ter. E.g. `Preço`, `nome`, `fabricante`, `categoria`, `número máximo de parcelas`...
// getValorDaParcela(numeroDeParcelas) -> Deve retornar o valor de cada parcela baseado no this.preco do produto

class Produto {
  constructor(preco, nome, fabricante, categoria, numeroMaximoParcelas) {
    this.preco = preco;
    this.nome = nome;
    this.fabricante = fabricante;
    this.categoria = categoria;

    if (numeroMaximoParcelas < 24) {
      this.numeroMaximoParcelas = numeroMaximoParcelas;  
    } else {
      this.numeroMaximoParcelas = 24;
    }
  }

  getValorDeParcela(numeroDeParcelas) {
    if (numeroDeParcelas > this.numeroMaximoParcelas) {
      throw new Error("Número de parcelas superior ao permitido para o produto");
    }

    return this.preco / numeroDeParcelas;
  }
}

/////////////////////////////////////////////////////////////////////////////////////////////////

// Crie uma lista de produtos. Pelo menos 10 itens.

const produtos = [
  new Produto(2500, "Geladeira", "Brastemp", "eletrodoméstico", 10),
  new Produto(300, "Vaso Decorativo", "Tok&Stok", "decoração", 5),
  new Produto(1500, "Tijolo", "Votorantim", "materiais de construção", 12),
  new Produto(200, "Camisa Polo", "Lacoste", "vestuário", 6),
  new Produto(100, "Calça Jeans", "Levi's", "vestuário", 6),
  new Produto(500, "Micro-ondas", "LG", "eletrodoméstico", 10),
  new Produto(800, "Sofá", "Etna", "decoração", 8),
  new Produto(1200, "Cimento", "Holcim", "materiais de construção", 12),
  new Produto(150, "Camiseta", "Hering", "vestuário", 6),
  new Produto(400, "Liquidificador", "Philco", "eletrodoméstico", 10),
];

/////////////////////////////////////////////////////////////////////////////////////////////////

// Crie uma função que conte o número de produtos da lista que pertencem a uma mesma categoria.

class ListaDeProdutos {
  categoriasAceitas = ["eletrodoméstico", "decoração", "materiais de construção", "vestuário"];

  constructor(listaDeProdutos) {
    this.listaDeProdutos = listaDeProdutos;
  }
  contarPorCategoria(categoria) {
    let contador = 0;

    if (!this.categoriasAceitas.includes(categoria)) {
      console.error(`Categoria ${categoria} não aceita. Categorias aceitas: ${this.categoriasAceitas.join(", ")}`);
      return contador;
    }

    for (const produto of this.listaDeProdutos) {
      if (produto.categoria === categoria) {
        contador++;
      }
    }

    return contador;
  }
}

/////////////////////////////////////////////////////////////////////////////////////////////////

const listaDeProdutos = new ListaDeProdutos(produtos);
console.log(`Número de produtos para a categoria "eletrodoméstico": ${listaDeProdutos.contarPorCategoria("eletrodoméstico")}`);
console.log(`Número de produtos para a categoria "decoração": ${listaDeProdutos.contarPorCategoria("decoração")}`);
console.log(`Número de produtos para a categoria "materiais de construção": ${listaDeProdutos.contarPorCategoria("materiais de construção")}`);
console.log(`Número de produtos para a categoria "vestuário": ${listaDeProdutos.contarPorCategoria("vestuário")}`);
console.log(`Número de produtos para a categoria "alimentos": ${listaDeProdutos.contarPorCategoria("alimentos")}`); // Categoria não aceita

// Número de produtos para a categoria "eletrodoméstico": 3
// Número de produtos para a categoria "decoração": 2
// Número de produtos para a categoria "materiais de construção": 2
// Número de produtos para a categoria "vestuário": 3
// Categoria alimentos não aceita. Categorias aceitas: eletrodoméstico, decoração, materiais de construção, vestuário
// Número de produtos para a categoria "alimentos": 0