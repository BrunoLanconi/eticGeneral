## Valores

### `INSERT INTO VALUES`
```sql
INSERT INTO users (name, email) 
VALUES ('John Doe', 'john.doe@example.com');
```

Este comando insere um novo registro na tabela `users` com o nome "John Doe" e o email "john.doe@example.com".

### `SELECT FROM WHERE`
   
```sql
SELECT * FROM users WHERE email = 'john.doe@example.com';
```

Este comando recupera todos os campos (`*`) da tabela `users` onde o email é igual a "john.doe@example.com".

### `SELECT FROM WHERE LIMIT`

```sql
SELECT name, email FROM users WHERE email = 'john.doe@example.com' LIMIT 1;
```
   
Este comando recupera apenas os campos `name` e `email` da tabela `users` onde o email é igual a "john.doe@example.com", limitando o resultado a 1 registro.

### `UPDATE SET WHERE`

```sql
UPDATE users 
SET email = 'john.newemail@example.com' 
WHERE name = 'John Doe';
```

Este comando atualiza o email de "John Doe" para "john.newemail@example.com" na tabela `users`.

### `DELETE FROM WHERE`

```sql
DELETE FROM users WHERE name = 'John Doe';
```

Este comando remove todos os registros que têm o campo `name` igual a "John Doe" da tabela `users`.

### `SELECT FROM JOIN ON`

```sql
SELECT users.name, orders.total
FROM users
JOIN orders ON users.id = orders.user_id;
```

Este comando recupera o nome do usuário e o total de todas as ordens associadas a esse usuário, combinando as tabelas `users` e `orders` com base na coluna `id` da tabela `users` e na coluna `user_id` da tabela `orders`.

### `SELECT FROM JOIN ON WHERE`

```sql
SELECT users.name, orders.total
FROM users
JOIN orders ON users.id = orders.user_id
WHERE users.name = 'John Doe';
```

Este comando recupera o nome do usuário e o total de todas as ordens associadas a esse usuário, combinando as tabelas `users` e `orders` com base na coluna `id` da tabela `users` e na coluna `user_id` da tabela `orders`, onde o nome do usuário é "John Doe".

### `SELECT FROM LEFT JOIN ON`

```sql
SELECT users.name, orders.total
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

Este comando recupera o nome do usuário e o total de todas as ordens associadas a esse usuário, combinando as tabelas `users` e `orders` com base na coluna `id` da tabela `users` e na coluna `user_id` da tabela `orders`, incluindo todos os usuários, mesmo que eles não tenham ordens associadas.

### `SELECT FROM RIGHT JOIN ON`

```sql
SELECT users.name, orders.total
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
```

Este comando recupera o nome do usuário e o total de todas as ordens associadas a esse usuário, combinando as tabelas `users` e `orders` com base na coluna `id` da tabela `users` e na coluna `user_id` da tabela `orders`, incluindo todas as ordens, mesmo que elas não tenham usuários associados.

## Tabelas

### `CREATE TABLE`

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);
```

Este comando cria uma tabela chamada `users` com três colunas: `id` (chave primária auto-incrementada), `name` (nome do usuário) e `email` (com valor único).

### `CREATE TABLE IF NOT EXISTS`

**Attention**: This command is not supported by all databases. PostgreSQL supports it.

```sql
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);
```

Este comando cria a tabela `users` apenas se ela ainda não existir.

### `ALTER TABLE`

#### `ADD COLUMN`

```sql
ALTER TABLE users ADD COLUMN age INT;
```

Este comando adiciona uma nova coluna `age` à tabela `users`.

#### `ALTER COLUMN`

```sql
ALTER TABLE users ALTER COLUMN name TYPE TEXT;
```

Este comando altera o tipo de dados da coluna `name` de `VARCHAR` para `TEXT`.

#### `RENAME TO`

```sql
ALTER TABLE users RENAME TO customers;
```

Este comando renomeia a tabela `users` para `customers`.

### `DROP TABLE`

```sql
DROP TABLE users;
```

Este comando remove a tabela `users` do banco de dados, junto com todos os seus dados.

### `DROP TABLE IF EXISTS`

```sql
DROP TABLE IF EXISTS users;
```

Este comando remove a tabela `users` do banco de dados, mas apenas se ela existir.

### `TRUNCATE TABLE`

```sql
TRUNCATE TABLE users;
```

Este comando remove todos os registros da tabela `users`, mas mantém sua estrutura intacta.

## Índices

### `CREATE INDEX ON`

```sql
CREATE INDEX idx_users_email ON users(email);
```

Este comando cria um índice chamado `idx_users_email` na coluna `email` da tabela `users`, acelerando as consultas baseadas no email.

### `ALTER INDEX RENAME TO`

```sql
ALTER INDEX idx_users_email RENAME TO index_users_email;
```

Este comando renomeia o índice `idx_users_email` para `index_users_email`.

### `DROP INDEX`

```sql
DROP INDEX idx_users_email;
```

Este comando remove o índice `idx_users_email` da tabela `users`.
