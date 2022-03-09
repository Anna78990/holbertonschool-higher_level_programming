-- Write a script that creates the MySQL server user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
USE hbtn_0d_2 GRANT SELECT TO user_0d_2;
