import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT,
    salary REAL
)
''')
# Delete existing records
cursor.execute('DELETE FROM employees')

# Insert data
employees = [
    (1, "John Doe", 30, "HR", 50000),
    (2, "Jane Smith", 25, "Finance", 60000),
    (3, "Emily Johnson", 35, "IT", 75000),
    (4, "Michael Brown", 40, "Marketing", 55000),
    (5, "Jessica Davis", 28, "Sales", 45000),
    (6, "William Wilson", 32, "HR", 48000),
    (7, "Olivia Martinez", 29, "Finance", 67000),
    (8, "James Garcia", 31, "IT", 72000),
    (9, "Isabella Hernandez", 26, "Marketing", 53000),
    (10, "Alexander Lee", 38, "Sales", 62000)
]

cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?)', employees)

# Commit changes
conn.commit()

# Display all data
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()
