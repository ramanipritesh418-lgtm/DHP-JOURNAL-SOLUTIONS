# ============================================================
# DHP 303 - Database Handling Using Python (PR)
# B.C.A. Semester III - December 2025
#
# QUESTION 2:
# 1. Add the column email_id in Cust_Master table.
# 2. Export CSV file of all Customers data.
#
# ============================================================
# CONCEPT:
# ALTER TABLE - Adds a new column to an existing table.
# PRAGMA      - Checks the table's column information.
# csv.writer  - Writes data into a CSV file.
# SELECT      - Retrieves all customer records.
# ============================================================

import sqlite3
import csv

# Connect to the same database created in Question 1
con = sqlite3.connect("Company.db")
cur = con.cursor()

# Step 1: Check whether email_id column already exists
cur.execute("PRAGMA table_info(Cust_Master)")
columns = [row[1] for row in cur.fetchall()]

# Add email_id only if it does not exist
if "email_id" not in columns:
    cur.execute("ALTER TABLE Cust_Master ADD COLUMN email_id TEXT")
    con.commit()
    print("email_id column added successfully!")
else:
    print("email_id column already exists.")

# Step 2: Retrieve all customer records
cur.execute("SELECT * FROM Cust_Master")
rows = cur.fetchall()

# Retrieve column names for the CSV heading
cur.execute("PRAGMA table_info(Cust_Master)")
columns = [row[1] for row in cur.fetchall()]

# Step 3: Export all customer data to CSV
with open("customers.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(columns)

    # Write customer records
    writer.writerows(rows)

print("All customer data exported to customers.csv successfully!")

# Step 4: Display customer data
print("\nCustomer Master Details:")

for row in rows:
    print(row)

# Close database connection
con.close()

# ============================================================
# EXPECTED OUTPUT:
#
# email_id column added successfully!
# All customer data exported to customers.csv successfully!
#
# Customer Master Details:
# (1, 'Amit', '9876543210', 'Surat', None)
# (2, 'Neha', '9876543211', 'Ahmedabad', None)
# (3, 'Raj', '9876543212', 'Vadodara', None)
#
# Note: If email_id already exists, the first message will
# instead say: email_id column already exists.
#
# ============================================================
# EXPLANATION:
#
# 1. PRAGMA table_info() checks existing columns.
# 2. ALTER TABLE adds email_id to Cust_Master.
# 3. SELECT * retrieves all customer records.
# 4. csv.writer() writes column headings and records to CSV.
# 5. customers.csv contains all customer data.
#
# ============================================================