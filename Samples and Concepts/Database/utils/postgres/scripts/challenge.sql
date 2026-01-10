-- Insert orders for the newly added users
DO $$
  -- Declare variables to hold user IDs
  DECLARE
      user_x_id INT;
      user_y_id INT;
  -- Begin block to execute the insertion
  BEGIN
      -- Retrieve the IDs of the newly added users
      --- Get user IDs based on their emails and store them in variable user_x_id
      SELECT id INTO user_x_id FROM users WHERE email = 'userx@new.com';
      --- Get user IDs based on their emails and store them in variable user_y_id
      SELECT id INTO user_y_id FROM users WHERE email = 'usery@new.com';

      INSERT INTO orders (user_id, total)
      VALUES
        (user_x_id, 100),
        (user_y_id, 200)
      ;
END $$;

-- Verify the inserted data
SELECT users.name, users.email, orders.total
FROM users
JOIN orders
ON users.id = orders.user_id
WHERE users.email IN ('userx@new.com', 'usery@new.com');