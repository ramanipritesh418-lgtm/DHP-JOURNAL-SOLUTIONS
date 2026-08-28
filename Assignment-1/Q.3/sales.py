# ============================================================
# PRACTICAL ASSIGNMENT - 3
# DATABASE HANDLING USING PYTHON
# ============================================================

"""
QUESTION:

Sales (sid, year, totalsales)

Create the above table into a SQLite database with appropriate
constraints.

1) Insert at least 5 to 10 records into the Sales table.

2) Export Sales table data into a sales.csv file.

3) Write a Python script that reads the sales.csv file.
"""


# ============================================================
# STEP 1: Import Required Modules
# ============================================================

import sqlite3
import csv


# ============================================================
# STEP 2: Create / Connect SQLite Database
# ============================================================

con = sqlite3.connect("Sales.db")


# ============================================================
# STEP 3: Create Cursor
# ============================================================

cursor = con.cursor()


# ============================================================
# STEP 4: Create Sales Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales(
    sid INTEGER PRIMARY KEY,
    year INTEGER,
    totalsales REAL
)
""")


# ============================================================
# STEP 5: Insert 10 Records into Sales Table
# ============================================================

data = [
    (1, 2021, 50000),
    (2, 2022, 65000),
    (3, 2023, 72000),
    (4, 2024, 85000),
    (5, 2025, 95000),
    (6, 2021, 55000),
    (7, 2022, 68000),
    (8, 2023, 75000),
    (9, 2024, 88000),
    (10, 2025, 99000)
]

cursor.executemany(
    "INSERT INTO Sales VALUES (?, ?, ?)",
    data
)

con.commit()


# ============================================================
# STEP 6: Display All Sales Records
# ============================================================

print("Sales Table Records:")

cursor.execute("SELECT * FROM Sales")

records = cursor.fetchall()

for row in records:
    print(row)


# ============================================================
# STEP 7: Export Sales Table Data to sales.csv File
# ============================================================

cursor.execute("SELECT * FROM Sales")

records = cursor.fetchall()

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column names
    writer.writerow(["sid", "year", "totalsales"])

    # Write all records
    writer.writerows(records)


# ============================================================
# STEP 8: Read sales.csv File
# ============================================================

print("\nData Read from sales.csv:")

with open("sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# ALTERNATIVE METHOD USING PANDAS
# ============================================================

"""
import pandas as pd

# Read CSV file
df = pd.read_csv("sales.csv")

# Display CSV data
print(df)
"""


# ============================================================
# STEP 9: Close Database Connection
# ============================================================

con.close()


# ============================================================
# END OF PRACTICAL ASSIGNMENT - 3

#:: Open the folder containing the SQLite database
#cd /d "D:\DHP paper solution\DHP JOURNAL SOLUTIONS\Practicle
#Assignment-1\question 3"

#:: Open the Sales.db database in SQLite
#sqlite3 Sales.db
# ============================================================


