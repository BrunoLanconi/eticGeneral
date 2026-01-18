## Arrays

Arrays são listas ordenadas (mutáveis) de elementos.

### Exemplo
```javascript
const fruits = ["apple", "banana", "cherry"];
console.log(fruits);

fruits.push("orange");
console.log(fruits);

fruits.splice(fruits.indexOf("banana"), 1);
console.log(fruits);

console.log(fruits[1]);

for (const fruit of fruits) {
  console.log(fruit);
}
```

---

## Objects

Objetos (`{}`) representam pares chave/valor. As chaves são strings (ou `Symbol`).

### Exemplo
```javascript
const person = {
  name: "John",
  age: 30,
  city: "New York",
};

console.log(person.name);

person.email = "john@example.com";
console.log(person);

delete person.age;
console.log(person);

for (const [key, value] of Object.entries(person)) {
  console.log(key, value);
}
```

---

## Map

`Map` é uma estrutura chave/valor onde as chaves podem ser qualquer tipo (incluindo objetos).

### Exemplo
```javascript
const scores = new Map();

scores.set("Alice", 90);
scores.set("Bob", 85);

console.log(scores.get("Alice"));

for (const [name, score] of scores.entries()) {
  console.log(name, score);
}
```

---

## Set

`Set` guarda valores únicos (sem duplicados).

### Exemplo
```javascript
const tags = new Set(["js", "node", "js"]);
console.log(tags.size); // 2

tags.add("web");
tags.delete("node");

for (const tag of tags) {
  console.log(tag);
}
```

---

## Array de Objects

Um padrão muito comum é uma lista de objetos.

### Exemplo
```javascript
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25 },
  { name: "Doe", age: 35 },
];

console.log(people[1].name); // "Jane"

for (const person of people) {
  console.log(person.name, person.age);
}
```

---

## Objects Aninhados (Nested Objects)

Objetos dentro de objetos ajudam a representar estruturas mais complexas.

### Exemplo
```javascript
const family = {
  child1: { name: "John", age: 30 },
  child2: { name: "Jane", age: 25 },
};

console.log(family.child1.name);

for (const [child, info] of Object.entries(family)) {
  console.log(`${child}: ${info.name} tem ${info.age} anos`);
}
```
