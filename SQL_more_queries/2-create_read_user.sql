-- task2 creates database and user with select privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- now make user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant select
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
