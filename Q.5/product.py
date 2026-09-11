# Q.5 Create following table with appropriate Constraints:
# Product (prod_id, prod_name, price, qty, total_amount)
#
# 1) Import Product.csv file data into Product table.
# 2) Export Product table data into prod.csv file.
#
#
# STEP 1: Create Product.csv
#
# Create a new file named "Product.csv" in the same folder
# as this Python file.
#
# Write the following data in Product.csv:
#
# 1,Laptop,50000,2,100000
# 2,Mouse,500,5,2500
# 3,Keyboard,1200,3,3600
# 4,Monitor,15000,2,30000
# 5,Printer,10000,1,10000
#
#
# STEP 2: Python Program
#
# Import required modules

import sqlite3
import csv

# Connect to Product database

con = sqlite3.connect("Product.db")

# Create cursor

cursor = con.cursor()

# Create Product table with constraints

cursor.execute("""
CREATE TABLE IF NOT EXISTS Product(
    prod_id INTEGER PRIMARY KEY,
    prod_name TEXT,
    price REAL,
    qty INTEGER,
    total_amount REAL
)
""")

# Open Product.csv file in read mode

with open("Product.csv", "r") as file:

    # Create CSV reader

    reader = csv.reader(file)

    # Read CSV file row by row

    for row in reader:

        # Insert CSV data into Product table

        cursor.execute(
            "INSERT INTO Product VALUES(?,?,?,?,?)",
            row
        )

# Save changes

con.commit()

# Select all records from Product table

cursor.execute("SELECT * FROM Product")

# Fetch all records

records = cursor.fetchall()

# Display all records

for row in records:
    print(row)

# Open prod.csv file in write mode for exporting data

with open("prod.csv", "w", newline="") as file:

    # Create CSV writer

    writer = csv.writer(file)

    # Write Product table data into prod.csv

    writer.writerows(records)

# Close database connection

con.close()


# OUTPUT:
#
# (1, 'Laptop', 50000.0, 2, 100000.0)
# (2, 'Mouse', 500.0, 5, 2500.0)
# (3, 'Keyboard', 1200.0, 3, 3600.0)
# (4, 'Monitor', 15000.0, 2, 30000.0)
# (5, 'Printer', 10000.0, 1, 10000.0)
#
#
# FINAL FILES:
#
# Product.py    -> Python program
# Product.csv   -> Input CSV file
# Product.db    -> SQLite database
# prod.csv      -> Exported CSV file
#
#
# FLOW:
#
# Product.csv
#      ↓
# Import
#      ↓
# Product Table
#      ↓
# Export
#      ↓
# prod.csv
