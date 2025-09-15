import sqlite3
conn = sqlite3.connect('app.db')
cursor = conn.cursor()
# Create table
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
# Insert user
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user1', 'pass123'))
conn.commit()
conn.close()
