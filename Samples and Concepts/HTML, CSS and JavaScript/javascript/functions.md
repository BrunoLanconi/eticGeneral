## Definir uma função simples

### Exemplo
```javascript
function greet() {
  console.log("Hello, World!");
}

greet();
```

---

## Função com parâmetros

### Exemplo
```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}

greet("Alice");
```

---

## Função com retorno

### Exemplo
```javascript
function add(a, b) {
  return a + b;
}

const result = add(5, 3);
console.log(result);
```

---

## Valores por omissão (default parameters)

### Exemplo
```javascript
function greet(name = "World") {
  console.log(`Hello, ${name}!`);
}

greet();
greet("Alice");
```

---

## “Keyword arguments” (parâmetros nomeados via objeto)

JavaScript não tem *keyword arguments* como Python, mas um padrão comum é receber um objeto e fazer *destructuring*.

### Exemplo
```javascript
function describePet({ petName, animalType = "dog" }) {
  console.log(`I have a ${animalType} named ${petName}.`);
}

describePet({ petName: "Willie" });
describePet({ petName: "Harry", animalType: "cat" });
```

---

## Número arbitrário de argumentos (rest parameters)

### Exemplo
```javascript
function makePizza(...toppings) {
  console.log("Making a pizza with:");
  for (const topping of toppings) {
    console.log(`- ${topping}`);
  }
}

makePizza("pepperoni", "mushrooms", "extra cheese");
```

---

## Arrow functions

Arrow functions são muito comuns, especialmente como callbacks.

### Exemplo
```javascript
const add = (x, y) => x + y;
console.log(add(5, 3));

const square = (x) => x ** 2;
console.log(square(4));
```

---

## Funções aninhadas e closures

### Exemplo
```javascript
function outerFunction(text) {
  function innerFunction() {
    console.log(text);
  }

  innerFunction();
}

outerFunction("Hello from the inner function!");
```

---

## Documentação (JSDoc)

### Exemplo
```javascript
/**
 * Soma dois números.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function addNumbers(a, b) {
  return a + b;
}
```
