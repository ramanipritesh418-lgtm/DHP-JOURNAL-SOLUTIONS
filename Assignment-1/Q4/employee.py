# ============================================================
# PRACTICAL ASSIGNMENT - 4
# ============================================================

# Create following table with appropriate constraints in
# College Database:
#
# Employee (E_ID, Name, Dob, Designation, Salary)
#
# a) Dump Employee table structure and data in Emp.csv file.
# b) Dump whole Database named College in Emp1.csv file.


# ============================================================
# Import Required Modules
# ============================================================

import sqlite3
import csv


# ============================================================
# Create / Connect College Database
# ============================================================

con = sqlite3.connect("College.db")


# ============================================================
# Create Cursor
# ============================================================

cursor = con.cursor()


# ============================================================
# Create Employee Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee(
    E_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Dob TEXT,
    Designation TEXT,
    Salary REAL
)
""")


# ============================================================
# Insert Records into Employee Table
# ============================================================

data = [
    (1, 'Amit', '2000-05-10', 'Manager', 50000),
    (2, 'Rahul', '1998-08-15', 'Developer', 45000),
    (3, 'Neha', '2001-02-20', 'Designer', 40000),
    (4, 'Ravi', '1999-11-05', 'Accountant', 42000),
    (5, 'Pooja', '2002-07-18', 'HR', 38000),
    (6, 'Kiran', '1997-03-25', 'Team Lead', 55000),
    (7, 'Priya', '2000-09-12', 'Tester', 35000),
    (8, 'Jay', '1998-06-30', 'Developer', 46000),
    (9, 'Riya', '2001-01-08', 'Designer', 41000),
    (10, 'Vijay', '1999-12-22', 'Manager', 52000)
]

cursor.executemany(
    "INSERT INTO Employee VALUES (?, ?, ?, ?, ?)",
    data
)

con.commit()


# ============================================================
# Display Employee Records
# ============================================================

cursor.execute("SELECT * FROM Employee")

records = cursor.fetchall()

for row in records:
    print(row)


# ============================================================
# PART (A)
# Dump Employee Table Structure and Data into Emp.csv
# ============================================================

# Get Employee Table Data
cursor.execute("SELECT * FROM Employee")
records = cursor.fetchall()


# Get Employee Table Structure
cursor.execute("PRAGMA table_info(Employee)")
structure = cursor.fetchall()


# Write Structure and Data into Emp.csv
with open("Emp.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Employee Table Structure"])

    writer.writerow(
        ["E_ID", "Name", "Dob", "Designation", "Salary"]
    )

    writer.writerows(structure)

    writer.writerow(["Employee Table Data"])

    writer.writerows(records)


# ============================================================
# PART (B)
# Dump Whole College Database into Emp1.csv
# ============================================================

# Get All Table Names
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table'
""")

tables = cursor.fetchall()


# Write Database Data into Emp1.csv
with open("Emp1.csv", "w", newline="") as file:

    writer = csv.writer(file)

    for table in tables:

        table_name = table[0]

        cursor.execute(f"SELECT * FROM {table_name}")

        rows = cursor.fetchall()

        writer.writerow([table_name])

        writer.writerows(rows)


# ============================================================
# Close Database Connection
# ============================================================

con.close()
