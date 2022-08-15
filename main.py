# CREATE TABLE salesperon(
# 	salesperson_id SERIAL PRIMARY KEY,
# 	sold_cars_name VARCHAR(50),
# 	sold_cars_id INTEGER,
# 	invoice_amount NUMERIC,
# 	invoice_id INTEGER
# );
#
# CREATE TABLE customer(
# 	customer_id SERIAL PRIMARY KEY,
# 	salesperson_id INTEGER,
# 	customer_car_name VARCHAR(50),
# 	customer_car_id INTEGER,
# 	invoice NUMERIC,
# 	FOREIGN KEY(salesperson_id) REFERENCES salesperson(salesperson_id)
# );
#
# ALTER TABLE salesperon
# RENAME TO salesperson;
#
# CREATE TABLE car_service(
# 	customer_id INTEGER,
# 	FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
# );
#
# SELECT *
# FROM customer;
#
# CREATE TABLE new_car(
# 	new_car_id SERIAL PRIMARY KEY,
# 	new_car_name VARCHAR(50),
# 	customer_id INTEGER,
# 	FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
# );
#
# CREATE TABLE used_car(
# 	used_car_id SERIAL PRIMARY KEY,
# 	used_car_name VARCHAR(50),
# 	customer_id INTEGER,
# 	FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
# );
#
# CREATE TABLE invoice(
# 	invoice_id SERIAL PRIMARY KEY,
# 	invoice_amount NUMERIC,
# 	customer_id INTEGER,
# 	FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
# );
#
#
# ALTER TABLE salesperson
# DROP COLUMN invoice_amount;
#
# ALTER TABLE salesperson
# DROP COLUMN invoice_id;
#
# ALTER TABLE customer
# DROP COLUMN invoice;
#
# ALTER TABLE car_service
# ADD COLUMN new_car_id INTEGER;
#
# ALTER TABLE car_service
# ADD COLUMN used_car_id INTEGER;
#
# ALTER TABLE car_service
# ADD FOREIGN KEY(new_car_id) REFERENCES new_car(new_car_id);
#
# ALTER TABLE car_service
# ADD FOREIGN KEY(used_car_id) REFERENCES used_car(used_car_id);
#
# ALTER TABLE car_service
# ADD COLUMN invoice_id INTEGER;
#
# ALTER TABLE car_service
# ADD FOREIGN KEY(invoice_id) REFERENCES invoice(invoice_id);
#
# ALTER TABLE car_service
# ADD COLUMN mechanics_id SERIAL PRIMARY KEY;
#
# SELECT *
# FROM new_car;
#
# INSERT INTO salesperson (salesperson_id, sold_cars_name, sold_cars_id)
# VALUES(1,'BMW', 1);
#
# SELECT *
# FROM salesperson;
#
# INSERT INTO customer(customer_id, salesperson_id, customer_car_name, customer_car_id)
# VALUES(1, 1, 'Ford', 1);
#
# SELECT *
# FROM customer;
#
# INSERT INTO new_car(new_car_id, new_car_name, customer_id)
# VALUES(1, 'Ford', 1);
#
# SELECT *
# FROM new_car;
#
# INSERT INTO invoice(invoice_id, invoice_amount, customer_id)
# VALUES(1, 10.500, 1);
#
# SELECT *
# FROM invoice;
#
# INSERT INTO car_service(customer_id, new_car_id, used_car_id, invoice_id, mechanics_id)
# VALUES(1, 1, NULL, 1, 1);
#
# SELECT *
# FROM car_service;
#
# SELECT customer.customer_id, customer.customer_car_name, invoice.invoice_amount
# FROM customer
# INNER JOIN invoice ON customer.customer_id = invoice.customer_id;
#
#
# INSERT INTO customer(customer_id, salesperson_id, customer_car_name, customer_car_id)
# VALUES(2, 2, 'BMW', 2);
# 
#
#
#

