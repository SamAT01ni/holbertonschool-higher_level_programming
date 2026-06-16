-- Task 1, create user with all priveleges and password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- give all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
