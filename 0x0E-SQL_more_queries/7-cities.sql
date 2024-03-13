-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table cities with the columns id, state_id, and name
-- The id column is unique, auto generated, not null, and the primary key
-- The state_id column is not null and a foreign key that references the states table
-- The name column is not null
-- If the table already exists, do nothing
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states (id)
);
