## For (clássico)

O `for` clássico é útil quando precisa de um contador.

### Exemplo
```javascript
for (let i = 0; i < 5; i += 1) {
  console.log(i);
}
```

---

## For...of (iterar valores)

Use `for...of` para iterar valores de iteráveis (arrays, strings, maps, sets...).

### Exemplo
```javascript
const fruits = ["apple", "banana", "cherry"];

for (const fruit of fruits) {
  console.log(fruit);
}

for (const char of "hello") {
  console.log(char);
}
```

---

## For...in (iterar chaves)

Use `for...in` para iterar chaves enumeráveis de um objeto.

### Exemplo
```javascript
const studentScores = { Alice: 90, Bob: 85, Charlie: 95 };

for (const student in studentScores) {
  console.log(student, studentScores[student]);
}
```

---

## While

O `while` repete enquanto a condição for verdadeira.

### Exemplo
```javascript
let n = 3;

while (n > 0) {
  console.log(n);
  n -= 1;
}
```

---

## Do...while

O `do...while` executa pelo menos uma vez.

### Exemplo
```javascript
let attempts = 0;

do {
  attempts += 1;
  console.log("Tentativa", attempts);
} while (attempts < 3);
```

---

## Break e Continue

- `break` termina o loop.
- `continue` salta para a próxima iteração.

### Exemplo
```javascript
for (let i = 0; i < 10; i += 1) {
  if (i === 5) break;
  console.log(i);
}

for (let i = 0; i < 10; i += 1) {
  if (i % 2 === 0) continue;
  console.log(i);
}
```

---

## Loops aninhados

### Exemplo
```javascript
const adj = ["red", "big", "tasty"];
const fruits = ["apple", "banana", "cherry"];

for (const a of adj) {
  for (const fruit of fruits) {
    console.log(`${a} ${fruit}`);
  }
}
```

---

## Alternativas funcionais (Array helpers)

Muitas vezes, `map`, `filter` e `reduce` tornam o código mais legível.

### Exemplo
```javascript
const numbers = [1, 2, 3, 4, 5];

const squares = numbers.map((n) => n * n);
const evens = numbers.filter((n) => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);

console.log(squares, evens, sum);
```
