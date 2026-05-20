import sqlite3
import os

DB_PATH = 'instance/books.db'

def get_db_connection():
    os.makedirs('instance', exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized")

def add_test_data():
    conn = get_db_connection()
    count = conn.execute('SELECT COUNT(*) FROM books').fetchone()[0]
    
    if count == 0:
        test_books = [
            ('Master and Margarita', 'Mikhail Bulgakov', 1967, 'A novel about the devil in Moscow', ''),
            ('Crime and Punishment', 'Fyodor Dostoevsky', 1866, 'A novel about morality and redemption', ''),
            ('1984', 'George Orwell', 1949, 'Dystopia about totalitarianism', ''),
        ]
        
        for book in test_books:
            conn.execute('''
                INSERT INTO books (title, author, year, description, image_url)
                VALUES (?, ?, ?, ?, ?)
            ''', book)
        
        conn.commit()
        print("Test data added")
    
    conn.close()

if __name__ == '__main__':
    init_db()
    add_test_data()
    print("Ready!")