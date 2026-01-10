```sql
SELECT * 
FROM users
JOIN orders
ON users.id = orders.user_id;
```

```
 id | name  | last_name | id |  total  | user_id
----+-------+-----------+----+---------+---------
  1 | John  | Doe       |  1 |  100.00 |       1
  1 | John  | Doe       |  2 |  200.00 |       1
  1 | John  | Doe       |  3 |  300.00 |       1
  2 | User1 | example   |  4 |  400.00 |       2
  2 | User1 | example   |  5 |  500.00 |       2
  2 | User1 | example   |  6 |  600.00 |       2
  3 | User2 | example   |  7 |  700.00 |       3
  3 | User2 | example   |  8 |  800.00 |       3
  3 | User2 | example   |  9 |  900.00 |       3
  4 | User3 | example   | 10 | 1000.00 |       4
  4 | User3 | example   | 11 | 1100.00 |       4
  4 | User3 | example   | 12 | 1200.00 |       4
  5 | User4 | example   | 13 | 1300.00 |       5
  5 | User4 | example   | 14 | 1400.00 |       5
  5 | User4 | example   | 15 | 1500.00 |       5
```

```sql
SELECT users.name, orders.total 
FROM users
JOIN orders
ON users.id = orders.user_id;
```

```
 name  |  total  
-------+---------
 John  |  100.00 
 John  |  200.00 
 John  |  300.00 
 User1 |  400.00 
 User1 |  500.00 
 User1 |  600.00 
 User2 |  700.00 
 User2 |  800.00 
 User2 |  900.00 
 User3 | 1000.00 
 User3 | 1100.00 
 User3 | 1200.00 
 User4 | 1300.00 
 User4 | 1400.00 
 User4 | 1500.00 
```

```sql
SELECT users.name, orders.total 
FROM users
JOIN orders
ON users.id = orders.user_id
WHERE users.name = 'John';
```

```
 name | total
------+--------
 John | 100.00
 John | 200.00
 John | 300.00
 ```

```sql
SELECT * 
FROM users --ESQUERDA
LEFT JOIN orders --DIREITA
ON users.id = orders.user_id;
```

```
 id | name  |       email       | id | user_id |  total
----+-------+-------------------+----+---------+---------
  1 | User1 | user1@example.com |  1 |       1 |  100.00
  1 | User1 | user1@example.com |  2 |       1 |  200.00
  1 | User1 | user1@example.com |  3 |       1 |  300.00
  2 | User2 | user2@example.com |  4 |       2 |  400.00
  2 | User2 | user2@example.com |  5 |       2 |  500.00
  2 | User2 | user2@example.com |  6 |       2 |  600.00
  3 | User3 | user3@example.com |  7 |       3 |  700.00
  3 | User3 | user3@example.com |  8 |       3 |  800.00
  3 | User3 | user3@example.com |  9 |       3 |  900.00
  4 | User4 | user4@example.com | 10 |       4 | 1000.00
  4 | User4 | user4@example.com | 11 |       4 | 1100.00
  4 | User4 | user4@example.com | 12 |       4 | 1200.00
  5 | User5 | user5@example.com | 13 |       5 | 1300.00
  5 | User5 | user5@example.com | 14 |       5 | 1400.00
  5 | User5 | user5@example.com | 15 |       5 | 1500.00
  6 | User6 | user6@example.com |    |         |
```

```sql
SELECT *
FROM users --ESQUERDA
RIGHT JOIN orders --DIREITA
ON users.id = orders.user_id;
```

```
 id | name  |       email       | id | user_id |  total
----+-------+-------------------+----+---------+---------
  1 | User1 | user1@example.com |  1 |       1 |  100.00
  1 | User1 | user1@example.com |  2 |       1 |  200.00
  1 | User1 | user1@example.com |  3 |       1 |  300.00
  2 | User2 | user2@example.com |  4 |       2 |  400.00
  2 | User2 | user2@example.com |  5 |       2 |  500.00
  2 | User2 | user2@example.com |  6 |       2 |  600.00
  3 | User3 | user3@example.com |  7 |       3 |  700.00
  3 | User3 | user3@example.com |  8 |       3 |  800.00
  3 | User3 | user3@example.com |  9 |       3 |  900.00
  4 | User4 | user4@example.com | 10 |       4 | 1000.00
  4 | User4 | user4@example.com | 11 |       4 | 1100.00
  4 | User4 | user4@example.com | 12 |       4 | 1200.00
  5 | User5 | user5@example.com | 13 |       5 | 1300.00
  5 | User5 | user5@example.com | 14 |       5 | 1400.00
  5 | User5 | user5@example.com | 15 |       5 | 1500.00
    |       |                   | 16 |         | 1600.00
    |       |                   | 17 |         | 1700.00
    |       |                   | 18 |         | 1800.00
```

```sql
SELECT * 
FROM users --ESQUERDA
FULL JOIN orders --DIREITA
ON users.id = orders.user_id;
```

```
 id | name  |       email       | id | user_id |  total
----+-------+-------------------+----+---------+---------
  1 | User1 | user1@example.com |  1 |       1 |  100.00
  1 | User1 | user1@example.com |  2 |       1 |  200.00
  1 | User1 | user1@example.com |  3 |       1 |  300.00
  2 | User2 | user2@example.com |  4 |       2 |  400.00
  2 | User2 | user2@example.com |  5 |       2 |  500.00
  2 | User2 | user2@example.com |  6 |       2 |  600.00
  3 | User3 | user3@example.com |  7 |       3 |  700.00
  3 | User3 | user3@example.com |  8 |       3 |  800.00
  3 | User3 | user3@example.com |  9 |       3 |  900.00
  4 | User4 | user4@example.com | 10 |       4 | 1000.00
  4 | User4 | user4@example.com | 11 |       4 | 1100.00
  4 | User4 | user4@example.com | 12 |       4 | 1200.00
  5 | User5 | user5@example.com | 13 |       5 | 1300.00
  5 | User5 | user5@example.com | 14 |       5 | 1400.00
  5 | User5 | user5@example.com | 15 |       5 | 1500.00
    |       |                   | 16 |         | 1600.00
    |       |                   | 17 |         | 1700.00
    |       |                   | 18 |         | 1800.00
  6 | User6 | user6@example.com |    |         |
```

```sql
SELECT *
FROM users
INNER JOIN orders
ON users.id = orders.user_id;
```

```
 id | name  |       email       | id | user_id |  total
----+-------+-------------------+----+---------+---------
  1 | User1 | user1@example.com |  1 |       1 |  100.00
  1 | User1 | user1@example.com |  2 |       1 |  200.00
  1 | User1 | user1@example.com |  3 |       1 |  300.00
  2 | User2 | user2@example.com |  4 |       2 |  400.00
  2 | User2 | user2@example.com |  5 |       2 |  500.00
  2 | User2 | user2@example.com |  6 |       2 |  600.00
  3 | User3 | user3@example.com |  7 |       3 |  700.00
  3 | User3 | user3@example.com |  8 |       3 |  800.00
  3 | User3 | user3@example.com |  9 |       3 |  900.00
  4 | User4 | user4@example.com | 10 |       4 | 1000.00
  4 | User4 | user4@example.com | 11 |       4 | 1100.00
  4 | User4 | user4@example.com | 12 |       4 | 1200.00
  5 | User5 | user5@example.com | 13 |       5 | 1300.00
  5 | User5 | user5@example.com | 14 |       5 | 1400.00
  5 | User5 | user5@example.com | 15 |       5 | 1500.00
```

```sql
SELECT u.name, o.total, s.name, s.registration
FROM users --ESQUERDA
JOIN orders --DIREITA
ON users.id = orders.user_id
FULL JOIN students
ON users.id = students.id;
```

```sql
SELECT u.name, o.total, s.name, s.registration
FROM users u --ESQUERDA
JOIN orders o --DIREITA
ON u.id = o.user_id
FULL JOIN students s --DIREITA
ON u.id = s.id;
```

```
 name  |  total  |    name    | registration
-------+---------+------------+--------------
 User1 |  100.00 | Student 1  | 2023-01-01
 User1 |  200.00 | Student 1  | 2023-01-01
 User1 |  300.00 | Student 1  | 2023-01-01
 User2 |  400.00 | Student 2  | 2023-01-02
 User2 |  500.00 | Student 2  | 2023-01-02
 User2 |  600.00 | Student 2  | 2023-01-02
 User3 |  700.00 | Student 3  | 2023-01-03
 User3 |  800.00 | Student 3  | 2023-01-03
 User3 |  900.00 | Student 3  | 2023-01-03
 User4 | 1000.00 | Student 4  | 2023-01-04
 User4 | 1100.00 | Student 4  | 2023-01-04
 User4 | 1200.00 | Student 4  | 2023-01-04
 User5 | 1300.00 | Student 5  | 2023-01-05
 User5 | 1400.00 | Student 5  | 2023-01-05
 User5 | 1500.00 | Student 5  | 2023-01-05
       |         | Student 20 | 2023-01-20
       |         | Student 25 | 2023-01-25
       |         | Student 26 | 2023-01-26
       |         | Student 27 | 2023-01-27
       |         | Student 11 | 2023-01-11
```

```sql
SELECT *
FROM users
LEFT JOIN orders
ON users.id = orders.user_id
WHERE orders.user_id IS NULL;
```

```
 id | name  |       email       | id | user_id | total
----+-------+-------------------+----+---------+-------
  6 | User6 | user6@example.com |    |         |
```

```sql
SELECT *
FROM users
RIGHT JOIN orders
ON users.id = orders.user_id
WHERE orders.user_id IS NULL;
```

```
 id | name | email | id | user_id |  total
----+------+-------+----+---------+---------
    |      |       | 18 |         | 1800.00
    |      |       | 17 |         | 1700.00
    |      |       | 16 |         | 1600.00
```
