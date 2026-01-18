## If / Else

O `if` executa um bloco de código quando uma condição é verdadeira.

### Exemplo
```javascript
const x = 10;

if (x > 5) {
  console.log("x é maior que 5");
}

if (x < 5) {
  console.log("Isto não vai executar");
}
```

---

## Else If

Use `else if` para testar várias condições.

### Exemplo
```javascript
const x = 10;

if (x < 5) {
  console.log("x é menor que 5");
} else if (x === 10) {
  console.log("x é igual a 10");
} else {
  console.log("x não é menor que 5 nem igual a 10");
}
```

---

## Switch

O `switch` é útil quando tem vários casos para o mesmo valor.

### Exemplo
```javascript
const role = "admin";

switch (role) {
  case "admin":
    console.log("Acesso total");
    break;
  case "editor":
    console.log("Pode editar conteúdo");
    break;
  default:
    console.log("Acesso limitado");
}
```

---

## Operador Ternário (`? :`)

Uma forma concisa de escrever um `if/else` que atribui um valor.

### Exemplo
```javascript
const age = 17;
const canVote = age >= 18 ? "Sim" : "Não";
console.log(canVote);
```

---

## Truthy e Falsy

Em JavaScript, algumas coisas são tratadas como `false` em condições. As mais comuns:

- `false`
- `0` e `-0`
- `0n` (BigInt)
- `""` (string vazia)
- `null`
- `undefined`
- `NaN`

Tudo o resto é *truthy* (incluindo `[]` e `{}`).

### Exemplo
```javascript
if ("") {
  console.log("não entra");
}

if ([]) {
  console.log("entra (arrays são truthy)");
}
```

---

## Coalescência Nula (`??`) e Encadeamento Opcional (`?.`)

- `??` usa o valor da direita apenas quando o da esquerda é `null` ou `undefined`.
- `?.` evita erros ao aceder a propriedades de algo que pode ser `null/undefined`.

### Exemplo
```javascript
const user = null;

const name = user?.name ?? "Anónimo";
console.log(name); // "Anónimo"
```
