# ============================================================
# DHP 303 - PAPER H
# FILE: 01_School.py
#
# QUESTION:
# Create SCHOOL table with:
# student_id, student_name, address, b_date, Class
#
# A. Insert 10 records.
# B. Display students whose name starts with 'A'.
# C. Display names and addresses of students in Class 10.
# D. Display students in ascending order of date of birth.
#
# CONCEPT:
# SQLite database, CREATE TABLE, INSERT, LIKE, WHERE, ORDER BY
# ============================================================

import sqlite3

# Connect to database
con = sqlite3.connect("School.db")
cur = con.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS SCHOOL(
        student_id INTEGER PRIMARY KEY,
        student_name TEXT,
        address TEXT,
        b_date TEXT,
        Class INTEGER
    )
""")

# Insert 10 records
# Delete old records to avoid duplicate IDs when running again
cur.execute("DELETE FROM SCHOOL")

data = [
    (1, "Amit", "Surat", "2007-05-12", 10),
    (2, "Anjali", "Navsari", "2006-11-20", 10),
    (3, "Rahul", "Bardoli", "2007-02-15", 9),
    (4, "Priya", "Surat", "2006-08-10", 10),
    (5, "Arjun", "Vapi", "2007-09-25", 12),
    (6, "Neha", "Bharuch", "2006-04-18", 9),
    (7, "Ayesha", "Surat", "2007-01-05", 10),
    (8, "Karan", "Navsari", "2006-12-30", 12),
    (9, "Bhavik", "Bardoli", "2007-07-22", 10),
    (10, "Meera", "Vapi", "2006-03-14", 9)
]

cur.executemany("""
    INSERT INTO SCHOOL
    (student_id, student_name, address, b_date, Class)
    VALUES (?, ?, ?, ?, ?)
""", data)

con.commit()
print("10 records inserted successfully.")


print("All records:")
cur.execute("Select*from SCHOOL")
for row in cur.fetchall():
    print(row)

# B. Display students whose name starts with A
print("\nStudents whose name starts with A:")
cur.execute("""
    SELECT * FROM SCHOOL
    WHERE student_name LIKE 'A%'
""")

for row in cur.fetchall():
    print(row)

# C. Display names and addresses of students in Class 10
print("\nStudents belonging to Class 10:")
cur.execute("""
    SELECT student_name, address FROM SCHOOL
    WHERE Class = 10
""")

for row in cur.fetchall():
    print(row)

# D. Display all students in ascending order of date of birth
print("\nStudents in ascending order of date of birth:")
cur.execute("""
    SELECT * FROM SCHOOL
    ORDER BY b_date ASC
""")

for row in cur.fetchall():
    print(row)

con.close()

# 10 records inserted successfully.
# All records:
# (1, 'Amit', 'Surat', '2007-05-12', 10, None)
# (2, 'Anjali', 'Navsari', '2006-11-20', 10, None)
# (3, 'Rahul', 'Bardoli', '2007-02-15', 9, None)
# (4, 'Priya', 'Surat', '2006-08-10', 10, None)
# (5, 'Arjun', 'Vapi', '2007-09-25', 12, None)
# (6, 'Neha', 'Bharuch', '2006-04-18', 9, None)
# (7, 'Ayesha', 'Surat', '2007-01-05', 10, None)
# (8, 'Karan', 'Navsari', '2006-12-30', 12, None)
# (9, 'Bhavik', 'Bardoli', '2007-07-22', 10, None)
# (10, 'Meera', 'Vapi', '2006-03-14', 9, None)

# Students whose name starts with A:
# (1, 'Amit', 'Surat', '2007-05-12', 10, None)
# (2, 'Anjali', 'Navsari', '2006-11-20', 10, None)
# (5, 'Arjun', 'Vapi', '2007-09-25', 12, None)
# (7, 'Ayesha', 'Surat', '2007-01-05', 10, None)

# Students belonging to Class 10:
# ('Amit', 'Surat')
# ('Anjali', 'Navsari')
# ('Priya', 'Surat')
# ('Ayesha', 'Surat')
# ('Bhavik', 'Bardoli')

# Students in ascending order of date of birth:
# (10, 'Meera', 'Vapi', '2006-03-14', 9, None)
# (6, 'Neha', 'Bharuch', '2006-04-18', 9, None)
# (4, 'Priya', 'Surat', '2006-08-10', 10, None)
# (2, 'Anjali', 'Navsari', '2006-11-20', 10, None)
# (8, 'Karan', 'Navsari', '2006-12-30', 12, None)
# (7, 'Ayesha', 'Surat', '2007-01-05', 10, None)
# (3, 'Rahul', 'Bardoli', '2007-02-15', 9, None)
# (1, 'Amit', 'Surat', '2007-05-12', 10, None)
# (9, 'Bhavik', 'Bardoli', '2007-07-22', 10, None)
# (5, 'Arjun', 'Vapi', '2007-09-25', 12, None)

