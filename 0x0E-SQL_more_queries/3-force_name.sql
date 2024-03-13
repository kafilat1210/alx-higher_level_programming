-- Create the table force_name with the columns id and name
-- The name column cannot be null
-- If the table already exists, do nothing
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
