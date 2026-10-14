# ============================================================
# DHP 303 - DATABASE HANDLING USING PYTHON
# FILE: 02_Company.py
#
# QUESTION:
# Create company.db and Employee table with:
# EmpID, EmpName, Department, Salary, City.
# Insert at least 8 employee records.
#
# 1. Create database and table, and insert records.
# 2. Display IT employees earning more than 40000.
# 3. Display department-wise employee count and average salary
#    using GROUP BY and HAVING.
# 4. Display employees from Bharuch, Surat or Mumbai using IN
#    and sort by salary in descending order.
#
# CONCEPT:
# SQLite, CREATE TABLE, INSERT, WHERE, GROUP BY, HAVING, IN,
# ORDER BY and aggregate functions.
# ============================================================

import sqlite3

# Connect to database
con = sqlite3.connect("company.db")
cur = con.cursor()

# 1. Create Employee table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        EmpID INTEGER PRIMARY KEY,
        EmpName TEXT,
        Department TEXT,
        Salary REAL,
        City TEXT
    )
""")

# Clear old records to avoid duplicate IDs when rerunning
cur.execute("DELETE FROM Employee")

# Insert 8 employee records
employees = [
    (1, "Amit", "IT", 55000, "Surat"),
    (2, "Neha", "HR", 35000, "Bharuch"),
    (3, "Rahul", "IT", 48000, "Mumbai"),
    (4, "Priya", "Sales", 42000, "Surat"),
    (5, "Karan", "IT", 38000, "Bharuch"),
    (6, "Anjali", "HR", 45000, "Mumbai"),
    (7, "Meera", "Sales", 30000, "Navsari"),
    (8, "Arjun", "IT", 62000, "Surat")
]

cur.executemany("""
    INSERT INTO Employee
    (EmpID, EmpName, Department, Salary, City)
    VALUES (?, ?, ?, ?, ?)
""", employees)

# Save changes
con.commit()
print("Database and Employee table created successfully.")
print("8 employee records inserted successfully.")

cur.execute("select*from Employee")
for row in cur.fetchall():
    print(row)

# 2. Employees earning more than 40000 in IT department
print("\n2. IT Employees With Salary Greater Than 40000:")

cur.execute("""
    SELECT * FROM Employee
    WHERE Salary > 40000 AND Department = 'IT'
""")

for row in cur.fetchall():
    print(row)

# 3. Department-wise employee count and average salary
# HAVING filters grouped departments whose average salary > 40000
print("\n3. Department-wise Count and Average Salary:")

cur.execute("""
    SELECT Department,
           COUNT(*) AS TotalEmployees,
           AVG(Salary) AS AverageSalary
    FROM Employee
    GROUP BY Department
    HAVING AVG(Salary) > 40000
""")

for row in cur.fetchall():
    print(row)

# 4. Employees from Bharuch, Surat or Mumbai
# Sort salary from highest to lowest
print("\n4. Employees From Bharuch, Surat or Mumbai:")

cur.execute("""
    SELECT * FROM Employee
    WHERE City IN ('Bharuch', 'Surat', 'Mumbai')
    ORDER BY Salary DESC
""")

for row in cur.fetchall():
    print(row)

# Close connection
con.close()


# Database and Employee table created successfully.
# 8 employee records inserted successfully.
# (1, 'Amit', 'IT', 55000.0, 'Surat')
# (2, 'Neha', 'HR', 35000.0, 'Bharuch')
# (3, 'Rahul', 'IT', 48000.0, 'Mumbai')
# (4, 'Priya', 'Sales', 42000.0, 'Surat')
# (5, 'Karan', 'IT', 38000.0, 'Bharuch')
# (6, 'Anjali', 'HR', 45000.0, 'Mumbai')
# (7, 'Meera', 'Sales', 30000.0, 'Navsari')
# (8, 'Arjun', 'IT', 62000.0, 'Surat')

# 2. IT Employees With Salary Greater Than 40000:
# (1, 'Amit', 'IT', 55000.0, 'Surat')
# (3, 'Rahul', 'IT', 48000.0, 'Mumbai')
# (8, 'Arjun', 'IT', 62000.0, 'Surat')

# 3. Department-wise Count and Average Salary:
# ('IT', 4, 50750.0)

# 4. Employees From Bharuch, Surat or Mumbai:
# (8, 'Arjun', 'IT', 62000.0, 'Surat')
# (1, 'Amit', 'IT', 55000.0, 'Surat')
# (3, 'Rahul', 'IT', 48000.0, 'Mumbai')
# (6, 'Anjali', 'HR', 45000.0, 'Mumbai')
# (4, 'Priya', 'Sales', 42000.0, 'Surat')
# (5, 'Karan', 'IT', 38000.0, 'Bharuch')
# (2, 'Neha', 'HR', 35000.0, 'Bharuch')
