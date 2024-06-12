import sqlite3
import os

# Создание директории для базы данных, если она еще не существует
if not os.path.exists('database'):
    os.makedirs('database')

# Подключение к базе данных и создание таблицы
conn = sqlite3.connect('database/database.db')
conn.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    age INTEGER
)
''')
conn.close()

print("Database initialized and table created.")
