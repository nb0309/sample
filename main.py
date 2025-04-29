import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Insert data
name = "John Doe"
email = "john.doe@example.com"

try:
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    print("Data inserted successfully.")
except sqlite3.IntegrityError:
    print("Email already exists in the database.")

# Query to confirm insertion
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
