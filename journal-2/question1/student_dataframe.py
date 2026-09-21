# ============================================================
# DATABASE HANDLING USING PYTHON
# ============================================================
# File Name: student_dataframe.py
#
# QUESTION:
# 1. Create Student Table with appropriate constraints.
# STUDENT(sno number primary key, sname text(20), age number,
# total_marks number)
#
# write python programs to perform following task:
# 1)store the table data into a dataframe and display the dataframe.
# 2) List out top three records from the dataframe
# 3)Display all records from dataframe whose age is not less than 18.
# 4)Display age of student whose sno is 5. (use loc() and iloc() function)
#
# ============================================================
# HOW TO CREATE AND RUN THE FILE
# ============================================================
# 1. Open VS Code / Notepad++.
# 2. Create a new Python file.
# 3. Save the file as:
#       student_dataframe.py
# 4. Install pandas if required:
#       pip install pandas
# 5. Run the program:
#       python student_dataframe.py
#
# The program will automatically create:
#       student.db
#
# ============================================================


import sqlite3
import pandas as pd


# ============================================================
# STEP 1: CONNECT TO DATABASE
# ============================================================

con = sqlite3.connect("student.db")


# ============================================================
# STEP 2: CREATE CURSOR
# ============================================================

cur = con.cursor()


# ============================================================
# STEP 3: CREATE STUDENT TABLE
# ============================================================

cur.execute("""
CREATE TABLE IF NOT EXISTS STUDENT
(
    sno INTEGER PRIMARY KEY,
    sname TEXT(20) NOT NULL,
    age INTEGER NOT NULL,
    total_marks INTEGER
)
""")


# ============================================================
# STEP 4: DELETE OLD RECORDS
# ============================================================

cur.execute("DELETE FROM STUDENT")


# ============================================================
# STEP 5: INSERT STUDENT RECORDS
# ============================================================

students = [
    (1, "Rahul", 17, 450),
    (2, "Amit", 19, 480),
    (3, "Priya", 20, 470),
    (4, "Neha", 17, 430),
    (5, "Pritesh", 21, 490),
    (6, "Karan", 18, 460)
]

cur.executemany(
    "INSERT INTO STUDENT VALUES (?, ?, ?, ?)",
    students
)


# ============================================================
# STEP 6: SAVE CHANGES
# ============================================================

con.commit()


# ============================================================
# QUESTION 1:
# Store the table data into a dataframe and display the dataframe.
# ============================================================

df = pd.read_sql_query("SELECT * FROM STUDENT", con)

print("\n1) Complete Student DataFrame:")
print(df)


# ============================================================
# QUESTION 2:
# List out top three records from the dataframe.
# ============================================================

print("\n2) Top Three Records:")
print(df.head(3))


# ============================================================
# QUESTION 3:
# Display all records from dataframe whose age is not less than 18.
# ============================================================

print("\n3) Students whose age is not less than 18:")
print(df[df["age"] >= 18])


# ============================================================
# QUESTION 4:
# Display age of student whose sno is 5.
# Use loc() and iloc() function.
# ============================================================

# Using loc()
df_index = df.set_index("sno")

print("\n4) Age of student whose sno is 5 using loc():")
print(df_index.loc[5, "age"])


# Using iloc()
print("\nAge of student whose sno is 5 using iloc():")
print(df.iloc[4, 2])


# ============================================================
# CLOSE DATABASE CONNECTION
# ============================================================

con.close()


# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# 1) Complete Student DataFrame:
#    sno    sname  age  total_marks
# 0    1    Rahul   17          450
# 1    2     Amit   19          480
# 2    3    Priya   20          470
# 3    4     Neha   17          430
# 4    5  Pritesh   21          490
# 5    6    Karan   18          460
#
# 2) Top Three Records:
#    sno  sname  age  total_marks
# 0    1  Rahul   17          450
# 1    2   Amit   19          480
# 2    3  Priya   20          470
#
# 3) Students whose age is not less than 18:
#    sno    sname  age  total_marks
# 1    2     Amit   19          480
# 2    3    Priya   20          470
# 4    5  Pritesh   21          490
# 5    6    Karan   18          460
#
# 4) Age of student whose sno is 5 using loc():
# 21
#
# Age of student whose sno is 5 using iloc():
# 21
#
# ============================================================
