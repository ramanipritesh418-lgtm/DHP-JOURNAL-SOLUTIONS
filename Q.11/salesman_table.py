# ============================================================
# PRACTICAL ASSIGNMENT - 2
# DATABASE HANDLING USING PYTHON
# ============================================================

"""
QUESTION:

Write a Python program to create a table and insert some
records in that table. Finally selects all rows from the
table and display the records.

Fields:
salesman_id,
name char(30),
city char(35),
commission decimal(7,2)
"""


# ============================================================
# STEP 1: Import sqlite3 module
# ============================================================

import sqlite3


# ============================================================
# STEP 2: Connect to SQLite Database
# ============================================================

con = sqlite3.connect("Salesman.db")


# ============================================================
# STEP 3: Create Cursor
# ============================================================

cursor = con.cursor()


# ============================================================
# STEP 4: Create Salesman Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Salesman (
    salesman_id INTEGER,
    name CHAR(30),
    city CHAR(35),
    commission DECIMAL(7,2)
)
""")


# ============================================================
# STEP 5: Insert Records
# ============================================================

data = [
    (5001, 'James Hoog', 'New York', 0.15),
    (5002, 'Nail Knite', 'Paris', 0.13),
    (5005, 'Pit Alex', 'London', 0.11),
    (5006, 'Mc Lyon', 'Paris', 0.14),
    (5007, 'Paul Adam', 'Rome', 0.13)
]

cursor.executemany("""
INSERT INTO Salesman
VALUES (?, ?, ?, ?)
""", data)


# ============================================================
# STEP 6: Commit Changes
# ============================================================

con.commit()


# ============================================================
# STEP 7: Display All Records
# ============================================================

print("Salesman Records:")

cursor.execute("SELECT * FROM Salesman")

records = cursor.fetchall()

for row in records:
    print(row)


# ============================================================
# STEP 8: Close Database Connection
# ============================================================

con.close()


# ============================================================
# OUTPUT
# ============================================================

# Salesman Records:
# (5001, 'James Hoog', 'New York', 0.15)
# (5002, 'Nail Knite', 'Paris', 0.13)
# (5005, 'Pit Alex', 'London', 0.11)
# (5006, 'Mc Lyon', 'Paris', 0.14)
# (5007, 'Paul Adam', 'Rome', 0.13)
