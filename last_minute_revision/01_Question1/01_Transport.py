import sqlite3
import matplotlib.pyplot as plt

#connect to db
con = sqlite3.connect("Transport.db")
cur=con.cursor()

#create Transport table
cur.execute("""
create table if not exists Transport(
    VehicleID integer primary key,
    VehicleType text,
    DriverName text,
    Route text,
    Charges real
)
""")

#Insert 8 Records
data=[
    (1,"Bus","Raj","Route-A",2000),
    (2,"Car","Amit","Route-B",1500),
    (3,"Bus","Rahul","Route-A",2500),
    (4,"Van","Karan","Route-C",1800),
    (5,"Bus","Jay","Route-B",2200),
    (6,"Car","Vijay","Route-A",1600),
    (7,"Van","Ravi","Route-A",1900),
    (8,"Bus","Mihir","Route-C",2300)
]

cur.executemany("""
    insert or ignore into Transport
    (VehicleID, VehicleType, DriverName,Route,Charges) values(?,?,?,?,?)
""",data)

con.commit()

#1.Display all vehicles operating on "Route-A"
print("Vehicles operating on Route-A:")

cur.execute("select*from Transport where Route='Route-A'")

for row in cur.fetchall():
    print(row)

#2.Update Charges by +500 for all "Bus" VehicleType.
cur.execute("""
    update Transport set Charges=Charges+500 where VehicleType='Bus'
""")

con.commit()

print("\nCharges updated for all Bus Vehicles.")

#3.Display Updated Records
print("\nUpdated Transport Records:")

cur.execute("select*from Transport")

for row in cur.fetchall():
    print(row)

#4.Prepare data for the pie chart                                                                                                                                                                                     
cur.execute("""
    select VehicleType,SUM(Charges) from transport group by VehicleType
""")

result=cur.fetchall()

vehicle_types=[row[0] for row in result]
charges=[row[1] for row in result]

#5.Draw Pie chart
plt.pie(charges,labels=vehicle_types,autopct='%1.1f%%')
plt.title("Charges Distribution by VehicleType")
plt.show()

con.close()