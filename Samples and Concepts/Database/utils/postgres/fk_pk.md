# Chaves primárias e estrangeiras

Chaves primárias e estrangeiras são conceitos importantes em bancos de dados relacionais. Uma chave primária é uma coluna ou conjunto de colunas que identifica unicamente cada linha em uma tabela. Uma chave estrangeira é uma coluna ou conjunto de colunas que estabelece uma relação entre duas tabelas.

## `PRIMARY KEY`

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);
```

Este comando cria uma tabela `users` com uma chave primária `id` auto-incrementada.

---

## `FOREIGN KEY`

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  total DECIMAL(10, 2)
);
```

Este comando cria uma tabela `orders` com uma chave estrangeira `user_id` que referencia a coluna `id` da tabela `users`.

---

## `ON DELETE CASCADE`

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  total DECIMAL(10, 2)
);
```

Este comando cria uma tabela `orders` com uma chave estrangeira `user_id` que referencia a coluna `id` da tabela `users` e deleta automaticamente todas as ordens associadas a um usuário quando o usuário é removido.

---

## `ON UPDATE CASCADE`

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON UPDATE CASCADE,
  total DECIMAL(10, 2)
);
```

Este comando cria uma tabela `orders` com uma chave estrangeira `user_id` que referencia a coluna `id` da tabela `users` e atualiza automaticamente o `user_id` em todas as ordens associadas a um usuário quando o `id` do usuário é atualizado.
