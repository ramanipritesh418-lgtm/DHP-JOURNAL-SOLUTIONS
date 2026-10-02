# ============================================================
# DHP-303 DATABASE HANDLING USING PYTHON
# UNIT 3 - PYTHON INTERACTION WITH SQLITE
# COMPLETE CODE SHEET
# ============================================================

# ============================================================
# PART 1 - CREATE AND USE A PYTHON MODULE
# ============================================================

# FILE 1: mymodule.py

def display(name):
    print("My name is " + name)


# FILE 2: main.py

import mymodule

name = input("Enter the name: ")
mymodule.display(name)

# Expected Output:
# Enter the name: Mayank
# My name is Mayank


# ============================================================
# PART 2 - FROM-IMPORT STATEMENT
# ============================================================

from mymodule import display

name = input("Enter the name: ")
display(name)

# Expected Output:
# Enter the name: Mayank
# My name is Mayank


# ============================================================
# PART 3 - IMPORT ALL ATTRIBUTES
# ============================================================

from mymodule import *

display("Mayank")

# Expected Output:
# My name is Mayank


# ============================================================
# PART 4 - NAMESPACE AND SCOPE
# ============================================================

global_var = 100

def outer_function():

    outer_var = 20

    def inner_function():

        inner_var = 30

        print("Inner variable:", inner_var)
        print("Outer variable:", outer_var)

    inner_function()

print("Global variable:", global_var)

outer_function()

# Expected Output:
# Global variable: 100
# Inner variable: 30
# Outer variable: 20


# ============================================================
# PART 5 - SQLITE3 MODULE
# ============================================================

import sqlite3

print("SQLite3 module imported successfully")

# Expected Output:
# SQLite3 module imported successfully


# ============================================================
# PART 6 - CONNECT TO DATABASE
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

print("Opened database successfully")

conn.close()

# Expected Output:
# Opened database successfully

# NOTE:
# If demo.db does not exist, SQLite creates it automatically.


# ============================================================
# PART 7 - CREATE TABLE USING PYTHON
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

print("Opened database successfully")

conn.execute("""
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INTEGER NOT NULL,
    ADDRESS TEXT
)
""")

print("Table created successfully")

conn.close()

# Expected Output:
# Opened database successfully
# Table created successfully


# ============================================================
# PART 8 - INSERT RECORDS
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

conn.execute("""
INSERT INTO STUDENT
(ID, NAME, AGE, ADDRESS)
VALUES (1, 'Aditya', 27, 'Surat')
""")

conn.execute("""
INSERT INTO STUDENT
(ID, NAME, AGE, ADDRESS)
VALUES (2, 'Raj', 32, 'Vapi')
""")

conn.execute("""
INSERT INTO STUDENT
(ID, NAME, AGE, ADDRESS)
VALUES (3, 'Deep', 22, 'Vadodara')
""")

conn.commit()

print("Records inserted successfully")

conn.close()

# Expected Output:
# Records inserted successfully


# ============================================================
# PART 9 - INSERT RECORD USING PLACEHOLDERS
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

student_id = 4
student_name = "Rani"
student_age = 21
student_address = "Ahmedabad"

conn.execute("""
INSERT INTO STUDENT
(ID, NAME, AGE, ADDRESS)
VALUES (?, ?, ?, ?)
""", (student_id, student_name, student_age, student_address))

conn.commit()

print("Record inserted using placeholders")

conn.close()

# Expected Output:
# Record inserted using placeholders


# ============================================================
# PART 10 - EXECUTE SELECT QUERY
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

data = conn.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

conn.close()

# Expected Output:
# (1, 'Aditya', 27, 'Surat')
# (2, 'Raj', 32, 'Vapi')
# (3, 'Deep', 22, 'Vadodara')
# (4, 'Rani', 21, 'Ahmedabad')


# ============================================================
# PART 11 - FETCHONE()
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

cursor = conn.cursor()

query = "SELECT * FROM STUDENT"

cursor.execute(query)

record = cursor.fetchone()

print("First row:")
print(record)

record = cursor.fetchone()

print("Second row:")
print(record)

cursor.close()
conn.close()

# Expected Output:
# First row:
# (1, 'Aditya', 27, 'Surat')
#
# Second row:
# (2, 'Raj', 32, 'Vapi')


# ============================================================
# PART 12 - FETCHALL()
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

cursor = conn.cursor()

query = "SELECT * FROM STUDENT"

cursor.execute(query)

records = cursor.fetchall()

print("Total rows are:", len(records))

print("Printing each row")

for row in records:

    print("ID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Address:", row[3])
    print()

cursor.close()
conn.close()

# Expected Output:
# Total rows are: 4
#
# Printing each row
#
# ID: 1
# Name: Aditya
# Age: 27
# Address: Surat
#
# ID: 2
# Name: Raj
# Age: 32
# Address: Vapi
#
# ID: 3
# Name: Deep
# Age: 22
# Address: Vadodara
#
# ID: 4
# Name: Rani
# Age: 21
# Address: Ahmedabad


# ============================================================
# PART 13 - SELECT SPECIFIC COLUMNS
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

data = conn.execute(
    "SELECT ID, NAME, AGE FROM STUDENT"
)

for row in data:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print()

conn.close()

# Expected Output:
# ID = 1
# NAME = Aditya
# AGE = 27
#
# ID = 2
# NAME = Raj
# AGE = 32
#
# ID = 3
# NAME = Deep
# AGE = 22
#
# ID = 4
# NAME = Rani
# AGE = 21


# ============================================================
# PART 14 - UPDATE RECORD
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

conn.execute("""
UPDATE STUDENT
SET AGE = 28
WHERE ID = 1
""")

conn.commit()

print("Record updated successfully")

conn.close()

# Expected Output:
# Record updated successfully


# ============================================================
# PART 15 - DELETE RECORD
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

student_id = int(input("Enter ID to delete: "))

conn.execute(
    "DELETE FROM STUDENT WHERE ID = ?",
    (student_id,)
)

conn.commit()

print(
    "Total number of rows deleted:",
    conn.total_changes
)

conn.close()

# Expected Output:
# Enter ID to delete: 4
# Total number of rows deleted: 1


# ============================================================
# PART 16 - total_changes
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

conn.execute("""
UPDATE STUDENT
SET AGE = AGE + 1
WHERE ID = 1
""")

print("Total changes:", conn.total_changes)

conn.commit()

conn.close()

# Expected Output:
# Total changes: 1


# ============================================================
# PART 17 - COMMIT()
# ============================================================

import sqlite3

conn = sqlite3.connect("demo.db")

conn.execute("""
INSERT INTO STUDENT
(ID, NAME, AGE, ADDRESS)
VALUES (5, 'Mehul', 20, 'Surat')
""")

# Save the transaction
conn.commit()

print("Transaction committed successfully")

conn.close()

# Expected Output:
# Transaction committed successfully


# ============================================================
# PART 18 - COMPLETE CRUD PROGRAM
# ============================================================

import sqlite3

conn = sqlite3.connect("crud.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INTEGER NOT NULL,
    ADDRESS TEXT
)
""")

# CREATE / INSERT
conn.execute("""
INSERT OR IGNORE INTO STUDENT
VALUES (1, 'Aditya', 27, 'Surat')
""")

conn.execute("""
INSERT OR IGNORE INTO STUDENT
VALUES (2, 'Raj', 32, 'Vapi')
""")

conn.commit()

# READ
print("Student Records:")

data = conn.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

# UPDATE
conn.execute("""
UPDATE STUDENT
SET AGE = 28
WHERE ID = 1
""")

conn.commit()

print("Record updated successfully")

# DELETE
conn.execute("""
DELETE FROM STUDENT
WHERE ID = 2
""")

conn.commit()

print("Record deleted successfully")

conn.close()

# Expected Output:
# Student Records:
# (1, 'Aditya', 27, 'Surat')
# (2, 'Raj', 32, 'Vapi')
# Record updated successfully
# Record deleted successfully


# ============================================================
# PART 19 - COMPLETE FETCHONE + FETCHALL EXAMPLE
# ============================================================

import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    COURSE TEXT,
    MARKS INTEGER
)
""")

cursor.execute("""
INSERT OR IGNORE INTO STUDENT
VALUES (1, 'Raj', 'BCA', 88)
""")

cursor.execute("""
INSERT OR IGNORE INTO STUDENT
VALUES (2, 'Rani', 'MCA', 99)
""")

cursor.execute("""
INSERT OR IGNORE INTO STUDENT
VALUES (3, 'Deep', 'BCA', 50)
""")

conn.commit()

# Fetch one record
cursor.execute("SELECT * FROM STUDENT")

record = cursor.fetchone()

print("First record:", record)

# Fetch remaining records
records = cursor.fetchall()

print("Remaining records:")

for row in records:
    print(row)

cursor.close()
conn.close()

# Expected Output:
# First record: (1, 'Raj', 'BCA', 88)
# Remaining records:
# (2, 'Rani', 'MCA', 99)
# (3, 'Deep', 'BCA', 50)


# ============================================================
# PART 20 - COMPLETE ERROR HANDLING EXAMPLE
# ============================================================

import sqlite3

connection = None

try:

    connection = sqlite3.connect("student.db")

    cursor = connection.cursor()

    print("Connected to database")

    cursor.execute("SELECT * FROM STUDENT")

    records = cursor.fetchall()

    print("Total rows:", len(records))

    for row in records:
        print(row)

    cursor.close()

except sqlite3.Error as error:

    print("Failed to read data from table:", error)

finally:

    if connection:
        connection.close()

    print("The SQLite connection is closed")

# Expected Output:
# Connected to database
# Total rows: 3
# (1, 'Raj', 'BCA', 88)
# (2, 'Rani', 'MCA', 99)
# (3, 'Deep', 'BCA', 50)
# The SQLite connection is closed


# ============================================================
# IMPORTANT SYNTAX REVISION
# ============================================================

# Import SQLite:
import sqlite3

# Connect:
conn = sqlite3.connect("demo.db")

# Create cursor:
cursor = conn.cursor()

# Execute:
cursor.execute("SQL QUERY")

# Fetch one:
cursor.fetchone()

# Fetch all:
cursor.fetchall()

# Save changes:
conn.commit()

# Close cursor:
cursor.close()

# Close connection:
conn.close()


# ============================================================
# UNIT 3 QUICK MEMORY
# ============================================================

# MODULE
# .py file
#
# import
# Import complete module
#
# from-import
# Import specific function/attribute
#
# PYTHONPATH
# Directory where Python searches for modules/packages
#
# NAMESPACE
# Manages names
#
# PACKAGE
# Collection/hierarchy of modules
#
# sqlite3
# Python module for SQLite
#
# connect()
# Opens/creates database connection
#
# execute()
# Executes SQL statement
#
# fetchone()
# Fetches one row
#
# fetchall()
# Fetches all remaining rows
#
# commit()
# Saves transaction
#
# total_changes
# Number of rows modified/inserted/deleted
#
# close()
# Closes connection/cursor


# ============================================================
# MOST IMPORTANT EXAM FLOW
# ============================================================

# import sqlite3
#
#       ↓
#
# sqlite3.connect()
#
#       ↓
#
# cursor()
#
#       ↓
#
# execute()
#
#       ↓
#
# ┌───────────────┐
# │ SELECT        │
# │ INSERT        │
# │ UPDATE        │
# │ DELETE        │
# └───────────────┘
#
#       ↓
#
# fetchone() / fetchall()
#
#       ↓
#
# commit()
#
#       ↓
#
# close()


# ============================================================
# END OF UNIT 3 CODE SHEET
# ============================================================
