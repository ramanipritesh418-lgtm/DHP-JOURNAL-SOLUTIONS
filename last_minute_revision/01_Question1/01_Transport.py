import sqlite3
import matplotlib.pyplot as plt

# =================================================
# Q1: Transport
# =================================================

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

# Insert 8 records
data = [
    (1, "Bus", "Raj", "Route-A", 2000),
    (2, "Car", "Amit", "Route-B", 1500),
    (3, "Bus", "Rahul", "Route-A", 2500),
    (4, "Van", "Karan", "Route-C", 1800),
    (5, "Bus", "Jay", "Route-B", 2200),
    (6, "Car", "Vijay", "Route-A", 1600),
    (7, "Van", "Ravi", "Route-A", 1900),
    (8, "Bus", "Mihir", "Route-C", 2300)
]

cur.executemany("""
INSERT OR IGNORE INTO Transport
(VehicleID, VehicleType, DriverName, Route, Charges)
VALUES (?, ?, ?, ?, ?)
""", data)

con.commit()

print("8 records inserted successfully.")

# -------------------------------------------------
# 1. Display vehicles operating on Route-A
# -------------------------------------------------

print("\nVehicles operating on Route-A:")

cur.execute("""
SELECT * FROM Transport
WHERE Route = 'Route-A'
""")

for row in cur.fetchall():
    print(row)

# -------------------------------------------------
# 2. Update Charges by +500 for all Bus
# -------------------------------------------------

cur.execute("""
UPDATE Transport
SET Charges = Charges + 500
WHERE VehicleType = 'Bus'
""")

con.commit()

print("\nCharges updated by +500 for all Bus vehicles.")

# Display updated records
print("\nUpdated Transport Records:")

cur.execute("SELECT * FROM Transport")

for row in cur.fetchall():
    print(row)

# -------------------------------------------------
# 3. Prepare data for Pie Chart
# -------------------------------------------------

cur.execute("""
SELECT VehicleType, SUM(Charges)
FROM Transport
GROUP BY VehicleType
""")

result = cur.fetchall()

vehicle_types = [row[0] for row in result]
charges = [row[1] for row in result]

# -------------------------------------------------
# 4. Draw Pie Chart
# -------------------------------------------------

plt.pie(
    charges,
    labels=vehicle_types,
    autopct='%1.1f%%'
)

plt.title("Charges Distribution by VehicleType")
plt.show()

# Close database
con.close()


# =================================================
# OUTPUT
# =================================================
#
# 8 records inserted successfully.
#
# Vehicles operating on Route-A:
# (1, 'Bus', 'Raj', 'Route-A', 2000.0)
# (3, 'Bus', 'Rahul', 'Route-A', 2500.0)
# (6, 'Car', 'Vijay', 'Route-A', 1600.0)
# (7, 'Van', 'Ravi', 'Route-A', 1900.0)
#
# Charges updated by +500 for all Bus vehicles.
#
# Updated Transport Records:
# (1, 'Bus', 'Raj', 'Route-A', 2500.0)
# (2, 'Car', 'Amit', 'Route-B', 1500.0)
# (3, 'Bus', 'Rahul', 'Route-A', 3000.0)
# (4, 'Van', 'Karan', 'Route-C', 1800.0)
# (5, 'Bus', 'Jay', 'Route-B', 2700.0)
# (6, 'Car', 'Vijay', 'Route-A', 1600.0)
# (7, 'Van', 'Ravi', 'Route-A', 1900.0)
# (8, 'Bus', 'Mihir', 'Route-C', 2800.0)
#
# Pie Chart will be displayed.
# =================================================