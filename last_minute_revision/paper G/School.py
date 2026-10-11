# ============================================================
# DHP 303 - Database Handling Using Python (PR)
# B.C.A. Semester III - December 2025
#
# QUESTION 2 (10 Marks):
#
# Create table School(StudentID, Name, Class, Marks, Age)
# and add at least 7 records.
#
# 1. Export table data into a CSV file named school.csv.
# 2. Retrieve all students whose Marks are greater than 80.
# 3. Delete the table School.
# 4. Import CSV data into a new table School_New.
#
# ============================================================
# CONCEPT / REQUIREMENTS:
#
# 1. sqlite3  - To create database and perform SQL operations.
# 2. csv      - To export and import CSV data.
# 3. INSERT   - To insert student records.
# 4. SELECT   - To retrieve students with Marks > 80.
# 5. DROP     - To delete the School table.
#
# ============================================================

import sqlite3
import csv

# Connect to database
con = sqlite3.connect("School.db")
cur = con.cursor()

# ------------------------------------------------------------
# Step 1: Create School table
# ------------------------------------------------------------

cur.execute("""
    CREATE TABLE IF NOT EXISTS School (
        StudentID INTEGER PRIMARY KEY,
        Name TEXT,
        Class TEXT,
        Marks REAL,
        Age INTEGER
    )
""")

con.commit()

print("School table created successfully!")

# ------------------------------------------------------------
# Step 2: Insert at least 7 records
# ------------------------------------------------------------

students = [
    (1, "Amit", "BCA", 85, 19),
    (2, "Neha", "BCA", 92, 20),
    (3, "Raj", "BCA", 76, 19),
    (4, "Priya", "BCA", 88, 20),
    (5, "Karan", "BCA", 67, 19),
    (6, "Riya", "BCA", 95, 20),
    (7, "Jay", "BCA", 80, 19)
]

cur.executemany("""
    INSERT INTO School
    (StudentID, Name, Class, Marks, Age)
    VALUES (?, ?, ?, ?, ?)
""", students)

con.commit()

print("7 student records inserted successfully!")

# ------------------------------------------------------------
# Step 3: Export table data into school.csv
# ------------------------------------------------------------

cur.execute("SELECT * FROM School")
rows = cur.fetchall()

with open("school.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["StudentID", "Name", "Class", "Marks", "Age"])

    # Write student records
    writer.writerows(rows)

print("Data exported to school.csv successfully!")

# ------------------------------------------------------------
# Step 4: Display students whose Marks are greater than 80
# ------------------------------------------------------------

print("\nStudents whose Marks are greater than 80:")

cur.execute("SELECT * FROM School WHERE Marks > 80")

for row in cur.fetchall():
    print(row)

# ------------------------------------------------------------
# Step 5: Delete the School table
# ------------------------------------------------------------

cur.execute("DROP TABLE School")
con.commit()

print("\nSchool table deleted successfully!")

# ------------------------------------------------------------
# Step 6: Create a new table School_New
# ------------------------------------------------------------

cur.execute("""
    CREATE TABLE IF NOT EXISTS School_New (
        StudentID INTEGER PRIMARY KEY,
        Name TEXT,
        Class TEXT,
        Marks REAL,
        Age INTEGER
    )
""")

# Clear old records before importing
cur.execute("DELETE FROM School_New")

con.commit()

# ------------------------------------------------------------
# Step 7: Import data from school.csv into School_New
# ------------------------------------------------------------

with open("school.csv", "r", newline="") as file:
    reader = csv.reader(file)

    # Skip the heading row
    next(reader)

    # Insert CSV records into School_New
    cur.executemany("""
        INSERT INTO School_New
        (StudentID, Name, Class, Marks, Age)
        VALUES (?, ?, ?, ?, ?)
    """, reader)

con.commit()

print("\nData imported into School_New successfully!")

# ------------------------------------------------------------
# Step 8: Display imported records
# ------------------------------------------------------------

print("\nRecords in School_New:")

cur.execute("SELECT * FROM School_New")

for row in cur.fetchall():
    print(row)

# ------------------------------------------------------------
# EXPECTED OUTPUT:
#
# School table created successfully!
# 7 student records inserted successfully!
# Data exported to school.csv successfully!
#
# Students whose Marks are greater than 80:
# (1, 'Amit', 'BCA', 85.0, 19)
# (2, 'Neha', 'BCA', 92.0, 20)
# (4, 'Priya', 'BCA', 88.0, 20)
# (6, 'Riya', 'BCA', 95.0, 20)
#
# School table deleted successfully!
# Data imported into School_New successfully!
#
# Records in School_New:
# (1, 'Amit', 'BCA', 85.0, 19)
# (2, 'Neha', 'BCA', 92.0, 20)
# (3, 'Raj', 'BCA', 76.0, 19)
# (4, 'Priya', 'BCA', 88.0, 20)
# (5, 'Karan', 'BCA', 67.0, 19)
# (6, 'Riya', 'BCA', 95.0, 20)
# (7, 'Jay', 'BCA', 80.0, 19)
#
# Note: REAL values may display with decimal points.
#
# ------------------------------------------------------------
# EXPLANATION:
#
# 1. CREATE TABLE creates the School table.
# 2. executemany() inserts 7 student records.
# 3. csv.writer() exports data to school.csv.
# 4. WHERE Marks > 80 retrieves students scoring above 80.
# 5. DROP TABLE deletes the original School table.
# 6. csv.reader() reads the CSV file.
# 7. School_New stores the imported student records.
#
# ============================================================

con.close()
