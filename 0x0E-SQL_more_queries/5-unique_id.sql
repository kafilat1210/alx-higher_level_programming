-- Create the table unique_id with the columns id and name
-- The id column has the default value 1 and the unique constraint
-- If the table already exists, do nothing
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
