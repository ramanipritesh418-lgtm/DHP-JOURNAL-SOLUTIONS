# ============================================================
# DHP PRACTICAL - PAPER H
# Q.2 Write a Python script to perform the following:
# 1. Create Clinic table and insert at least 6 records.
# 2. Export data to clinic.csv.
# 3. Display doctors of Cardiology specialization.
# 4. Drop Clinic table.
# 5. Import CSV data into Clinic_New table.
# ============================================================

# CONCEPT:
# SQLite stores data in database tables.
# CSV files store tabular data in text format.
#
# Clinic Table:
# DoctorID, DoctorName, Specialization, Patients, Fees
# ============================================================

import sqlite3
import csv

# Connect to database
con = sqlite3.connect("Clinic.db")
cur = con.cursor()

# ------------------------------------------------------------
# 1. CREATE CLINIC TABLE
# ------------------------------------------------------------

cur.execute("""
    CREATE TABLE IF NOT EXISTS Clinic(
        DoctorID INTEGER PRIMARY KEY,
        DoctorName TEXT,
        Specialization TEXT,
        Patients INTEGER,
        Fees REAL
    )
""")

# ------------------------------------------------------------
# 2. INSERT 6 RECORDS
# ------------------------------------------------------------

cur.execute("SELECT COUNT(*) FROM Clinic")

if cur.fetchone()[0] == 0:
    data = [
        (1, 'Dr. Amit', 'Cardiology', 25, 800),
        (2, 'Dr. Neha', 'Neurology', 30, 1000),
        (3, 'Dr. Raj', 'Cardiology', 20, 900),
        (4, 'Dr. Priya', 'Dermatology', 15, 500),
        (5, 'Dr. Kiran', 'Cardiology', 35, 1200),
        (6, 'Dr. Meera', 'Orthopedic', 22, 700)
    ]

    cur.executemany("""
        INSERT INTO Clinic
        VALUES(?,?,?,?,?)
    """, data)

    con.commit()
    print("6 Records Inserted Successfully.")

# ------------------------------------------------------------
# 3. DISPLAY ALL CLINIC RECORDS
# ------------------------------------------------------------

print("\nAll Clinic Records:")

cur.execute("SELECT * FROM Clinic")

for row in cur.fetchall():
    print(row)

# ------------------------------------------------------------
# 4. EXPORT DATA TO clinic.csv
# ------------------------------------------------------------

cur.execute("SELECT * FROM Clinic")
records = cur.fetchall()

with open("clinic.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "DoctorID",
        "DoctorName",
        "Specialization",
        "Patients",
        "Fees"
    ])

    writer.writerows(records)

print("\nData Exported to clinic.csv Successfully.")

# ------------------------------------------------------------
# 5. DISPLAY CARDIOLOGY DOCTORS
# ------------------------------------------------------------

print("\nDoctors of Cardiology:")

cur.execute("""
    SELECT * FROM Clinic
    WHERE Specialization = 'Cardiology'
""")

for row in cur.fetchall():
    print(row)

# ------------------------------------------------------------
# 6. DROP CLINIC TABLE
# ------------------------------------------------------------

cur.execute("DROP TABLE Clinic")
con.commit()

print("\nClinic Table Dropped Successfully.")

# ------------------------------------------------------------
# 7. CREATE NEW TABLE Clinic_New
# ------------------------------------------------------------

cur.execute("""
    CREATE TABLE IF NOT EXISTS Clinic_New(
        DoctorID INTEGER PRIMARY KEY,
        DoctorName TEXT,
        Specialization TEXT,
        Patients INTEGER,
        Fees REAL
    )
""")

# ------------------------------------------------------------
# 8. IMPORT CSV DATA INTO Clinic_New
# ------------------------------------------------------------

cur.execute("SELECT COUNT(*) FROM Clinic_New")

if cur.fetchone()[0] == 0:
    with open("clinic.csv", "r", newline="") as file:
        reader = csv.reader(file)

        next(reader)  # Skip column headings

        for row in reader:
            cur.execute("""
                INSERT INTO Clinic_New
                VALUES(?,?,?,?,?)
            """, (
                int(row[0]),
                row[1],
                row[2],
                int(row[3]),
                float(row[4])
            ))

    con.commit()
    print("CSV Data Imported Successfully.")

# ------------------------------------------------------------
# 9. DISPLAY IMPORTED RECORDS
# ------------------------------------------------------------

print("\nAll Records from Clinic_New:")

cur.execute("SELECT * FROM Clinic_New")

for row in cur.fetchall():
    print(row)

con.close()

# ============================================================
# OUTPUT:
# ============================================================
#
# 6 Records Inserted Successfully.
#
# All Clinic Records:
# (1, 'Dr. Amit', 'Cardiology', 25, 800.0)
# (2, 'Dr. Neha', 'Neurology', 30, 1000.0)
# (3, 'Dr. Raj', 'Cardiology', 20, 900.0)
# (4, 'Dr. Priya', 'Dermatology', 15, 500.0)
# (5, 'Dr. Kiran', 'Cardiology', 35, 1200.0)
# (6, 'Dr. Meera', 'Orthopedic', 22, 700.0)
#
# Data Exported to clinic.csv Successfully.
#
# Doctors of Cardiology:
# (1, 'Dr. Amit', 'Cardiology', 25, 800.0)
# (3, 'Dr. Raj', 'Cardiology', 20, 900.0)
# (5, 'Dr. Kiran', 'Cardiology', 35, 1200.0)
#
# Clinic Table Dropped Successfully.
# CSV Data Imported Successfully.
#
# All Records from Clinic_New:
# (1, 'Dr. Amit', 'Cardiology', 25, 800.0)
# (2, 'Dr. Neha', 'Neurology', 30, 1000.0)
# (3, 'Dr. Raj', 'Cardiology', 20, 900.0)
# (4, 'Dr. Priya', 'Dermatology', 15, 500.0)
# (5, 'Dr. Kiran', 'Cardiology', 35, 1200.0)
# (6, 'Dr. Meera', 'Orthopedic', 22, 700.0)
#
# ============================================================
# EXPLANATION:
# ============================================================
#
# 1. CREATE TABLE creates the Clinic table.
# 2. executemany() inserts six records.
# 3. csv.writer() writes data into a CSV file.
# 4. writer.writerow() writes column headings.
# 5. writer.writerows() writes all records.
# 6. WHERE selects doctors of Cardiology.
# 7. DROP TABLE deletes the original Clinic table.
# 8. csv.reader() reads data from the CSV file.
# 9. next(reader) skips the heading row.
# 10. INSERT INTO Clinic_New stores imported records.
# 11. fetchall() retrieves all records.
#
# NOTE:
# The question mentions Excel data in the last step.
# This solution imports clinic.csv, the file exported above.
# ============================================================