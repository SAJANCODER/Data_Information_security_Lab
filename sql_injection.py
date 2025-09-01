import sqlite3

# Create a local SQLite database (file or in-memory)
conn = sqlite3.connect(":memory:")  # in-memory, disappears after program ends
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE users(username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Unsafe query (simulated SQL injection vulnerability)
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
print("Simulated Query:", query)

cursor.execute(query)
if cursor.fetchall():
    print("Login successful (simulated)")
else:
    print("Login failed (simulated)")
