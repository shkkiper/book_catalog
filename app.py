from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection, init_db

app = Flask(__name__)

init_db()

@app.route('/')
def index():
    """Показывает все книги в виде карточек"""
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/book/<int:id>')
def detail(id):
    """Показывает подробную информацию о книге"""
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if book is None:
        return "Книга не найдена", 404
    
    return render_template('detail.html', book=book)

@app.route('/admin')
def admin():
    """Страница управления с таблицей всех записей"""
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('admin.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    """Добавляет новую книгу"""
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    description = request.form['description']
    image_url = request.form.get('image_url', '')
    
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO books (title, author, year, description, image_url)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, author, year, description, image_url))
    conn.commit()
    conn.close()
    
    return redirect(url_for('admin'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    """Редактирует существующую книгу"""
    conn = get_db_connection()
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        description = request.form['description']
        image_url = request.form.get('image_url', '')
        
        conn.execute('''
            UPDATE books 
            SET title=?, author=?, year=?, description=?, image_url=?
            WHERE id=?
        ''', (title, author, year, description, image_url, id))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))
    
    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if book is None:
        return "Книга не найдена", 404
    
    return render_template('edit.html', book=book)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    """Удаляет книгу"""
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('admin'))

if __name__ == '__main__':
    print("=" * 50)
    print("BOOK CATALOG - START")
    print("=" * 50)
    print("Main page: http://127.0.0.1:5000")
    print("Admin panel: http://127.0.0.1:5000/admin")
    print("=" * 50)
    app.run(debug=True, host='127.0.0.1', port=5000)
