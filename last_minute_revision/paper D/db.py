# ============================================================
# DHP 303 - Database Handling Using Python (PR)
# B.C.A. Semester III - December 2025
#
# QUESTION 1:
# A. Create the following tables:
#    1. Cust_Master(Cid, CName, ContactNo, City)
#    2. Prod_Master(Pid, PName, Company, Price, Qty)
#
# B. Create a Python program to display data of Prod_Master.
#
# ============================================================
# CONCEPT:
# sqlite3       - Connects Python to SQLite database.
# CREATE TABLE  - Creates database tables.
# INSERT        - Inserts records.
# SELECT        - Retrieves records.
# fetchall()    - Fetches all records.
# ============================================================

import sqlite3

# Connect to database
con = sqlite3.connect("Company.db")
cur = con.cursor()

# Step 1: Create Cust_Master table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Cust_Master (
        Cid INTEGER PRIMARY KEY,
        CName TEXT,
        ContactNo TEXT,
        City TEXT
    )
""")

# Step 2: Create Prod_Master table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Prod_Master (
        Pid INTEGER PRIMARY KEY,
        PName TEXT,
        Company TEXT,
        Price REAL,
        Qty INTEGER
    )
""")

con.commit()

print("Database and tables created successfully!")

# Step 3: Insert sample customer records
customers = [
    (1, "Amit", "9876543210", "Surat"),
    (2, "Neha", "9876543211", "Ahmedabad"),
    (3, "Raj", "9876543212", "Vadodara")
]

cur.executemany("""
    INSERT OR IGNORE INTO Cust_Master
    (Cid, CName, ContactNo, City)
    VALUES (?, ?, ?, ?)
""", customers)

# Step 4: Insert sample product records
products = [
    (101, "Laptop", "Dell", 45000, 10),
    (102, "Mouse", "HP", 500, 25),
    (103, "Keyboard", "Logitech", 1200, 15),
    (104, "Monitor", "Samsung", 12000, 8),
    (105, "Printer", "Canon", 8000, 5)
]

cur.executemany("""
    INSERT OR IGNORE INTO Prod_Master
    (Pid, PName, Company, Price, Qty)
    VALUES (?, ?, ?, ?, ?)
""", products)

con.commit()

print("Sample records inserted successfully!")

# Step 5: Display Prod_Master table records
print("\nProduct Master Details:")

cur.execute("SELECT * FROM Prod_Master")

for row in cur.fetchall():
    print(row)

# Close database connection
con.close()

# ============================================================
# EXPECTED OUTPUT:
#
# Database and tables created successfully!
# Sample records inserted successfully!
#
# Product Master Details:
# (101, 'Laptop', 'Dell', 45000.0, 10)
# (102, 'Mouse', 'HP', 500.0, 25)
# (103, 'Keyboard', 'Logitech', 1200.0, 15)
# (104, 'Monitor', 'Samsung', 12000.0, 8)
# (105, 'Printer', 'Canon', 8000.0, 5)
#
# ============================================================
# EXPLANATION:
#
# 1. connect() creates or opens Company.db.
# 2. CREATE TABLE creates Cust_Master and Prod_Master.
# 3. executemany() inserts sample records into both tables.
# 4. SELECT * retrieves all product records.
# 5. fetchall() returns the records for display.
#
# ============================================================
