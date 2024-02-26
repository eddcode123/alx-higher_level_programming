-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on a MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create a table in the created data base
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    state_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
