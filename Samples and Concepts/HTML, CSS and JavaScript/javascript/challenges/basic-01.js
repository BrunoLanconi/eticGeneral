// ==========================================
// DESAFIOS BÁSICOS DE JAVASCRIPT
// Foco: Operadores, Condições e Funções
// ==========================================

// Nota:
// - Este arquivo era um enunciado em formato “markdown”.
// - Foi convertido para um .js válido (sem ``` e sem texto solto).
// - Cada desafio está dentro de um bloco { ... } para evitar conflitos de variáveis.

// ------------------------------------------
// DESAFIO 1 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const a = 10;
  const b = 5;

  console.log(a + b);
  // Resposta (anotação): irá logar "15"
}

// ------------------------------------------
// DESAFIO 2 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const x = "10";
  const y = 10;

  console.log(x == y); // x é igual em valor a y? true
  console.log(x === y); // x é igual em valor e tipo a y? false
  console.log(x != y); // x é diferente em valor a y? false
  console.log(x !== y); // x é diferente em valor ou tipo a y? true
}

// ------------------------------------------
// DESAFIO 3 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const n = 7;

  console.log(n > 10);
  console.log(n <= 7);
}

// ------------------------------------------
// DESAFIO 4 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  let saldo = 50;
  saldo = saldo - 20;
  console.log(saldo);
}

// Versão equivalente:
{
  const saldo = 50;
  const valorADebitar = 20;
  const saldoFinal = saldo - valorADebitar;

  console.log(`Seu saldo final é ${saldoFinal}. Seu inicial era ${saldo}.`);
}

// ------------------------------------------
// DESAFIO 5 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const idade = 18;

  if (idade >= 18) {
    console.log("Maior de idade");
  } else {
    console.log("Menor de idade");
  }
}

// ------------------------------------------
// DESAFIO 6 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const temperatura = 30;

  if (temperatura < 15) {
    console.log("Frio");
  } else if (temperatura < 25) {
    console.log("Agradável");
  } else {
    console.log("Quente");
  }
}

// ------------------------------------------
// DESAFIO 7 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const a = 3;
  const b = 4;

  console.log(a * b);
  console.log(a / b);
}

// ------------------------------------------
// DESAFIO 8 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const nome = "Ana";
  const sobrenome = "Silva";

  console.log(nome + " " + sobrenome);
}

// ------------------------------------------
// DESAFIO 9 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const valor = 0;

  if (valor) {
    console.log("Entrou no IF");
  } else {
    console.log("Entrou no ELSE");
  }
}

// ------------------------------------------
// DESAFIO 10 - Análise de código
// ------------------------------------------
// Dado o código abaixo, o que será impresso no console?
{
  const a = 5;
  const b = 5;

  console.log(a != b);
  console.log(a !== "5");
}

// ------------------------------------------
// DESAFIO 11 - Correção de código
// ------------------------------------------
// O código abaixo contém um erro. Corrija para funcionar corretamente.
// (Original comentado para o arquivo continuar executável.)
// let x = 20;
// console.log(y);
{
  const x = 20;
  console.log(x);
}

// ------------------------------------------
// DESAFIO 12 - Correção de código
// ------------------------------------------
// O código abaixo contém um erro. Corrija para funcionar corretamente.
// const idade = 19;
// idade = 20;
// console.log(idade);
{
  let idade = 19;
  idade = 20;
  console.log(idade);
}

// ------------------------------------------
// DESAFIO 13 - Correção de código
// ------------------------------------------
// O código abaixo deveria imprimir “Aprovado” quando nota for maior ou igual a 7. Corrija.
// let nota = 7;
// if (nota = 7) {
//   console.log("Aprovado");
// } else {
//   console.log("Reprovado");
// }
{
  const nota = 7;

  if (nota >= 7) {
    console.log("Aprovado");
  } else {
    console.log("Reprovado");
  }
}

// ------------------------------------------
// DESAFIO 14 - Correção de código
// ------------------------------------------
// O código abaixo deveria imprimir “Senha correta” quando a senha for exatamente "1234". Corrija.
// let senha = 1234;
// if (senha === "1234") {
//   console.log("Senha correta");
// } else {
//   console.log("Senha incorreta");
// }
{
  const senha = "1234";

  if (senha === "1234") {
    console.log("Senha correta");
  } else {
    console.log("Senha incorreta");
  }
}

// ------------------------------------------
// DESAFIO 15 - Correção de código
// ------------------------------------------
// O código abaixo deveria somar 2 números e imprimir o resultado. Corrija.
// let a = 10;
// let b = 5;
// console.log("Resultado: " + a - b);
{
  const a = 10;
  const b = 5;
  console.log("Resultado: " + (a + b));
}

// ------------------------------------------
// DESAFIO 16 - Correção de código
// ------------------------------------------
// O código abaixo deveria imprimir “Pode entrar” se a idade for maior ou igual a 18. Corrija.
// let idade = 18;
// if (idade > 18) {
//   console.log("Pode entrar");
// } else {
//   console.log("Não pode entrar");
// }
{
  const idade = 18;

  if (idade >= 18) {
    console.log("Pode entrar");
  } else {
    console.log("Não pode entrar");
  }
}

// ------------------------------------------
// DESAFIO 17 - Correção de código
// ------------------------------------------
// O código abaixo contém um erro de variável. Corrija.
// let preco = 100;
// let desconto = 20;
// let total = preco - desonto;
// console.log(total);
{
  const preco = 100;
  const desconto = 20;
  const total = preco - desconto;
  console.log(total);
}

// ------------------------------------------
// DESAFIO 18 - Correção de código
// ------------------------------------------
// O código abaixo deveria imprimir “É igual” quando os valores forem iguais (considerando tipo e valor). Corrija.
// let a = 5;
// let b = "5";
// if (a == b) {
//   console.log("É igual");
// } else {
//   console.log("É diferente");
// }
{
  const a = 5;
  const b = "5";

  if (a === Number(b)) {
    console.log("É igual");
  } else {
    console.log("É diferente");
  }
}

// ------------------------------------------
// DESAFIO 19 - Correção de código
// ------------------------------------------
// O código abaixo deveria imprimir o valor atualizado de pontos. Corrija.
// let pontos = 10;
// pontos + 5;
// console.log(pontos);
{
  let pontos = 10;
  pontos += 5;
  console.log(pontos);
}

// ------------------------------------------
// DESAFIO 20 - Correção de código
// ------------------------------------------
// O código abaixo deveria imprimir “Par” quando o número for par. Corrija.
// let numero = 8;
// if (numero / 2 == 0) {
//   console.log("Par");
// } else {
//   console.log("Ímpar");
// }
{
  const numero = 8;

  if (numero % 2 === 0) {
    console.log("Par");
  } else {
    console.log("Ímpar");
  }
}

// ------------------------------------------
// DESAFIO 21 - Escrita de função
// ------------------------------------------
// Crie uma função soma(a, b) que receba dois números e imprima no console a soma deles.
function soma(a, b) {
  console.log(a + b);
}

// ------------------------------------------
// DESAFIO 22 - Escrita de função
// ------------------------------------------
// Crie uma função comparar(a, b) que imprima:
// - "a é maior" se a > b
// - "b é maior" se b > a
// - "são iguais" se a === b
function comparar(a, b) {
  if (a > b) {
    console.log("a é maior");
  } else if (b > a) {
    console.log("b é maior");
  } else {
    console.log("são iguais");
  }
}

// ------------------------------------------
// DESAFIO 23 - Escrita de script
// ------------------------------------------
// Defina a variável horarioDeEntrada (número) e verifique se o funcionário chegou no horário (entre 8 e 9, inclusive).
// - Se chegou, imprima "Acesso permitido"
// - Caso contrário, imprima "Acesso negado"
{
  const horarioDeEntrada = 8;

  if (horarioDeEntrada >= 8 && horarioDeEntrada <= 9) {
    console.log("Acesso permitido");
  } else {
    console.log("Acesso negado");
  }
}

// ------------------------------------------
// DESAFIO 24 - Escrita de função
// ------------------------------------------
// Crie uma função ehMaiorDeIdade(idade) que retorne:
// - true se idade >= 18
// - false caso contrário
function ehMaiorDeIdade(idade) {
  return idade >= 18;
}

// ------------------------------------------
// DESAFIO 25 - Escrita de função
// ------------------------------------------
// Crie uma função desconto(preco, porcentagem) que:
// - Calcule o preço final com desconto
// - Imprima o preço final no console
function desconto(preco, porcentagem) {
  const precoFinal = preco - (preco * porcentagem) / 100;
  console.log(precoFinal);
}

// ------------------------------------------
// DESAFIO 26 - Escrita de função
// ------------------------------------------
// Crie uma função verificarNota(nota) que imprima:
// - "Aprovado" se nota >= 7
// - "Recuperação" se nota >= 5 e nota < 7
// - "Reprovado" se nota < 5
function verificarNota(nota) {
  if (nota >= 7) {
    console.log("Aprovado");
  } else if (nota >= 5) {
    console.log("Recuperação");
  } else {
    console.log("Reprovado");
  }
}

// ------------------------------------------
// DESAFIO 27 - Escrita de função
// ------------------------------------------
// Crie uma função maiorOuIgualDez(numero) que imprima:
// - "Sim" se numero >= 10
// - "Não" se numero < 10
function maiorOuIgualDez(numero) {
  if (numero >= 10) {
    console.log("Sim");
  } else {
    console.log("Não");
  }
}

// ------------------------------------------
// DESAFIO 28 - Escrita de função
// ------------------------------------------
// Crie uma função compararComZero(n) que imprima:
// - "Positivo" se n > 0
// - "Zero" se n === 0
// - "Negativo" se n < 0
function compararComZero(n) {
  if (n > 0) {
    console.log("Positivo");
  } else if (n === 0) {
    console.log("Zero");
  } else {
    console.log("Negativo");
  }
}

// ------------------------------------------
// DESAFIO 29 - Escrita de função
// ------------------------------------------
// Crie uma função calcularMedia(a, b) que:
// - Calcule a média de a e b
// - Imprima "Passou" se a média for >= 7, senão imprima "Não passou"
function calcularMedia(a, b) {
  const media = (a + b) / 2;

  if (media >= 7) {
    console.log("Passou");
  } else {
    console.log("Não passou");
  }
}

// ------------------------------------------
// DESAFIO 30 - Escrita de função
// ------------------------------------------
// Crie uma função podeDirigir(idade, temCarteira) que imprima:
// - "Pode dirigir" se idade >= 18 e temCarteira === true
// - "Não pode dirigir" caso contrário
function podeDirigir(idade, temCarteira) {
  if (idade >= 18 && temCarteira === true) {
    console.log("Pode dirigir");
  } else {
    console.log("Não pode dirigir");
  }
}

// ==========================================
// FIM DOS DESAFIOS
// ==========================================
