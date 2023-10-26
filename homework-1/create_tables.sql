-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id serial PRIMARY KEY, -- Используется 'serial' для автоматического увеличения значения
	first_name varchar(20) NOT NULL,
	last_name varchar(40) NOT NULL,
	title text,
	birth_date DATE,
	notes text
);

CREATE TABLE customers
(
	customer_id CHAR(5) PRIMARY KEY,
	company_name varchar(60),
	contact_name varchar(70)
);

CREATE TABLE orders
(
	order_id serial PRIMARY KEY, -- Используется 'serial' для автоматического увеличения значения
	customer_id CHAR(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date DATE,
	ship_city varchar(30)
);
