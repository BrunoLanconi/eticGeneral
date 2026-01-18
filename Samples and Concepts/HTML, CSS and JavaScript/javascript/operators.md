## Operadores Lógicos

### AND (`&&`)

Retorna `true` se ambos os operandos forem `true`.

```javascript
if (condicao1 && condicao2) {
   // executa se ambas forem verdadeiras
}
```

---

### OR (`||`)

Retorna `true` se pelo menos um dos operandos for `true`.

```javascript
if (condicao1 || condicao2) {
   // executa se pelo menos uma for verdadeira
}
```

---

### NOT (`!`)

Inverte o valor booleano (verdadeiro ↔ falso).

```javascript
if (!condicao) {
   // executa se a condição for falsa
}
```

---

## Operador Ternário (`? :`)

Uma forma concisa de expressar uma condição (atalho de `if/else`).

```javascript
const resultado = condicao ? valorSeVerdadeiro : valorSeFalso;
```

---

## Igualdade

### Igualdade “solta” (`==`) vs igualdade estrita (`===`)

- `==` pode fazer conversões de tipo (coerção).
- `===` compara valor e tipo (recomendado na maioria dos casos).

```javascript
console.log(1 == "1");   // true
console.log(1 === "1");  // false
```

---

### Diferença “solta” (`!=`) vs diferença estrita (`!==`)

```javascript
console.log(0 != false);   // false
console.log(0 !== false);  // true
```

---

## Comparação

### Menor/maior

```javascript
console.log(2 < 3);   // true
console.log(3 > 2);   // true
console.log(3 <= 3);  // true
console.log(4 >= 5);  // false
```

---

## Operadores Numéricos (aritmética)

```javascript
console.log(10 + 3);
console.log(10 - 3);
console.log(10 * 3);
console.log(10 / 3);
console.log(10 % 3);
console.log(2 ** 3);
```

---

## Atribuição

```javascript
let x = 10;
x += 5;
x *= 2;
console.log(x);
```

Use `let` ou `const` para declarar variáveis.

- `let` permite reatribuição.
- `const` cria uma constante (não pode ser reatribuída).

Em ambos os casos, o escopo é de bloco (`{ ... }`). Isto significa que a variável só existe dentro do bloco onde foi declarada. Por exemplo:

```javascript
if (true) {
   let a = 5;
   const b = 10;
   console.log(a + b); // 15
}
// console.log(a); // Erro: a não está definido
// console.log(b); // Erro: b não está definido
```

---

## Operador de Coalescência Nula (`??`)

Usa o valor da direita apenas quando o da esquerda é `null` ou `undefined`.

```javascript
const input = "";
console.log(input ?? "default"); // "" (não troca)

const maybeNull = null;
console.log(maybeNull ?? "default"); // "default"
```
