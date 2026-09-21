# ============================================================
# DATABASE HANDLING USING PYTHON
# ============================================================
# FILE NAME:
# employee_dataframe.py
#
# ============================================================
# QUESTION:
#
# 2. Create following table and store any five records:
# Employee(eno number primary key, Ename text(20),designation
# text(10),basic number , da number,gross_salary number)
#
# write python programs to perform following tasks:
#
# 1) Store the table data into dataframe and display the dataframe.
#
# 2) Sort the dataframe based used on gross salary and List out
#    bottom two record from thedataframe.
#
# 3)Display all records from dataframe whose gross Display gross salary is
#    more than 25000 .
#
# 4)Display gross salary of employee whose eno is 4.
#
# ============================================================
# HOW TO CREATE AND RUN THE FILE:
#
# 1. Open VS Code / Notepad++.
# 2. Create a new Python file.
# 3. Save the file as:
#       employee_dataframe.py
# 4. Install pandas if required:
#       pip install pandas
# 5. Run the program:
#       python employee_dataframe.py
#
# The program will automatically create:
#       employee.db
#
# ============================================================


import sqlite3
import pandas as pd


# ============================================================
# STEP 1: CONNECT TO DATABASE
# ============================================================

con = sqlite3.connect("employee.db")


# ============================================================
# STEP 2: CREATE CURSOR
# ============================================================

cur = con.cursor()


# ============================================================
# STEP 3: CREATE EMPLOYEE TABLE
# ============================================================

cur.execute("""
CREATE TABLE IF NOT EXISTS Employee
(
    eno INTEGER PRIMARY KEY,
    Ename TEXT(20) NOT NULL,
    designation TEXT(10),
    basic INTEGER,
    da INTEGER,
    gross_salary INTEGER
)
""")


# ============================================================
# STEP 4: DELETE OLD RECORDS
# ============================================================

cur.execute("DELETE FROM Employee")


# ============================================================
# STEP 5: STORE ANY FIVE RECORDS
# ============================================================

employees = [
    (1, "Rahul", "Manager", 20000, 5000, 25000),
    (2, "Amit", "Clerk", 18000, 4000, 22000),
    (3, "Priya", "Developer", 25000, 7000, 32000),
    (4, "Pritesh", "Analyst", 22000, 6000, 28000),
    (5, "Neha", "Developer", 30000, 8000, 38000)
]

cur.executemany(
    "INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?)",
    employees
)


# ============================================================
# STEP 6: SAVE CHANGES
# ============================================================

con.commit()


# ============================================================
# QUESTION 1:
# Store the table data into dataframe and display the dataframe.
# ============================================================

df = pd.read_sql_query("SELECT * FROM Employee", con)

print("\n1) Complete Employee DataFrame:")
print(df)


# ============================================================
# QUESTION 2:
# Sort the dataframe based on gross salary and list out
# bottom two records from the dataframe.
# ============================================================

sorted_df = df.sort_values(by="gross_salary")

print("\n2) DataFrame Sorted by Gross Salary:")
print(sorted_df)

print("\nBottom Two Records:")
print(sorted_df.head(2))


# ============================================================
# QUESTION 3:
# Display all records from dataframe whose gross salary is
# more than 25000.
# ============================================================

print("\n3) Employees whose Gross Salary is more than 25000:")
print(df[df["gross_salary"] > 25000])


# ============================================================
# QUESTION 4:
# Display gross salary of employee whose eno is 4.
# ============================================================

print("\n4) Gross Salary of Employee whose eno is 4:")
print(df.loc[df["eno"] == 4, "gross_salary"].iloc[0])


# ============================================================
# CLOSE DATABASE CONNECTION
# ============================================================

con.close()


# ============================================================
# EXPECTED OUTPUT:
# ============================================================
#
# 1) Complete Employee DataFrame:
#    eno    Ename designation  basic    da  gross_salary
# 0    1    Rahul     Manager  20000  5000         25000
# 1    2     Amit       Clerk  18000  4000         22000
# 2    3    Priya   Developer  25000  7000         32000
# 3    4  Pritesh     Analyst  22000  6000         28000
# 4    5     Neha   Developer  30000  8000         38000
#
#
# 2) DataFrame Sorted by Gross Salary:
#    eno    Ename designation  basic    da  gross_salary
# 1    2     Amit       Clerk  18000  4000         22000
# 0    1    Rahul     Manager  20000  5000         25000
# 3    4  Pritesh     Analyst  22000  6000         28000
# 2    3    Priya   Developer  25000  7000         32000
# 4    5     Neha   Developer  30000  8000         38000
#
# Bottom Two Records:
#    eno Ename designation  basic    da  gross_salary
# 1    2  Amit       Clerk  18000  4000         22000
# 0    1 Rahul     Manager  20000  5000         25000
#
#
# 3) Employees whose Gross Salary is more than 25000:
#    eno    Ename designation  basic    da  gross_salary
# 2    3    Priya   Developer  25000  7000         32000
# 3    4  Pritesh     Analyst  22000  6000         28000
# 4    5     Neha   Developer  30000  8000         38000
#
#
# 4) Gross Salary of Employee whose eno is 4:
# 28000
#
# ============================================================
