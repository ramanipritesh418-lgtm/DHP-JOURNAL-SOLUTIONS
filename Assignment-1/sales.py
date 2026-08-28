import sqlite3
import csv
con=sqlite3.connect("Sales.db")

cursor=con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales(
    sid INTEGER PRIMARY KEY,
    year INTEGER,
    totalsales REAL
)
""")

data=[
    (1,2021,50000),
    (2,2022,65000),
    (3,2023,72000),
    (4,2024,85000),
    (5,2025,95000),
    (6,2021,55000),
    (7,2022,68000),
    (8,2023,75000),
    (9,2024,88000),
    (10,2025,99000)
    ]

cursor.executemany(
    "INSERT INTO Sales VALUES(?,?,?)",
data
)

con.commit()

cursor.execute("SELECT*FROM Sales")

records=cursor.fetchall()

for row in records:
    print(row)


cursor.execute("SELECT*FROM Sales")
records=cursor.fetchall()

with open("sales.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["sid","year","totalsales"])
    writer.writerows(records)    
    
with open("sales.csv","r")as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)








    
    
