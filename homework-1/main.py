"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
from config import *

def fill_employees_data():
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='2162'
    )
    cur = conn.cursor()
    with open(employees_csv , encoding='windows-1251') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",(
                int(row['employee_id']), str(row["first_name"]), str(row["last_name"]),
                str(row["title"]), str(row["birth_date"]), str(row["notes"])))
        cur.execute("SELECT * FROM employees")
        conn.commit()
        cur.close()
        conn.close()

def fill_customers_data():
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='2162'
    )
    cur = conn.cursor()
    with open(customers_csv, encoding='windows-1251') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",(
                str(row['customer_id']), str(row["company_name"]), str(row["contact_name"])))
        cur.execute("SELECT * FROM customers")
        conn.commit()
        cur.close()
        conn.close()

def fill_orders_data():
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='2162'
    )
    cur = conn.cursor()
    with open(orders_csv, encoding='windows-1251') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s, %s, %s)",(
                int(row['order_id']), str(row["customer_id"]), int(row["employee_id"]),
                str(row["order_date"]), str(row["ship_city"]), int(row["employee_id"]),  str(row["customer_id"])))
        cur.execute("SELECT * FROM orders")
        conn.commit()
        cur.close()
        conn.close()


fill_employees_data()

fill_customers_data()

fill_orders_data()

