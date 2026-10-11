# ============================================================
# DHP 303 - Database Handling Using Python (PR)
# B.C.A. Semester III - December 2025
#
# QUESTION 1:
# Implement the following operations on Employee table
# using SQLite module.
#
# Employee(emp_id, emp_name, contact_no, department_name, DOJ)
#
# A. Insert 10 records.
# B. Display all records using cursor.
#
# ============================================================
# CONCEPT:
# sqlite3       - Connects Python to SQLite database.
# CREATE TABLE  - Creates Employee table.
# executemany() - Inserts multiple records.
# SELECT *      - Retrieves all records.
# fetchall()    - Fetches all records.
# ============================================================

import sqlite3

# Connect to database
con = sqlite3.connect("Employee.db")
cur = con.cursor()

# Create Employee table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        emp_id INTEGER PRIMARY KEY,
        emp_name TEXT,
        contact_no TEXT,
        department_name TEXT,
        DOJ TEXT
    )
""")

con.commit()

print("Employee table created successfully!")

# Insert 10 records
data = [
    (101, "Amit", "9876543210", "Sales", "2023-01-15"),
    (102, "Neha", "9876543211", "HR", "2023-02-10"),
    (103, "Raj", "9876543212", "IT", "2023-03-05"),
    (104, "Priya", "9876543213", "Sales", "2023-04-12"),
    (105, "Karan", "9876543214", "Finance", "2023-05-20"),
    (106, "Riya", "9876543215", "Sales", "2023-06-18"),
    (107, "Jay", "9876543216", "IT", "2023-07-22"),
    (108, "Pooja", "9876543217", "HR", "2023-08-14"),
    (109, "Rahul", "9876543218", "Finance", "2023-09-09"),
    (110, "Meera", "9876543219", "Sales", "2023-10-25")
]

cur.executemany("""
    INSERT INTO Employee
    (emp_id, emp_name, contact_no, department_name, DOJ)
    VALUES (?, ?, ?, ?, ?)
""", data)

con.commit()

print("10 records inserted successfully!")

# Display all records using cursor
print("\nAll Employee Records:")

cur.execute("SELECT * FROM Employee")

for row in cur.fetchall():
    print(row)

# Close database connection
con.close()

# ============================================================
# EXPECTED OUTPUT:
#
# Employee table created successfully!
# 10 records inserted successfully!
#
# All Employee Records:
# (101, 'Amit', '9876543210', 'Sales', '2023-01-15')
# (102, 'Neha', '9876543211', 'HR', '2023-02-10')
# (103, 'Raj', '9876543212', 'IT', '2023-03-05')
# (104, 'Priya', '9876543213', 'Sales', '2023-04-12')
# (105, 'Karan', '9876543214', 'Finance', '2023-05-20')
# (106, 'Riya', '9876543215', 'Sales', '2023-06-18')
# (107, 'Jay', '9876543216', 'IT', '2023-07-22')
# (108, 'Pooja', '9876543217', 'HR', '2023-08-14')
# (109, 'Rahul', '9876543218', 'Finance', '2023-09-09')
# (110, 'Meera', '9876543219', 'Sales', '2023-10-25')
#
# ============================================================
# EXPLANATION:
#
# 1. connect() opens the Employee.db database.
# 2. CREATE TABLE creates the Employee table.
# 3. executemany() inserts 10 employee records.
# 4. commit() saves the inserted records.
# 5. SELECT * retrieves all employee records.
# 6. fetchall() returns all records for display.
#
# ============================================================
