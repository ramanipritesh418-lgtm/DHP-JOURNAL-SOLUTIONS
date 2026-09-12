# ============================================================
# PRACTICAL ASSIGNMENT - 2
# DATABASE HANDLING USING PYTHON
# ============================================================

"""
QUESTION:

Write a Python program to insert values to a table
from user input.

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
# STEP 5: Take Values from User
# ============================================================

salesman_id = int(input("Enter Salesman ID: "))
name = input("Enter Name: ")
city = input("Enter City: ")
commission = float(input("Enter Commission: "))


# ============================================================
# STEP 6: Insert User Input into Table
# ============================================================

cursor.execute("""
INSERT INTO Salesman
VALUES (?, ?, ?, ?)
""", (salesman_id, name, city, commission))


# ============================================================
# STEP 7: Commit Changes
# ============================================================

con.commit()


# ============================================================
# STEP 8: Display Inserted Record
# ============================================================

print("\nRecord inserted successfully.")

cursor.execute("""
SELECT * FROM Salesman
WHERE salesman_id = ?
""", (salesman_id,))

record = cursor.fetchone()

print(record)


# ============================================================
# STEP 9: Close Database Connection
# ============================================================

con.close()


# ============================================================
# OUTPUT
# ============================================================

# Enter Salesman ID: 5008
# Enter Name: John
# Enter City: London
# Enter Commission: 0.12
#
# Record inserted successfully.
# (5008, 'John', 'London', 0.12)
