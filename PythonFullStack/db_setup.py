import sqlite3

# Connect (creates app.db if not exists)
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

# Insert a user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "pass123"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "pass123"))
# Commit changes
conn.commit()

# Fetch and display all users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users in database:")
for row in rows:
    print(row)

conn.close()
