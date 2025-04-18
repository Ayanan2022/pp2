import psycopg2
import csv

# Подключение
conn = psycopg2.connect(
    dbname="testdb",      # или "postgres"
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Создание таблицы
cur.execute("""
CREATE TABLE IF NOT EXISTS Phonebook (
    id SERIAL PRIMARY KEY,
    name TEXT
)
""")

# Вставка данных
cur.execute("INSERT INTO users (name) VALUES (%s)", ("Ayana",))

# Чтение данных
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
cur.close()
conn.close()
