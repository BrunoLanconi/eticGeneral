## **Schemas**

São uma maneira de organizar e agrupar objetos dentro de um banco de dados, como tabelas, views, índices, funções e outros. Eles funcionam como uma camada de organização para os objetos do banco de dados, permitindo a separação lógica entre diferentes conjuntos de dados e funcionalidades.

### Principais características dos **schemas**

1. **Organização**: Dentro de um banco de dados, você pode ter múltiplos schemas, cada um contendo suas próprias tabelas e objetos. Isso facilita a organização e gerenciamento de grandes bancos de dados.

2. **Isolamento**: Schemas permitem que objetos com o mesmo nome coexistam, desde que estejam em schemas diferentes. Por exemplo, você pode ter uma tabela chamada `users` no schema `public` e outra tabela `users` em um schema chamado `admin`.

3. **Segurança e Permissões**: Schemas permitem a definição de permissões específicas para usuários ou grupos de usuários. Você pode, por exemplo, conceder acesso de leitura a certos schemas, mas restringir a escrita ou exclusão em outros.

4. **Namespace**: Schemas são usados como "espaços de nome" para evitar conflitos de nome entre diferentes objetos. Para acessar um objeto específico em um schema, é comum usar a notação `schema.objeto`, como por exemplo `public.users`.

### Exemplos de uso de schemas no PostgreSQL

- O PostgreSQL, por padrão, cria um **schema `public`** onde todas as tabelas e objetos são armazenados, a menos que um outro schema seja especificado.
- Ao criar uma tabela em um schema específico, você pode fazer isso da seguinte forma:
```sql
CREATE SCHEMA admin;
CREATE TABLE admin.users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);
```

Neste exemplo, a tabela `users` foi criada dentro do schema `admin`.

### Exemplo de consulta com schemas:
- Se você tiver duas tabelas chamadas `users` em schemas diferentes (`public` e `admin`), para referenciar uma tabela específica, você usaria:
```sql
SELECT * FROM public.users;  -- Acessa a tabela users no schema public
SELECT * FROM admin.users;   -- Acessa a tabela users no schema admin
```