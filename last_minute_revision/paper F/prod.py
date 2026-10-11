# ============================================================
# DHP 303 - Database Handling Using Python (PR)
# B.C.A. Semester III - December 2025
#
# QUESTION 1:
# Consider a product.csv file with columns:
# pid, pname, category, price.
#
# 1. Using writer object, write 5 records in product.csv.
# 2. Read data using reader object.
# 3. Insert all records into SQLite table Product using cursor.
# 4. Display all records where price > 70.
#
# ============================================================
# CONCEPT:
# csv.writer()  - Writes records into CSV file.
# csv.reader()  - Reads records from CSV file.
# sqlite3       - Connects to SQLite database.
# cursor        - Executes SQL queries.
# WHERE         - Filters records using a condition.
# ============================================================

import csv
import sqlite3

# Step 1: Write 5 records into product.csv
with open("product.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["pid", "pname", "category", "price"])

    # Write 5 product records
    data = [
        [1, "Mouse", "Electronics", 50],
        [2, "Keyboard", "Electronics", 90],
        [3, "Pen", "Stationery", 20],
        [4, "Bag", "Accessories", 120],
        [5, "Notebook", "Stationery", 80]
    ]

    writer.writerows(data)

print("Records written to product.csv successfully!")

# Step 2: Read data using reader object
with open("product.csv", "r", newline="") as file:
    reader = csv.reader(file)

    # Read column headings
    header = next(reader)

    # Read all product records
    records = list(reader)

print("\nData read from product.csv:")
print(header)

for row in records:
    print(row)

# Step 3: Insert records into SQLite Product table
con = sqlite3.connect("Product.db")
cur = con.cursor()

# Create Product table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Product (
        pid INTEGER PRIMARY KEY,
        pname TEXT,
        category TEXT,
        price REAL
    )
""")

# Clear old records before inserting
cur.execute("DELETE FROM Product")

# Insert CSV records into the table
cur.executemany("""
    INSERT INTO Product (pid, pname, category, price)
    VALUES (?, ?, ?, ?)
""", records)

con.commit()

print("\nRecords inserted into Product table successfully!")

# Step 4: Display records where price > 70
print("\nProducts whose price is greater than 70:")

cur.execute("SELECT * FROM Product WHERE price > 70")

for row in cur.fetchall():
    print(row)

# Close database connection
con.close()

# ============================================================
# EXPECTED OUTPUT:
#
# Records written to product.csv successfully!
#
# Data read from product.csv:
# ['pid', 'pname', 'category', 'price']
# ['1', 'Mouse', 'Electronics', '50']
# ['2', 'Keyboard', 'Electronics', '90']
# ['3', 'Pen', 'Stationery', '20']
# ['4', 'Bag', 'Accessories', '120']
# ['5', 'Notebook', 'Stationery', '80']
#
# Records inserted into Product table successfully!
#
# Products whose price is greater than 70:
# (2, 'Keyboard', 'Electronics', 90.0)
# (4, 'Bag', 'Accessories', 120.0)
# (5, 'Notebook', 'Stationery', 80.0)
#
# ============================================================
# EXPLANATION:
#
# 1. csv.writer() writes headings and 5 records into product.csv.
# 2. csv.reader() reads the CSV file.
# 3. sqlite3.connect() opens the Product.db database.
# 4. executemany() inserts all CSV records into Product.
# 5. WHERE price > 70 displays products priced above 70.
#
# ============================================================
