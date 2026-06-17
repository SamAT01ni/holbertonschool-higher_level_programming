-- Task 6 states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Now make the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
