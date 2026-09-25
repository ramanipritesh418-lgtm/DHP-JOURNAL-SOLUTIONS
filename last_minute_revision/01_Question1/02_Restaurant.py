import sqlite3
import csv

#connect to db
con=sqlite3.connect("Restaurant.db")
cur=con.cursor()

#create reataurant tb
cur.execute("""
    create table if not exists Restaurant(
        OrderID integer primary key, 
        Customer text,
        Dish text, 
        Quantity integer, 
        BillAmount real
    )
""")

#insert 6 records
data=[
    (1,"Rahul","Pizza",2,400),
    (2,"Amit","Burger",4,600),
    (3,"Jay","Pasta",3,450),
    (4,"Raj","Sandwich",5,500),
    (5,"Karan","Pizza",6,1200),
    (6,"Vijay","Biryani",2,300)
]

cur.executemany("""
    insert or ignore into restaurant(OrderID, Customer, Dish, Quantity, BillAmount)
    values(?,?,?,?,?)
""",data)

con.commit()

print("Restaurant Table created and 6 records inserted.")

#Display all records
cur.execute("select*from Restaurant")

for row in cur.fetchall():
    print(row)

# Export restaurant table into CSV file

cur.execute("select*from Restaurant")

rows=cur.fetchall()

with open("restaurant.csv","w",newline="") as file:
    writer=csv.writer(file)

    #write column headings
    writer.writerow(["OrderID", "Customer", "Dish", "Quantity", "BillAmount"])

    #write records
    writer.writerows(rows)

print("\nRestaurant table exported to restaurant.csv")

#Display orders where Quantity > 3

print("\nOrders where Quantity>3:")

cur.execute("""
    select*from restaurant where Quantity>3
""")

for row in cur.fetchall():
    print(row)

# 3. Drop the table Restaurant.
cur.execute("drop table Restaurant")
con.commit()

print("\nRestaurant table dropped successfully.")


# create new Restaurant_New table
cur.execute("""
    create table Restaurant_New(
        OrderID integer primary key, 
        Customer text,
        Dish text, 
        Quantity integer, 
        BillAmount real
    )
""")

#Read data from csv file

with open("restaurant.csv","r") as file:
    reader=csv.reader(file)

    #skip heading
    next(reader)

    #insert csv data into Restaurant_New
    for row in reader:
        cur.execute("""
            insert into Restaurant_New
            (OrderID, Customer, Dish, Quantity, BillAmount)
            values(?,?,?,?,?)
        """,row)

con.commit()

print("\nCSV data imported into Restaurant_New successfully.")

#display Restaurant_New records

cur.execute("select*from Restaurant_New")

for row in cur.fetchall():
    print(row)

#close db
con.close()