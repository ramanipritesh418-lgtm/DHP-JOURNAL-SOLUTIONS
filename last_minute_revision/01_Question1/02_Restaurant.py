import sqlite3
import csv

# =================================================
# Q2: Restaurant
# =================================================

# Connect to database
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

# Insert 6 records
data = [
    (1, "Rahul", "Pizza", 2, 400),
    (2, "Amit", "Burger", 4, 600),
    (3, "Jay", "Pasta", 3, 450),
    (4, "Raj", "Sandwich", 5, 500),
    (5, "Karan", "Pizza", 6, 1200),
    (6, "Vijay", "Biryani", 2, 300)
]

cur.executemany("""
INSERT OR IGNORE INTO Restaurant
(OrderID, Customer, Dish, Quantity, BillAmount)
VALUES (?, ?, ?, ?, ?)
""", data)

con.commit()

print("Restaurant table created and 6 records inserted.")

# -------------------------------------------------
# 1. Export Restaurant table into CSV
# -------------------------------------------------

cur.execute("SELECT * FROM Restaurant")

rows = cur.fetchall()

with open("restaurant.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Write column headings
    writer.writerow([
        "OrderID",
        "Customer",
        "Dish",
        "Quantity",
        "BillAmount"
    ])

    # Write records
    writer.writerows(rows)

print("\nRestaurant table exported to restaurant.csv")

# -------------------------------------------------
# 2. Retrieve orders where Quantity > 3
# -------------------------------------------------

print("\nOrders where Quantity > 3:")

cur.execute("""
SELECT * FROM Restaurant
WHERE Quantity > 3
""")

for row in cur.fetchall():
    print(row)

# -------------------------------------------------
# 3. Drop Restaurant table
# -------------------------------------------------

cur.execute("DROP TABLE Restaurant")

con.commit()

print("\nRestaurant table dropped successfully.")

# -------------------------------------------------
# 4. Import CSV data into Restaurant_New
# -------------------------------------------------

cur.execute("""
CREATE TABLE Restaurant_New(
    OrderID INTEGER PRIMARY KEY,
    Customer TEXT,
    Dish TEXT,
    Quantity INTEGER,
    BillAmount REAL
)
""")

# Read CSV file
with open("restaurant.csv", "r") as file:

    reader = csv.reader(file)

    # Skip column headings
    next(reader)

    # Insert CSV data into Restaurant_New
    for row in reader:

        cur.execute("""
        INSERT INTO Restaurant_New
        (OrderID, Customer, Dish, Quantity, BillAmount)
        VALUES (?, ?, ?, ?, ?)
        """, row)

con.commit()

print("\nCSV data imported into Restaurant_New successfully.")

# Display Restaurant_New records
print("\nRestaurant_New Records:")

cur.execute("SELECT * FROM Restaurant_New")

for row in cur.fetchall():
    print(row)

# Close database
con.close()


# =================================================
# OUTPUT
# =================================================
#
# Restaurant table created and 6 records inserted.
#
# Restaurant table exported to restaurant.csv
#
# Orders where Quantity > 3:
# (2, 'Amit', 'Burger', 4, 600.0)
# (4, 'Raj', 'Sandwich', 5, 500.0)
# (5, 'Karan', 'Pizza', 6, 1200.0)
#
# Restaurant table dropped successfully.
#
# CSV data imported into Restaurant_New successfully.
#
# Restaurant_New Records:
# (1, 'Rahul', 'Pizza', 2, 400.0)
# (2, 'Amit', 'Burger', 4, 600.0)
# (3, 'Jay', 'Pasta', 3, 450.0)
# (4, 'Raj', 'Sandwich', 5, 500.0)
# (5, 'Karan', 'Pizza', 6, 1200.0)
# (6, 'Vijay', 'Biryani', 2, 300.0)
# =================================================