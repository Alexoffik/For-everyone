from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Маршрут для главной страницы
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Маршрут для обработки формы
@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    age = request.form['age']

    conn = get_db_connection()
    conn.execute('INSERT INTO users (first_name, last_name, gender, age) VALUES (?, ?, ?, ?)',
                 (first_name, last_name, gender, age))
    conn.commit()
    conn.close()

    return redirect('/')

# Маршрут для очистки базы данных
@app.route('/clear', methods=['POST'])
def clear():
    conn = get_db_connection()
    conn.execute('DELETE FROM users')
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
