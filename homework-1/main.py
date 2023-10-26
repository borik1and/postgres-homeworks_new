import psycopg2
import csv

def open_csv_file(file):
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Пропускаем первую строку (заголовки)
        next(csv_reader, None)
        data = list(csv_reader)
    return data

employees = open_csv_file('north_data/employees_data.csv')
customers = open_csv_file('north_data/customers_data.csv')
orders = open_csv_file('north_data/orders_data.csv')

# Конфигурация базы данных
db_config = {
    'dbname': 'north',
    'user': 'postgres',
    'password': '1975',
    'host': 'localhost'
}

# Устанавливаем соединение с базой данных
conn = psycopg2.connect(**db_config)

try:
    # Создаем курсор
    cur = conn.cursor()

    # Вставляем данные в таблицу employees
    cur.executemany("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)", employees)

    # Вставляем данные в таблицу customers
    cur.executemany("INSERT INTO customers VALUES(%s, %s, %s)", customers)

    # Вставляем данные в таблицу orders
    cur.executemany("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)", orders)

    # Подтверждаем изменения в базе данных
    conn.commit()

except Exception as e:
    # В случае ошибки откатываем транзакцию
    conn.rollback()
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем курсор и соединение
    cur.close()
    conn.close()
