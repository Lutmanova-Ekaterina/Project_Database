import csv

import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='15973')
count = 0
try:
    with conn:
        with conn.cursor() as cur:
            with open('customers_data.csv') as customers:
                reader = csv.DictReader(customers)
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (row['customer_id'], row['company_name'], row['contact_name']))
            with open('employees_data.csv') as employees:
                reader = csv.DictReader(employees)
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (
                    row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes'], count))
                    count += 1
            with open('orders_dara.csv') as order:
                reader = csv.DictReader(order)
                for row in reader:
                    cur.execute("INSERT INTO orders VALUES(%S, %S, %S, %S, %S)", (
                    row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']))

finally:
    conn.close()
