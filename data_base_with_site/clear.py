from flask import Flask, redirect

app = Flask(__name__)

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
