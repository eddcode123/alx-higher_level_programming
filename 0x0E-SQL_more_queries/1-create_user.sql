-- Script creates a new user and assigns all privileges to user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- assign all privileges to user
GRANT *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- apply the changes immediately.
FLUSH PRIVILEGES;
