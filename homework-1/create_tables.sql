-- SQL-команды для создания таблиц

CREATE TABLE employees
(
    employees_id    int PRIMARY KEY,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    title varchar(100) NOT NULL,
    birth_date varchar(100) NOT NULL,
    notes varchar(555) NOT NULL
);

SELECT * FROM employees


CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name  varchar(100) NOT NULL
);

SELECT * FROM customers


CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(100) NOT NULL,
    employee_id int NOT NULL,
    order_date varchar(100) NOT NULL,
    ship_city varchar(100) NOT NULL,
    autor int REFERENCES employees(employees_id) NOT NULL,
	custom varchar(100) REFERENCES customers(customer_id) NOT NULL
);

SELECT * FROM orders
