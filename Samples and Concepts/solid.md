# Princípios SOLID

## Introdução

SOLID é um acrônimo para cinco princípios de design de software orientado a objetos, criados por Robert C. Martin (Uncle Bob). Esses princípios ajudam a criar código mais:

- **Manutenível**: Fácil de modificar
- **Flexível**: Fácil de estender
- **Testável**: Fácil de testar
- **Reutilizável**: Componentes podem ser reutilizados
- **Compreensível**: Mais fácil de entender

---

## S - Single Responsibility Principle

**"Uma classe deve ter uma, e somente uma, razão para mudar."**

Cada módulo, classe ou função deve ter responsabilidade sobre uma única parte da funcionalidade.

### ❌ Violação do SRP

```javascript
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  // Responsabilidade 1: Gerenciar dados do usuário
  getName() {
    return this.name;
  }

  // Responsabilidade 2: Persistência de dados
  save() {
    const db = Database.connect();
    db.query(`INSERT INTO users (name, email) VALUES ('${this.name}', '${this.email}')`);
  }

  // Responsabilidade 3: Enviar email
  sendEmail(message) {
    const smtp = SMTP.connect();
    smtp.send(this.email, message);
  }

  // Responsabilidade 4: Validação
  validate() {
    if (!this.email.includes('@')) {
      throw new Error('Invalid email');
    }
  }
}
```

**Problemas:**
- Muitas razões para mudar a classe
- Difícil de testar
- Difícil de reutilizar

### ✅ Seguindo o SRP

```javascript
// Responsabilidade: Representar dados do usuário
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  getName() {
    return this.name;
  }

  getEmail() {
    return this.email;
  }
}

// Responsabilidade: Validar usuário
class UserValidator {
  validate(user) {
    if (!user.getEmail().includes('@')) {
      throw new Error('Invalid email');
    }
    
    if (user.getName().length < 3) {
      throw new Error('Name too short');
    }
    
    return true;
  }
}

// Responsabilidade: Persistir usuário
class UserRepository {
  constructor(database) {
    this.database = database;
  }

  save(user) {
    return this.database.query(
      'INSERT INTO users (name, email) VALUES (?, ?)',
      [user.getName(), user.getEmail()]
    );
  }

  findById(id) {
    const data = this.database.query('SELECT * FROM users WHERE id = ?', [id]);
    return new User(data.name, data.email);
  }
}

// Responsabilidade: Enviar emails
class EmailService {
  constructor(smtpConfig) {
    this.smtp = SMTP.connect(smtpConfig);
  }

  send(to, subject, message) {
    return this.smtp.send({ to, subject, message });
  }
}

// Uso
const user = new User('João Silva', 'joao@example.com');
const validator = new UserValidator();
const repository = new UserRepository(database);
const emailService = new EmailService(smtpConfig);

validator.validate(user);
repository.save(user);
emailService.send(user.getEmail(), 'Welcome', 'Welcome to our app!');
```

**Benefícios:**
- Cada classe tem uma única responsabilidade
- Fácil de testar cada componente isoladamente
- Mudanças em uma funcionalidade não afetam outras
- Componentes são reutilizáveis

---

## O - Open/Closed Principle

**"Entidades de software devem estar abertas para extensão, mas fechadas para modificação."**

Você deve poder adicionar novas funcionalidades sem modificar código existente.

### ❌ Violação do OCP

```javascript
class PaymentProcessor {
  processPayment(amount, paymentType) {
    if (paymentType === 'credit_card') {
      console.log(`Processing credit card payment of $${amount}`);
      // Lógica do cartão de crédito
    } else if (paymentType === 'paypal') {
      console.log(`Processing PayPal payment of $${amount}`);
      // Lógica do PayPal
    } else if (paymentType === 'bitcoin') {
      console.log(`Processing Bitcoin payment of $${amount}`);
      // Lógica do Bitcoin
    }
    // Para adicionar novo método, precisa modificar esta classe
  }
}
```

**Problemas:**
- Adicionar novo método de pagamento requer modificar a classe
- Viola o princípio de "fechado para modificação"
- Aumenta complexidade ciclomática

### ✅ Seguindo o OCP

```javascript
// Interface (conceitual em JavaScript)
class PaymentMethod {
  process(amount) {
    throw new Error('Method process() must be implemented');
  }
}

// Implementações específicas
class CreditCardPayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing credit card payment of $${amount}`);
    // Lógica específica do cartão
    return { success: true, method: 'credit_card', amount };
  }
}

class PayPalPayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing PayPal payment of $${amount}`);
    // Lógica específica do PayPal
    return { success: true, method: 'paypal', amount };
  }
}

class BitcoinPayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing Bitcoin payment of $${amount}`);
    // Lógica específica do Bitcoin
    return { success: true, method: 'bitcoin', amount };
  }
}

// Processador não precisa ser modificado para novos métodos
class PaymentProcessor {
  constructor(paymentMethod) {
    this.paymentMethod = paymentMethod;
  }

  processPayment(amount) {
    return this.paymentMethod.process(amount);
  }
}

// Uso
const creditCardProcessor = new PaymentProcessor(new CreditCardPayment());
creditCardProcessor.processPayment(100);

const paypalProcessor = new PaymentProcessor(new PayPalPayment());
paypalProcessor.processPayment(200);

// Adicionar novo método não requer modificar PaymentProcessor
class PixPayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing PIX payment of $${amount}`);
    return { success: true, method: 'pix', amount };
  }
}

const pixProcessor = new PaymentProcessor(new PixPayment());
pixProcessor.processPayment(150);
```

**Benefícios:**
- Adicionar novos métodos de pagamento não modifica código existente
- Cada método de pagamento é independente
- Fácil de testar cada método isoladamente

---

## L - Liskov Substitution Principle

**"Objetos de uma classe derivada devem poder substituir objetos da classe base sem quebrar a aplicação."**

Subclasses devem ser substituíveis por suas classes base.

### ❌ Violação do LSP

```javascript
class Bird {
  fly() {
    console.log('Flying...');
  }
}

class Sparrow extends Bird {
  fly() {
    console.log('Sparrow flying');
  }
}

class Penguin extends Bird {
  fly() {
    // Pinguins não voam!
    throw new Error('Penguins cannot fly');
  }
}

// Uso
function makeBirdFly(bird) {
  bird.fly(); // Quebra se for um Penguin
}

makeBirdFly(new Sparrow()); // OK
makeBirdFly(new Penguin());  // Error!
```

**Problema:**
- Penguin não pode substituir Bird
- Quebra o contrato da classe base

### ✅ Seguindo o LSP

```javascript
// Classe base mais genérica
class Bird {
  eat() {
    console.log('Eating...');
  }
}

// Interface para pássaros que voam
class FlyingBird extends Bird {
  fly() {
    console.log('Flying...');
  }
}

// Sparrow pode voar
class Sparrow extends FlyingBird {
  fly() {
    console.log('Sparrow flying');
  }
}

// Penguin é apenas um Bird
class Penguin extends Bird {
  swim() {
    console.log('Penguin swimming');
  }
}

// Uso
function makeBirdFly(bird) {
  if (bird instanceof FlyingBird) {
    bird.fly();
  } else {
    console.log('This bird cannot fly');
  }
}

makeBirdFly(new Sparrow()); // "Sparrow flying"
makeBirdFly(new Penguin());  // "This bird cannot fly"
```

**Outro Exemplo:**

```javascript
// ❌ Violação
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  setWidth(width) {
    this.width = width;
  }

  setHeight(height) {
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  setWidth(width) {
    this.width = width;
    this.height = width; // Quebra o contrato
  }

  setHeight(height) {
    this.width = height;  // Quebra o contrato
    this.height = height;
  }
}

// Teste
function testRectangle(rectangle) {
  rectangle.setWidth(5);
  rectangle.setHeight(4);
  console.log(rectangle.getArea()); // Espera 20
}

testRectangle(new Rectangle(0, 0)); // 20 ✓
testRectangle(new Square(0, 0));     // 16 ✗ (quebra expectativa)
```

```javascript
// ✅ Seguindo LSP
class Shape {
  getArea() {
    throw new Error('Method must be implemented');
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

class Square extends Shape {
  constructor(side) {
    super();
    this.side = side;
  }

  getArea() {
    return this.side * this.side;
  }
}
```

---

## I - Interface Segregation Principle

**"Nenhum cliente deve ser forçado a depender de métodos que não usa."**

Muitas interfaces específicas são melhores que uma interface geral.

### ❌ Violação do ISP

```javascript
// Interface "gorda" com muitos métodos
class Worker {
  work() {
    throw new Error('Method must be implemented');
  }

  eat() {
    throw new Error('Method must be implemented');
  }

  sleep() {
    throw new Error('Method must be implemented');
  }

  charge() {
    throw new Error('Method must be implemented');
  }
}

class HumanWorker extends Worker {
  work() {
    console.log('Human working');
  }

  eat() {
    console.log('Human eating');
  }

  sleep() {
    console.log('Human sleeping');
  }

  charge() {
    // Humanos não precisam carregar!
    throw new Error('Humans do not charge');
  }
}

class RobotWorker extends Worker {
  work() {
    console.log('Robot working');
  }

  eat() {
    // Robôs não comem!
    throw new Error('Robots do not eat');
  }

  sleep() {
    // Robôs não dormem!
    throw new Error('Robots do not sleep');
  }

  charge() {
    console.log('Robot charging');
  }
}
```

**Problema:**
- Classes são forçadas a implementar métodos que não usam
- Interface muito genérica

### ✅ Seguindo o ISP

```javascript
// Interfaces segregadas e específicas
class Workable {
  work() {
    throw new Error('Method must be implemented');
  }
}

class Eatable {
  eat() {
    throw new Error('Method must be implemented');
  }
}

class Sleepable {
  sleep() {
    throw new Error('Method must be implemented');
  }
}

class Chargeable {
  charge() {
    throw new Error('Method must be implemented');
  }
}

// Humano implementa apenas o que precisa
class HumanWorker extends Workable {
  constructor() {
    super();
    this.eatable = new class extends Eatable {
      eat() {
        console.log('Human eating');
      }
    };
    this.sleepable = new class extends Sleepable {
      sleep() {
        console.log('Human sleeping');
      }
    };
  }

  work() {
    console.log('Human working');
  }

  eat() {
    this.eatable.eat();
  }

  sleep() {
    this.sleepable.sleep();
  }
}

// Robô implementa apenas o que precisa
class RobotWorker extends Workable {
  constructor() {
    super();
    this.chargeable = new class extends Chargeable {
      charge() {
        console.log('Robot charging');
      }
    };
  }

  work() {
    console.log('Robot working');
  }

  charge() {
    this.chargeable.charge();
  }
}
```

**Exemplo com Composição:**

```javascript
// Interfaces pequenas
const Workable = {
  work() {
    console.log(`${this.name} working`);
  }
};

const Eatable = {
  eat() {
    console.log(`${this.name} eating`);
  }
};

const Sleepable = {
  sleep() {
    console.log(`${this.name} sleeping`);
  }
};

const Chargeable = {
  charge() {
    console.log(`${this.name} charging`);
  }
};

// Compor funcionalidades
class HumanWorker {
  constructor(name) {
    this.name = name;
    Object.assign(this, Workable, Eatable, Sleepable);
  }
}

class RobotWorker {
  constructor(name) {
    this.name = name;
    Object.assign(this, Workable, Chargeable);
  }
}

// Uso
const human = new HumanWorker('João');
human.work();   // "João working"
human.eat();    // "João eating"
human.sleep();  // "João sleeping"

const robot = new RobotWorker('R2D2');
robot.work();   // "R2D2 working"
robot.charge(); // "R2D2 charging"
// robot.eat(); // undefined (não existe)
```

---

## D - Dependency Inversion Principle

**"Dependa de abstrações, não de implementações concretas."**

Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

### ❌ Violação do DIP

```javascript
// Implementação concreta de baixo nível
class MySQLDatabase {
  connect() {
    console.log('Connecting to MySQL');
  }

  query(sql) {
    console.log(`Executing MySQL query: ${sql}`);
    return [];
  }
}

// Módulo de alto nível depende de implementação concreta
class UserRepository {
  constructor() {
    this.database = new MySQLDatabase(); // Dependência hard-coded
  }

  findAll() {
    this.database.connect();
    return this.database.query('SELECT * FROM users');
  }
}

// Problemas:
// - Difícil trocar de MySQL para PostgreSQL
// - Difícil testar (não pode mockar o banco)
// - Alto acoplamento
```

### ✅ Seguindo o DIP

```javascript
// Abstração (interface)
class Database {
  connect() {
    throw new Error('Method must be implemented');
  }

  query(sql) {
    throw new Error('Method must be implemented');
  }
}

// Implementações concretas
class MySQLDatabase extends Database {
  connect() {
    console.log('Connecting to MySQL');
  }

  query(sql) {
    console.log(`Executing MySQL query: ${sql}`);
    return [];
  }
}

class PostgreSQLDatabase extends Database {
  connect() {
    console.log('Connecting to PostgreSQL');
  }

  query(sql) {
    console.log(`Executing PostgreSQL query: ${sql}`);
    return [];
  }
}

class MongoDBDatabase extends Database {
  connect() {
    console.log('Connecting to MongoDB');
  }

  query(filter) {
    console.log(`Executing MongoDB query:`, filter);
    return [];
  }
}

// Módulo de alto nível depende de abstração
class UserRepository {
  constructor(database) {
    this.database = database; // Injeção de dependência
  }

  findAll() {
    this.database.connect();
    return this.database.query('SELECT * FROM users');
  }
}

// Uso - facilmente intercambiável
const mysqlRepo = new UserRepository(new MySQLDatabase());
mysqlRepo.findAll();

const postgresRepo = new UserRepository(new PostgreSQLDatabase());
postgresRepo.findAll();

// Fácil de testar com mock
class MockDatabase extends Database {
  connect() {
    // Não faz nada
  }

  query(sql) {
    return [{ id: 1, name: 'Test User' }];
  }
}

const testRepo = new UserRepository(new MockDatabase());
testRepo.findAll(); // Retorna dados mockados
```

**Exemplo com Dependency Injection:**

```javascript
// Service de envio de email (abstração)
class EmailService {
  send(to, subject, body) {
    throw new Error('Method must be implemented');
  }
}

// Implementações concretas
class SendGridEmailService extends EmailService {
  send(to, subject, body) {
    console.log(`Sending email via SendGrid to ${to}`);
    // Lógica do SendGrid
  }
}

class MailgunEmailService extends EmailService {
  send(to, subject, body) {
    console.log(`Sending email via Mailgun to ${to}`);
    // Lógica do Mailgun
  }
}

// Service de alto nível
class UserService {
  constructor(userRepository, emailService) {
    this.userRepository = userRepository;
    this.emailService = emailService;
  }

  registerUser(userData) {
    const user = this.userRepository.save(userData);
    this.emailService.send(
      user.email,
      'Welcome',
      'Welcome to our platform!'
    );
    return user;
  }
}

// Configuração (Dependency Injection Container)
const database = new MySQLDatabase();
const userRepository = new UserRepository(database);
const emailService = new SendGridEmailService();
const userService = new UserService(userRepository, emailService);

// Fácil trocar implementações
const alternativeEmailService = new MailgunEmailService();
const alternativeUserService = new UserService(userRepository, alternativeEmailService);
```

---

## Conclusão

### Resumo dos Princípios

| Princípio | Descrição                                      | Benefício Principal |
| --------- | ---------------------------------------------- | ------------------- |
| **S**RP   | Uma classe, uma responsabilidade               | Manutenibilidade    |
| **O**CP   | Aberto para extensão, fechado para modificação | Flexibilidade       |
| **L**SP   | Subclasses devem ser substituíveis             | Confiabilidade      |
| **I**SP   | Interfaces específicas, não genéricas          | Desacoplamento      |
| **D**IP   | Dependa de abstrações                          | Testabilidade       |

### Benefícios de Seguir SOLID

1. **Código mais limpo e organizado**
2. **Fácil de testar** (especialmente com DIP)
3. **Fácil de manter** (especialmente com SRP)
4. **Fácil de estender** (especialmente com OCP)
5. **Menos bugs** (especialmente com LSP)
6. **Melhor separação de responsabilidades**
7. **Código mais reutilizável**

### Quando Aplicar

- Em projetos grandes e complexos
- Quando múltiplos desenvolvedores trabalham no código
- Quando o projeto precisa escalar
- Quando testabilidade é importante
- Quando manutenção a longo prazo é necessária

### Cuidados

- **Não exagere**: SOLID não é dogma
- **Comece simples**: Refatore para SOLID quando necessário
- **Balance**: Às vezes um pouco de "impureza" é aceitável
- **Contexto**: Nem todo código precisa ser 100% SOLID
- **Pragmatismo**: O objetivo é código melhor, não perfeição

### Recursos

- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Clean Code - Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [Agile Software Development - Robert C. Martin](https://www.amazon.com/Software-Development-Principles-Patterns-Practices/dp/0135974445)
