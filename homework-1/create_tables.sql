-- SQL-команды для создания таблиц
CREATE TABLE employees
(employee_id VARCHAR(15) PRIMARY KEY NOT NULL,
 first_name VARCHAR(20) NOT NULL,
 last_name VARCHAR(30) NOT NULL,
 title VARCHAR(50) NOT NULL,
 birth_date DATE NOT NULL,
 notes TEXT
)

CREATE TABLE customers
(customer_id VARCHAR(15) PRIMARY KEY NOT NULL,
 company_name VARCHAR(50) NOT NULL,
 contact_name VARCHAR(100) NOT NULL
)

CREATE TABLE orders
(order_id INT PRIMARY KEY NOT NULL,
 customer_id VARCHAR(15) NOT NULL,
 employee_id VARCHAR(15) NOT NULL,
 order_date DATE,
 ship_city VARCHAR(20) NOT NULL,

 CONSTRAINT customer_id_fk FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
 CONSTRAINT employee_id_fk FOREIGN KEY (employee_id) REFERENCES employees(employee_id)

)
