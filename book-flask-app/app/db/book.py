import sqlite3
import os

if os.path.exists('book.db'):
    os.remove('book.db')

conn = sqlite3.connect('book.db')

conn.execute("CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, author TEXT NOT NULL)")
conn.execute("INSERT INTO book (name,author) VALUES ('The Great Gatsby', 'F. Scott Fitzgerald')")
conn.execute("INSERT INTO book (name,author) VALUES ('Moby Dick', 'Herman Melville')")
conn.commit()
conn.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def findAll():
    conn = sqlite3.connect('book.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def save(name,author):
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book (name,author) values (\'{}\', \'{}\')'.format(name,author))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id={}'.format(id))
    conn.commit()
    conn.close()

def update(id,name,author):
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute('UPDATE book SET name=\'{}\', author=\'{}\' WHERE id={}'.format(name,author,id))
    conn.commit()
    conn.close()