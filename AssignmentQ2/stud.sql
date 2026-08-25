# ============================================================
# PRACTICAL ASSIGNMENT - 2
# DATABASE HANDLING USING PYTHON
# ============================================================

"""
QUESTION:

Write a Python script to perform the following operations on
Student(Rollno, Name, Sub1, Sub2, Sub3, Total) table:

1) Insert at least 5 to 10 records.
2) Update a specific record value.
3) Delete a specific record.
4) Display student details who got highest total marks.
"""


# ============================================================
# STEP 1: Import sqlite3 module
# ============================================================

import sqlite3


# ============================================================
# STEP 2: Create / Connect SQLite Database
# Student.db will be created automatically if it does not exist.
# ============================================================

con = sqlite3.connect("Student.db")


# ============================================================
# STEP 3: Create Cursor
# ============================================================

cursor = con.cursor()


# ============================================================
# STEP 4: Create Student Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    Rollno INTEGER PRIMARY KEY,
    Name TEXT,
    Sub1 INTEGER,
    Sub2 INTEGER,
    Sub3 INTEGER,
    Total INTEGER
)
""")


# ============================================================
# STEP 5: Insert 5 Student Records
# ============================================================

data = [
    (1, 'Amit', 80, 75, 85, 240),
    (2, 'Rahul', 70, 65, 75, 210),
    (3, 'Neha', 90, 85, 95, 270),
    (4, 'Ravi', 60, 70, 65, 195),
    (5, 'Pooja', 85, 90, 80, 255)
]

cursor.executemany(
    "INSERT INTO student VALUES (?, ?, ?, ?, ?, ?)",
    data
)

con.commit()


# ============================================================
# STEP 6: Display All Student Records
# ============================================================

print("All Student Records:")

cursor.execute("SELECT * FROM student")

data = cursor.fetchall()

for row in data:
    print(row)


# ============================================================
# STEP 7: Update a Specific Record
# Update Sub1 marks of student whose Rollno is 2.
# ============================================================

cursor.execute("""
UPDATE student
SET Sub1 = 80
WHERE Rollno = 2
""")

con.commit()


# ============================================================
# STEP 8: Delete a Specific Record
# Delete student record whose Rollno is 4.
# ============================================================

cursor.execute("""
DELETE FROM student
WHERE Rollno = 4
""")

con.commit()


# ============================================================
# STEP 9: Display Student Details with Highest Total Marks
# ============================================================

print("\nStudent with Highest Total Marks:")

cursor.execute("""
SELECT * FROM student
WHERE Total = (
    SELECT MAX(Total)
    FROM student
)
""")

data = cursor.fetchall()

for row in data:
    print(row)


# ============================================================
# STEP 10: Close Database Connection
# ============================================================

con.close()


# ============================================================
# END OF PRACTICAL ASSIGNMENT - 2
# ============================================================
