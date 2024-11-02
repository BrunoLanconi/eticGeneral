1. **Base de Dados**: Uma base de dados é uma coleção organizada de dados estruturados, armazenados e acessados eletronicamente. Serve como o repositório central para o armazenamento e gerenciamento de informações críticas em aplicações.

2. **SGBD (Sistema de Gerenciamento de Banco de Dados)**: Software que facilita a criação, manutenção e uso de bases de dados, permitindo a manipulação dos dados de maneira eficiente. Simplifica a interação com os dados e garante integridade, segurança e performance.

- **Exemplos:** MySQL, PostgreSQL, Oracle, SQL Server.

3. **Modelagem de Dados**: Processo de definir a estrutura e os relacionamentos dos dados através de diagramas e modelos. Fundamental para garantir que os dados sejam organizados de maneira lógica e eficiente, facilitando futuras consultas e manipulações.

4. **SQL (Structured Query Language)**: Categoria de SGBD. Linguagem padrão para manipulação de dados em bases de dados relacionais. Permite a execução de consultas, inserção, atualização e exclusão de dados, sendo essencial para o desenvolvimento de aplicações que dependem de dados estruturados.

5. **NoSQL (Not Only SQL)**: Categoria de SGBD. Tipo de base de dados que permite o armazenamento de dados de maneira não estruturada ou semi-estruturada. Crucial para aplicações que exigem alta escalabilidade e que lidam com grandes volumes de dados heterogêneos, como redes sociais e big data.

6. **ORM (Object-Relational Mapping)**: Técnica que permite o mapeamento entre as tabelas do banco de dados e os objetos de uma aplicação. Facilita a integração entre a lógica da aplicação e a base de dados, permitindo que os desenvolvedores trabalhem com dados de maneira mais intuitiva.

7. **Segurança de Dados**: Conjunto de práticas e tecnologias utilizadas para proteger os dados contra acesso não autorizado e corrupção. Essencial para garantir a confidencialidade, integridade e disponibilidade dos dados, especialmente em aplicações sensíveis.

8. **Escalabilidade**: Capacidade do sistema de base de dados de crescer e se adaptar a um aumento na quantidade de dados ou número de usuários. Crucial para aplicações que devem suportar um grande número de acessos simultâneos e um volume crescente de dados.

9.  **Backup e Recuperação**: Processos de criação de cópias de segurança dos dados e de restauração dos mesmos em caso de falha. Garantem a continuidade do serviço e a minimização de perdas de dados, sendo fundamentais em ambientes de produção.

10. **ACID (Atomicity, Consistency, Isolation, Durability)**: Propriedades que garantem a integridade e confiabilidade das transações em bases de dados. Asseguram que as operações sejam realizadas de forma segura e consistente, mesmo em situações de falha.

- **Atomicidade**: Todas as operações de uma transação são executadas com sucesso ou nenhuma é executada. Por exemplo, se uma operação falhar, a transação é revertida.
- **Consistência**: A base de dados permanece consistente antes e depois de uma transação. Por exemplo, as restrições de integridade são mantidas.
- **Isolamento**: As transações são executadas de forma isolada, sem interferir umas nas outras. Por exemplo, uma transação não deve ver os resultados de outra transação que ainda não foi concluída.
- **Durabilidade**: As alterações realizadas por uma transação são permanentes e persistem mesmo em caso de falha do sistema. Por exemplo, após um commit, as alterações são gravadas no disco e não podem ser perdidas.

11. **Commit e Rollback**: Operações utilizadas para confirmar ou desfazer uma transação em um banco de dados. O `commit` salva as alterações realizadas na transação, enquanto o `rollback` desfaz as alterações e restaura o estado anterior.