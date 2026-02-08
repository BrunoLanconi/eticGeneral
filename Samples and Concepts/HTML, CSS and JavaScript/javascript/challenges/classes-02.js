// Estamos simulando programaticamente uma compra em um mercado.

// Crie uma classe chamada `Item`, que represente um item comprado.
// O objeto `Item` deve ter os seguintes atributos: `codigoDoProduto`, `quantidadeComprada` e `precoUnitario`.

class Item {
  constructor(codigoDoProduto, quantidadeComprada, precoUnitario) {
    this.codigoDoProduto = codigoDoProduto;
    this.quantidadeComprada = quantidadeComprada;
    this.precoUnitario = precoUnitario;
  }
}

////////////////////////////////////////////////////////////////////////////////////////

// Crie uma lista de produtos comprados. Pelo menos 5 itens.

const produtosComprados = [
  new Item("Arroz", 2, 20.00),
  new Item("Feijão", 1, 15.00),
  new Item("Macarrão", 3, 10.00),
  new Item("Óleo", 1, 8.00),
  new Item("Açúcar", 2, 5.00)
];

////////////////////////////////////////////////////////////////////////////////////////

// Crie uma classe chamada `carrinhoDeCompras` que receba uma lista de `Item`s.
// A classe deve ter um método chamado `calcularValorTotal` que retorne o valor total da compra (soma do preço de todos os itens, considerando a quantidade comprada de cada item).

class CarrinhoDeCompras {
  constructor(itens) {
    this.itens = itens;
  }

  calcularValorTotal() {
    let valorTotal = 0;

    for (const item of this.itens) {
      valorTotal += item.quantidadeComprada * item.precoUnitario;
    }

    return valorTotal;
  }
}

/////////////////////////////////////////////////////////////////////////////////////////

// Crie uma classe chamada `CaixaRegistradora` que receba um `carrinhoDeCompras`.
// A classe deve ter um método chamado `fecharCompra` que retorne o valor total da compra com um desconto de 10% se o valor total for maior que 500,00 moedas.
// A classe deve também ter um método chamado `imprimirCupom` que exiba no console os detalhes da compra: lista de itens, quantidade comprada de cada item, preço unitário, preço total por item e valor total da compra (com desconto, se aplicável).

// Exemplo de saída:
// ------------------------------
// Cupom Fiscal
// ------------------------------
// Item: Arroz - Quantidade: 2 - Preço Unitário: R$ 20,00 - Preço Total: R$ 40,00
// Item: Feijão - Quantidade: 1 - Preço Unitário: R$ 15,00 - Preço Total: R$ 15,00
// ...
// ------------------------------
// Valor Total: R$ 450,00
// Desconto Aplicado: R$ 45,00
// Valor a Pagar: R$ 405,00
// ------------------------------

class CaixaRegistradora {
  desconto = 0.10;
  valorMinimoParaDesconto = 500.00;

  constructor(carrinho) {
    this.carrinho = carrinho;
    this.valorTotal = this.carrinho.calcularValorTotal();
    this.valorDoDesconto = this.getValorDoDesconto();
    this.valorComDesconto = this.getValorComDesconto();
  }

  getValorDoDesconto() {
    if (this.valorTotal > this.valorMinimoParaDesconto) {
      console.log(`Desconto de ${this.desconto * 100}% aplicado!`);
      return this.valorTotal * this.desconto;
    }

    console.log("Valor total abaixo do mínimo para desconto. Nenhum desconto aplicado.");
    return 0.00;
  }

  getValorComDesconto() {
    return this.valorTotal - this.valorDoDesconto;
  }
}

class CupomFiscal {
  constructor(caixa) {
    this.items = caixa.carrinho.itens;
    this.valorTotal = caixa.valorTotal;
    this.valorDoDesconto = caixa.valorDoDesconto;
    this.valorComDesconto = caixa.valorComDesconto;
  }

  getCabecalho() {
    return [
      "------------------------------",
      "Cupom Fiscal",
      "------------------------------"
    ];
  }

  getContent() {
    const linhas = [];

    for (const item of this.items) {
      const precoTotal = item.quantidadeComprada * item.precoUnitario;

      linhas.push(`Item: ${item.codigoDoProduto} - Quantidade: ${item.quantidadeComprada} - Preço Unitário: R$ ${item.precoUnitario.toFixed(2)} - Preço Total: R$ ${precoTotal.toFixed(2)}`);
    }

    return linhas;
  }

  getRodape() {
    return [
      "------------------------------",
      `Valor Total: R$ ${this.valorTotal.toFixed(2)}`,
      `Desconto Aplicado: R$ ${this.valorDoDesconto.toFixed(2)}`,
      `Valor a Pagar: R$ ${this.valorComDesconto.toFixed(2)}`,
      "------------------------------"
    ];
  }
}

class ImpressoraDeCupom {
  imprimir(cupom) {
    const cabecalho = cupom.getCabecalho();
    const content = cupom.getContent();
    const rodape = cupom.getRodape();

    const linhas = [...cabecalho, ...content, ...rodape];

    for (const linha of linhas) {
      console.log(linha);
    }
  }
}

const carrinho = new CarrinhoDeCompras(produtosComprados);
const caixa = new CaixaRegistradora(carrinho);
const cupom = new CupomFiscal(caixa);
const impressora = new ImpressoraDeCupom();

impressora.imprimir(cupom);