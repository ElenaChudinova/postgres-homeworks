import os
import psycopg2
import csv


"""Скрипт для заполнения данными таблиц в БД Postgres."""
con = psycopg2.connect(host='localhost', database='north', user='postgres', password='0000')

path = os.path.join(os.path.dirname(__file__), "north_data/employees_data.csv")
try:
    with con:
        with con.cursor() as cur:
            with open(path, 'r', encoding='UTF-8') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    employee_id = i['employee_id'],
                    first_name = i['first_name'],
                    last_name = i['last_name'],
                    title = i['title'],
                    birth_date = i['birth_date'],
                    notes = i['notes']
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (
                            employee_id,
                            first_name,
                            last_name,
                            title,
                            birth_date,
                            notes))
                    cur.execute("SELECT * FROM employees")

                    datas = cur.fetchall()
                    for data in datas:
                        print(data)

finally:
    con.close()

path = os.path.join(os.path.dirname(__file__), "north_data/customers_data.csv")
try:
    with con:
        with con.cursor() as cur:
            with open(path, 'r', encoding='UTF-8') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    customer_id = i['customer_id'],
                    company_name = i['company_name'],
                    contact_name = i['contact_name'],
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (
                            customer_id,
                            company_name,
                            contact_name,
                            ))
                    cur.execute("SELECT * FROM customers")

                    datas = cur.fetchall()
                    for data in datas:
                        print(data)

finally:
    con.close()


path = os.path.join(os.path.dirname(__file__), "north_data/orders_data.csv")
try:
    with con:
        with con.cursor() as cur:
            with open(path, 'r', encoding='UTF-8') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    order_id = i['order_id'],
                    customer_id = i['customer_id'],
                    employee_id = i['employee_id'],
                    order_date = i['order_date'],
                    ship_city = i['ship_city']
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (
                            order_id,
                            customer_id,
                            employee_id,
                            order_date,
                            ship_city,
                            ))
                    cur.execute("SELECT * FROM orders")

                    datas = cur.fetchall()
                    for data in datas:
                        print(data)

finally:
    con.close()





