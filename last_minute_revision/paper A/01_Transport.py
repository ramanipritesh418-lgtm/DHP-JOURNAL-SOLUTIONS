# ============================================================
# B.C.A. Sem-III Examination December 2025
# Subject: 303 - Database Handling Using Python (PR)
# Paper A - Question 1 (10 Marks)
#
# QUESTION:
# 1. Create Transport(VehicleID, VehicleType, DriverName,
#    Route, Charges).
# 2. Insert at least 8 records.
# 3. Display vehicles operating on Route-A.
# 4. Increase Charges by 500 for all Bus vehicles.
# 5. Draw a pie chart showing Charges distribution
#    by VehicleType.
#
# CONCEPT:
# 1. sqlite3.connect() creates/connects to a database.
# 2. CREATE TABLE creates a table.
# 3. executemany() inserts multiple records.
# 4. SELECT with WHERE filters Route-A vehicles.
# 5. UPDATE changes Bus charges using Charges + 500.
# 6. GROUP BY VehicleType calculates total charges
#    for each vehicle type.
# 7. matplotlib.pyplot.pie() draws a pie chart.
# ============================================================

import sqlite3
import matplotlib.pyplot as plt

# Connect to database
con = sqlite3.connect("Transport.db")
cur = con.cursor()

# Create Transport table
cur.execute("""
CREATE TABLE IF NOT EXISTS Transport(
    VehicleID INTEGER PRIMARY KEY,
    VehicleType TEXT,
    DriverName TEXT,
    Route TEXT,
    Charges REAL
)
""")

# Remove old records before inserting sample data again
cur.execute("DELETE FROM Transport")

# Insert at least 8 records
data = [
    (1, "Bus", "Amit", "Route-A", 2000),
    (2, "Car", "Raj", "Route-B", 1000),
    (3, "Bus", "Neha", "Route-A", 2500),
    (4, "Van", "Kiran", "Route-C", 1500),
    (5, "Car", "Mehul", "Route-A", 1200),
    (6, "Bus", "Jay", "Route-B", 2200),
    (7, "Van", "Ravi", "Route-A", 1800),
    (8, "Car", "Nita", "Route-C", 1300)
]

cur.executemany(
    "INSERT INTO Transport VALUES (?, ?, ?, ?, ?)", data
)
con.commit()

# Display vehicles operating on Route-A
print("Vehicles operating on Route-A:")

cur.execute("SELECT * FROM Transport WHERE Route = 'Route-A'")

for row in cur.fetchall():
    print(row)

# Increase charges by 500 for all Bus vehicles
cur.execute("""
UPDATE Transport
SET Charges = Charges + 500
WHERE VehicleType = 'Bus'
""")
con.commit()

print("\nRecords after updating Bus charges:")

cur.execute("SELECT * FROM Transport")

for row in cur.fetchall():
    print(row)

# Draw pie chart of total charges by VehicleType
cur.execute("""
SELECT VehicleType, SUM(Charges)
FROM Transport
GROUP BY VehicleType
""")

result = cur.fetchall()

vehicle_types = [row[0] for row in result]
charges = [row[1] for row in result]

plt.pie(charges, labels=vehicle_types, autopct="%1.1f%%")
plt.title("Charges Distribution by Vehicle Type")
plt.show()

con.close()

# OUTPUT:
# Vehicles operating on Route-A:
# (1, 'Bus', 'Amit', 'Route-A', 2000.0)
# (3, 'Bus', 'Neha', 'Route-A', 2500.0)
# (5, 'Car', 'Mehul', 'Route-A', 1200.0)
# (7, 'Van', 'Ravi', 'Route-A', 1800.0)
#
# After update, Bus charges become:
# Amit  = 2500
# Neha  = 3000
# Jay   = 2700
#
# Pie chart displays the charge distribution by vehicle type.
