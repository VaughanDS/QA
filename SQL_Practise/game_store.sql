DROP DATABASE IF EXISTS game_store;
CREATE DATABASE game_store;
USE game_store;

#Product
CREATE TABLE games(
game_id BIGINT AUTO_INCREMENT NOT NULL,
game_name varchar(100) NOT NULL,
game_description varchar(500),
game_console varchar(50),
game_price decimal(5,2) NOT NULL,
game_stock int NOT NULL,
PRIMARY KEY (game_id)
);

#Customer
CREATE TABLE customers(
customer_id BIGINT AUTO_INCREMENT NOT NULL,
first_name varchar(100) NOT NULL,
last_name varchar(100) NOT NULL,
email_address varchar(100) UNIQUE,
contact_number BIGINT UNIQUE,
PRIMARY KEY (customer_id)
);

#Order
CREATE TABLE orders(
order_id BIGINT AUTO_INCREMENT NOT NULL,
fk_game_id BIGINT NOT NULL,
fk_customer_id BIGINT NOT NULL,
order_date_placed DATE NOT NULL,
order_quantity int NOT NULL,
PRIMARY KEY (order_id),
FOREIGN KEY (fk_game_id) REFERENCES games (game_id),
FOREIGN KEY (fk_customer_id) REFERENCES customers (customer_id)
);

