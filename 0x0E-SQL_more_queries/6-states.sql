-- creates hbtn_0d_usa database with a states table within
-- states table attributes
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);
