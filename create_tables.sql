CREATE TABLE employees(
    employee_id int PRIMARY KEY,
    first_name  varchar(100) NOT NULL,
    last_name   varchar(100) NOT NULL,
    title       varchar(100) NOT NULL,
    birth_date  date,
    notes       text NOT NULL
);

CREATE TABLE customers(
    customer_id  varchar(100) unique NOT NULL,
    company_name varchar(100)  NOT NULL,
    contact_name varchar(100)  NOT NULL
);

CREATE TABLE orders(
    order_id    int PRIMARY KEY,
    customer_id varchar(100) REFERENCES customers (customer_id),
    employee_id int  NOT NULL REFERENCES employees (employee_id),
    order_date  date,
    ship_city   varchar(100) NOT NULL
);

select * from empoyees
