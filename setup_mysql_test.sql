-- Prepares a MySQL server for the project (testing).
-- Creates the database hbnb_test_db and the user hbnb_test.

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Give all privileges on hbnb_test_db only
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Give SELECT on performance_schema only
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
