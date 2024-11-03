-- Insert users
INSERT INTO users (name, email) VALUES
('User1', 'user1@example.com'),
('User2', 'user2@example.com'),
('User3', 'user3@example.com'),
('User4', 'user4@example.com'),
('User5', 'user5@example.com'),
('User6', 'user6@example.com');

-- Insert orders for each user
INSERT INTO orders (user_id, total) VALUES
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
(null, 1800.00);