# ============================================================
# DHP 303 - PAPER H
# FILE: 02_School_CSV.py
#
# QUESTION:
# 1. Add email_id column to SCHOOL table.
# 2. Export student_id, student_name and std to Student_List.csv.
#
# CONCEPT:
# ALTER TABLE, SELECT, CSV export using csv module
# ============================================================

import sqlite3
import csv

# Connect to existing database
con = sqlite3.connect("School.db")
cur = con.cursor()

# 1. Add email_id column if it does not already exist
cur.execute("PRAGMA table_info(SCHOOL)")
columns = [row[1] for row in cur.fetchall()]

if "email_id" not in columns:
    cur.execute("ALTER TABLE SCHOOL ADD COLUMN email_id TEXT")
    con.commit()
    print("email_id column added successfully.")
else:
    print("email_id column already exists.")

# Optional: Add email addresses to the records
cur.execute("""
    UPDATE SCHOOL
    SET email_id = lower(student_name) || '@gmail.com'
""")
con.commit()

# 2. Export selected columns to CSV
cur.execute("""
    SELECT student_id, student_name, Class AS std
    FROM SCHOOL
""")

rows = cur.fetchall()

with open("Student_List.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["student_id", "student_name", "std"])

    # Write student records
    writer.writerows(rows)

print("Data exported to Student_List.csv successfully.")

con.close()
