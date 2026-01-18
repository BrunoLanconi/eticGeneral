## Definir uma classe simples

Em JavaScript, uma classe é declarada com `class` e normalmente inicializada com `constructor`.

### Exemplo
```javascript
class Dog {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sit() {
    console.log(`${this.name} is now sitting.`);
  }

  rollOver() {
    console.log(`${this.name} rolled over!`);
  }
}

const myDog = new Dog("Willie", 6);
console.log(myDog.name);
myDog.sit();
myDog.rollOver();
```

---

## Métodos

### Exemplo
```javascript
class Car {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  getDescriptiveName() {
    return `${this.year} ${this.make} ${this.model}`;
  }
}

const myNewCar = new Car("audi", "a4", 2019);
console.log(myNewCar.getDescriptiveName());
```

---

## Herança (`extends`) e `super`

### Exemplo
```javascript
class ElectricCar extends Car {
  constructor(make, model, year) {
    super(make, model, year);
    this.batterySize = 75;
  }

  describeBattery() {
    console.log(`This car has a ${this.batterySize}-kWh battery.`);
  }
}

const myTesla = new ElectricCar("tesla", "model s", 2019);
console.log(myTesla.getDescriptiveName());
myTesla.describeBattery();
```

---

## Encapsulamento (campos privados `#`)

Campos privados são suportados em JavaScript moderno.

### Exemplo
```javascript
class BankAccount {
  #balance;

  constructor(owner, balance = 0) {
    this.owner = owner;
    this.#balance = balance;
  }

  deposit(amount) {
    if (amount > 0) this.#balance += amount;
  }

  withdraw(amount) {
    if (amount > 0 && amount <= this.#balance) this.#balance -= amount;
  }

  getBalance() {
    return this.#balance;
  }
}

const account = new BankAccount("John Doe", 1000);
account.deposit(500);
account.withdraw(200);
console.log(account.getBalance());
```

---

## Polimorfismo (override de métodos)

### Exemplo
```javascript
class Cat {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} says Meow!`;
  }
}

class Dog2 {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} says Woof!`;
  }
}

const animals = [new Cat("Whiskers"), new Dog2("Fido")];
for (const animal of animals) {
  console.log(animal.speak());
}
```

---

## Getters / Setters e métodos `static`

### Exemplo
```javascript
class Circle {
  constructor(radius = 1) {
    this.radius = radius;
  }

  get area() {
    return Math.PI * this.radius ** 2;
  }

  static fromDiameter(diameter) {
    return new Circle(diameter / 2);
  }
}

const circle = new Circle(5);
console.log(circle.area);

const c2 = Circle.fromDiameter(10);
console.log(c2.radius);
```
