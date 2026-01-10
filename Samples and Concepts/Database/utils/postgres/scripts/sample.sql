CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  last_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS orders (
  id SERIAL PRIMARY KEY,
  total DECIMAL,
  user_id INT REFERENCES users(id) ON DELETE SET NULL
  -- user_id INT REFERENCES users(id) ON DELETE SET NULL
  -- user_id INT REFERENCES users(id) ON DELETE CASCADE
  -- user_id INT REFERENCES users(id) ON DELETE RESTRICT
);

INSERT INTO users (id, name, last_name)
VALUES
  (0, 'Bruno', 'Lanconi'),
  (1, 'John', 'Doe'),
  (2, 'User1', 'example'),
  (3, 'User2', 'example'),
  (4, 'User3', 'example'),
  (5, 'User4', 'example'),
  (6, 'User5', 'example'),
  (7, 'User6', 'example')
;

INSERT INTO orders (user_id, total)
VALUES
  (1, 100.00),
  (1, 200.00),
  (1, 300.00),
  (2, 400.00),
  (2, 500.00),
  (2, 600.00),
  (3, 700.00),
  (3, 800.00),
  (3, 900.00),
  (4, 1000.00),
  (4, 1100.00),
  (4, 1200.00),
  (5, 1300.00),
  (5, 1400.00),
  (5, 1500.00),
  (null, 1600.00),
  (null, 1700.00),
  (null, 1800.00)
;