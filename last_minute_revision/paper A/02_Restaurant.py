# ============================================================
# Paper A - Question 2 (10 Marks)
#
# QUESTION:
# Create Restaurant(OrderID, Customer, Dish, Quantity,
# BillAmount) and insert at least 6 records.
# 1. Export data to restaurant.xlsx in CSV format.
# 2. Display orders where Quantity > 3.
# 3. Drop Restaurant table.
# 4. Import CSV data into Restaurant_New.
#
# CONCEPT:
# 1. CREATE TABLE creates the Restaurant table.
# 2. INSERT adds six records.
# 3. csv.writer() exports data into a CSV file.
# 4. WHERE Quantity > 3 filters orders.
# 5. DROP TABLE deletes the original table.
# 6. csv.reader() reads the exported file.
# 7. Restaurant_New stores the imported records.
#
# NOTE:
# The question specifies a CSV file named restaurant.xlsx.
# This code stores CSV text with that exact filename.
# It is NOT a genuine Excel workbook.
# ============================================================

import sqlite3
import csv

con = sqlite3.connect("Restaurant.db")
cur = con.cursor()

# Create Restaurant table
cur.execute("""
CREATE TABLE IF NOT EXISTS Restaurant(
    OrderID INTEGER PRIMARY KEY,
    Customer TEXT,
    Dish TEXT,
    Quantity INTEGER,
    BillAmount REAL
)
""")

cur.execute("DELETE FROM Restaurant")

# Insert at least 6 records
data = [
    (1, "Amit", "Pizza", 2, 500),
    (2, "Neha", "Burger", 4, 600),
    (3, "Raj", "Pasta", 3, 450),
    (4, "Kiran", "Sandwich", 5, 750),
    (5, "Mehul", "Dosa", 2, 200),
    (6, "Ravi", "Pizza", 4, 1000)
]

cur.executemany(
    "INSERT INTO Restaurant VALUES (?, ?, ?, ?, ?)", data
)
con.commit()

# 1. Export table data to restaurant.xlsx
cur.execute("SELECT * FROM Restaurant")
rows = cur.fetchall()

with open("restaurant.xlsx", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["OrderID", "Customer", "Dish", "Quantity", "BillAmount"]
    )
    writer.writerows(rows)

print("Data exported to restaurant.xlsx")

# 2. Display orders where Quantity > 3
print("\nOrders where Quantity > 3:")

cur.execute("SELECT * FROM Restaurant WHERE Quantity > 3")

for row in cur.fetchall():
    print(row)

# 3. Drop Restaurant table
cur.execute("DROP TABLE Restaurant")
con.commit()

print("\nRestaurant table dropped")

# 4. Import CSV data into Restaurant_New
with open("restaurant.xlsx", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    imported_data = list(reader)

cur.execute("""
CREATE TABLE IF NOT EXISTS Restaurant_New(
    OrderID INTEGER PRIMARY KEY,
    Customer TEXT,
    Dish TEXT,
    Quantity INTEGER,
    BillAmount REAL
)
""")

cur.execute("DELETE FROM Restaurant_New")

cur.executemany(
    "INSERT INTO Restaurant_New VALUES (?, ?, ?, ?, ?)",
    [
        (int(r[0]), r[1], r[2], int(r[3]), float(r[4]))
        for r in imported_data
    ]
)
con.commit()

print("\nData imported into Restaurant_New:")

cur.execute("SELECT * FROM Restaurant_New")

for row in cur.fetchall():
    print(row)

con.close()

# OUTPUT:
# Data exported to restaurant.xlsx
#
# Orders where Quantity > 3:
# (2, 'Neha', 'Burger', 4, 600.0)
# (4, 'Kiran', 'Sandwich', 5, 750.0)
# (6, 'Ravi', 'Pizza', 4, 1000.0)
#
# Restaurant table dropped
# Data imported into Restaurant_New
# All 6 records are displayed.