# ============================================================
# PRACTICAL ASSIGNMENT - 4
# DATABASE HANDLING USING PYTHON
# ============================================================

"""
QUESTION:

Create following table with appropriate constraints in
College Database:

Employee (E_ID, Name, Dob, Designation, Salary)

a) Dump Employee table structure and data in Emp.csv file.
b) Dump whole Database named College in Emp1.csv file.
"""


# ============================================================
# STEP 1: IMPORT REQUIRED MODULES
# ============================================================

# sqlite3 is used to create and work with SQLite database.
# csv is used to create and write CSV files.

import sqlite3
import csv


# ============================================================
# STEP 2: CREATE / CONNECT COLLEGE DATABASE
# ============================================================

# This creates College.db if it does not exist.
# If the database already exists, it connects to it.

con = sqlite3.connect("College.db")


# ============================================================
# STEP 3: CREATE CURSOR
# ============================================================

# Cursor is used to execute SQL commands.

cur = con.cursor()


# ============================================================
# STEP 4: CREATE EMPLOYEE TABLE
# ============================================================

# Employee table contains:
# E_ID        -> Employee ID
# Name        -> Employee Name
# Dob         -> Date of Birth
# Designation -> Job Designation
# Salary      -> Employee Salary
#
# E_ID is PRIMARY KEY, so every employee must have
# a unique ID.

cur.execute("""
CREATE TABLE IF NOT EXISTS Employee(
    E_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Dob TEXT,
    Designation TEXT,
    Salary REAL
)
""")


# ============================================================
# STEP 5: INSERT 10 EMPLOYEE RECORDS
# ============================================================

# The following records are inserted into Employee table.

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

# executemany() inserts multiple records at once.

cur.executemany(
    "INSERT INTO Employee VALUES (?, ?, ?, ?, ?)",
    data
)

# Save all changes permanently in the database.

con.commit()


# ============================================================
# STEP 6: DISPLAY EMPLOYEE RECORDS
# ============================================================

# SELECT * retrieves all records from Employee table.

print("Employee Records:")

cur.execute("SELECT * FROM Employee")

# fetchall() gets all records.

rows = cur.fetchall()

# Display each record.

for row in rows:
    print(row)


# ============================================================
# PART (A)
# DUMP EMPLOYEE TABLE DATA INTO Emp.csv
# ============================================================

# Open Emp.csv in write mode.
# newline="" prevents blank lines in CSV file.

with open("Emp.csv", "w", newline="") as file:

    # Create CSV writer object.

    writer = csv.writer(file)

    # Write Employee table column names.

    writer.writerow([
        "E_ID",
        "Name",
        "Dob",
        "Designation",
        "Salary"
    ])

    # Write all Employee records.

    writer.writerows(rows)


# Display confirmation message.

print("\nEmployee data dumped into Emp.csv")


# ============================================================
# PART (B)
# DUMP WHOLE COLLEGE DATABASE INTO Emp1.csv
# ============================================================

# Get all table names from College database.

cur.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

tables = cur.fetchall()


# Open Emp1.csv in write mode.

with open("Emp1.csv", "w", newline="") as file:

    # Create CSV writer object.

    writer = csv.writer(file)

    # Process every table in the College database.

    for table in tables:

        # Get table name.

        table_name = table[0]

        # Select all records from the table.

        cur.execute("SELECT * FROM " + table_name)

        rows = cur.fetchall()

        # Write table name into Emp1.csv.

        writer.writerow([table_name])

        # Write table records into Emp1.csv.

        writer.writerows(rows)


# Display confirmation message.

print("Whole College database dumped into Emp1.csv")


# ============================================================
# STEP 7: CLOSE DATABASE CONNECTION
# ============================================================

# Close the SQLite database connection.

con.close()


# ============================================================
# EXPECTED OUTPUT
# ============================================================

"""
Employee Records:
(1, 'Amit', '2000-05-10', 'Manager', 50000.0)
(2, 'Rahul', '1998-08-15', 'Developer', 45000.0)
(3, 'Neha', '2001-02-20', 'Designer', 40000.0)
(4, 'Ravi', '1999-11-05', 'Accountant', 42000.0)
(5, 'Pooja', '2002-07-18', 'HR', 38000.0)
(6, 'Kiran', '1997-03-25', 'Team Lead', 55000.0)
(7, 'Priya', '2000-09-12', 'Tester', 35000.0)
(8, 'Jay', '1998-06-30', 'Developer', 46000.0)
(9, 'Riya', '2001-01-08', 'Designer', 41000.0)
(10, 'Vijay', '1999-12-22', 'Manager', 52000.0)

Employee data dumped into Emp.csv
Whole College database dumped into Emp1.csv
"""


# ============================================================
# FILES CREATED
# ============================================================

"""
After running this program, the following files will be created:

1. College.db
   -> SQLite database file

2. Emp.csv
   -> Contains Employee table column names and data

3. Emp1.csv
   -> Contains data of all tables in College database
"""
