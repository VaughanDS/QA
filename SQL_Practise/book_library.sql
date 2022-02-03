CREATE DATABASE Book_Library;
USE Book_Library;
	CREATE TABLE books(
		book_name varchar(40) NOT NULL,
        book_author varchar(40) NOT NULL,
        book_ref_id int NOT NULL,
        PRIMARY KEY (book_ref_id)
        );
	CREATE TABLE customers(
		customer_name varchar(40) NOT NULL,
        customer_email varchar(60) NOT NULL,
        customer_id int NOT NULL,
        PRIMARY KEY (customer_id)
        );
	CREATE TABLE booking(
    order_id INT NOT NULL,
    book_ref_id INT NOT NULL,
    customer_id INT NOT NULL,
    date_placed DATE NOT NULL,
    date_due DATE NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (book_ref_id)
        REFERENCES books (book_ref_id),
    FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id)
);
