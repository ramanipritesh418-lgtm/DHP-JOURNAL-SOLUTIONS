# ============================================================
# Paper B - Question 2 (10 Marks)
#
# QUESTION:
# Create University(ProfID, ProfName, Department, Experience,
# Salary) and insert at least 7 records.
# 1. Export data into university.csv.
# 2. Display professors with Experience > 10 years.
# 3. Drop University table.
# 4. Import CSV data into University_New.
#
# CONCEPT:
# 1. CREATE TABLE creates the University table.
# 2. csv.writer() exports the records.
# 3. WHERE Experience > 10 selects experienced professors.
# 4. DROP TABLE removes the original table.
# 5. csv.reader() reads CSV records.
# 6. University_New stores the imported records.
# ============================================================

import sqlite3
import csv

con = sqlite3.connect("University.db")
cur = con.cursor()

# Create University table
cur.execute("""
CREATE TABLE IF NOT EXISTS University(
    ProfID INTEGER PRIMARY KEY,
    ProfName TEXT,
    Department TEXT,
    Experience INTEGER,
    Salary REAL
)
""")

cur.execute("DELETE FROM University")

# Insert at least 7 records
data = [
    (1, "Amit", "Computer", 12, 65000),
    (2, "Neha", "Science", 8, 50000),
    (3, "Raj", "Commerce", 15, 70000),
    (4, "Kiran", "Computer", 11, 62000),
    (5, "Mehul", "Mathematics", 6, 45000),
    (6, "Nita", "Science", 18, 80000),
    (7, "Ravi", "Commerce", 9, 52000)
]

cur.executemany(
    "INSERT INTO University VALUES (?, ?, ?, ?, ?)", data
)
con.commit()

# 1. Export table into university.csv
cur.execute("SELECT * FROM University")
rows = cur.fetchall()

with open("university.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["ProfID", "ProfName", "Department", "Experience", "Salary"]
    )
    writer.writerows(rows)

print("Data exported to university.csv")

# 2. Display professors having more than 10 years of experience
print("\nProfessors with Experience > 10:")

cur.execute("SELECT * FROM University WHERE Experience > 10")

for row in cur.fetchall():
    print(row)

# 3. Drop University table
cur.execute("DROP TABLE University")
con.commit()

print("\nUniversity table dropped")

# 4. Import CSV data into University_New
with open("university.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    imported_data = list(reader)

cur.execute("""
CREATE TABLE IF NOT EXISTS University_New(
    ProfID INTEGER PRIMARY KEY,
    ProfName TEXT,
    Department TEXT,
    Experience INTEGER,
    Salary REAL
)
""")

cur.execute("DELETE FROM University_New")

cur.executemany(
    "INSERT INTO University_New VALUES (?, ?, ?, ?, ?)",
    [
        (int(r[0]), r[1], r[2], int(r[3]), float(r[4]))
        for r in imported_data
    ]
)
con.commit()

print("\nData imported into University_New:")

cur.execute("SELECT * FROM University_New")

for row in cur.fetchall():
    print(row)

con.close()

# OUTPUT:
# Data exported to university.csv
#
# Professors with Experience > 10:
# (1, 'Amit', 'Computer', 12, 65000.0)
# (3, 'Raj', 'Commerce', 15, 70000.0)
# (4, 'Kiran', 'Computer', 11, 62000.0)
# (6, 'Nita', 'Science', 18, 80000.0)
#
# University table dropped
# All 7 records are imported into University_New.