-- Prepares a MySQL server for the project (development).
-- Creates the database hbnb_dev_db and the user hbnb_dev.

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Give all privileges on hbnb_dev_db only
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Give SELECT on performance_schema only
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
