# ============================================================
# DHP PRACTICAL - PAPER H
# Q.1 Write a Python script to perform the following:
# 1. Create Sales table and insert at least 10 records.
# 2. Display North region sales.
# 3. Add 1000 to Revenue where Quantity > 20.
# 4. Draw bar chart of total Revenue by Region.
# ============================================================

# CONCEPT:
# SQLite is used to store data in database tables.
# Matplotlib is used to draw charts.
#
# Sales Table:
# SalesID, Item, Region, Quantity, Revenue
# ============================================================

import sqlite3
import matplotlib.pyplot as plt

# Connect to database
con = sqlite3.connect("Sales.db")
cur = con.cursor()

# ------------------------------------------------------------
# 1. CREATE SALES TABLE
# ------------------------------------------------------------

cur.execute("""
    CREATE TABLE IF NOT EXISTS Sales(
        SalesID INTEGER PRIMARY KEY,
        Item TEXT,
        Region TEXT,
        Quantity INTEGER,
        Revenue REAL
    )
""")

# ------------------------------------------------------------
# 2. INSERT 10 RECORDS
# ------------------------------------------------------------

cur.execute("SELECT COUNT(*) FROM Sales")

if cur.fetchone()[0] == 0:
    data = [
        (1, 'Laptop', 'North', 25, 50000),
        (2, 'Mobile', 'South', 15, 30000),
        (3, 'Tablet', 'East', 30, 40000),
        (4, 'Keyboard', 'West', 10, 5000),
        (5, 'Mouse', 'North', 22, 3000),
        (6, 'Monitor', 'South', 28, 20000),
        (7, 'Printer', 'East', 18, 12000),
        (8, 'Laptop', 'West', 35, 60000),
        (9, 'Mobile', 'North', 12, 25000),
        (10, 'Tablet', 'South', 24, 35000)
    ]

    cur.executemany("""
        INSERT INTO Sales
        VALUES(?,?,?,?,?)
    """, data)

    con.commit()
    print("10 Records Inserted Successfully.")

# ------------------------------------------------------------
# 3. DISPLAY NORTH REGION SALES
# ------------------------------------------------------------

print("\nSales in North Region:")

cur.execute("""
    SELECT * FROM Sales
    WHERE Region = 'North'
""")

for row in cur.fetchall():
    print(row)

# ------------------------------------------------------------
# 4. UPDATE REVENUE WHERE QUANTITY > 20
# ------------------------------------------------------------

cur.execute("""
    UPDATE Sales
    SET Revenue = Revenue + 1000
    WHERE Quantity > 20
""")

con.commit()

print("\nRevenue Updated Successfully.")

# ------------------------------------------------------------
# 5. DISPLAY ALL SALES RECORDS
# ------------------------------------------------------------

print("\nAll Sales Records:")

cur.execute("SELECT * FROM Sales")

for row in cur.fetchall():
    print(row)

# ------------------------------------------------------------
# 6. CALCULATE TOTAL REVENUE BY REGION
# ------------------------------------------------------------

cur.execute("""
    SELECT Region, SUM(Revenue)
    FROM Sales
    GROUP BY Region
""")

result = cur.fetchall()

regions = [row[0] for row in result]
revenues = [row[1] for row in result]

# ------------------------------------------------------------
# 7. DRAW BAR CHART
# ------------------------------------------------------------

plt.bar(regions, revenues)
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.title("Total Revenue by Region")
plt.show()

con.close()

# ============================================================
# OUTPUT:
# ============================================================
#
# 10 Records Inserted Successfully.
#
# Sales in North Region:
# (1, 'Laptop', 'North', 25, 50000.0)
# (5, 'Mouse', 'North', 22, 3000.0)
# (9, 'Mobile', 'North', 12, 25000.0)
#
# Revenue Updated Successfully.
#
# All Sales Records:
# (1, 'Laptop', 'North', 25, 51000.0)
# (2, 'Mobile', 'South', 15, 30000.0)
# (3, 'Tablet', 'East', 30, 41000.0)
# (4, 'Keyboard', 'West', 10, 5000.0)
# (5, 'Mouse', 'North', 22, 4000.0)
# (6, 'Monitor', 'South', 28, 21000.0)
# (7, 'Printer', 'East', 18, 12000.0)
# (8, 'Laptop', 'West', 35, 61000.0)
# (9, 'Mobile', 'North', 12, 25000.0)
# (10, 'Tablet', 'South', 24, 36000.0)
#
# A bar chart displays total Revenue by Region.
#
# ============================================================
# EXPLANATION:
# ============================================================
#
# 1. sqlite3.connect() connects to the database.
# 2. CREATE TABLE creates the Sales table.
# 3. executemany() inserts multiple records.
# 4. WHERE Region = 'North' displays North region sales.
# 5. UPDATE adds 1000 to Revenue where Quantity > 20.
# 6. GROUP BY Region groups records by region.
# 7. SUM(Revenue) calculates total Revenue.
# 8. plt.bar() draws the bar chart.
# 9. commit() saves database changes.
#
# NOTE:
# Run this program once with a fresh database to match
# the output shown above. Running it again updates Revenue
# by another 1000 for qualifying records.
# ============================================================
