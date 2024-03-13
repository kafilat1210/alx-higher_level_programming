-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table states with the columns id and name
-- The id column is unique, auto generated, not null, and the primary key
-- The name column is not null
-- If the table already exists, do nothing
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
