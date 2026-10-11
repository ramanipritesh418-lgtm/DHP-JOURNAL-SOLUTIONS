import sqlite3
import matplotlib.pyplot as plt

con=sqlite3.connect("Orders.db")
cur=con.cursor()

cur.execute("""
    create table if not exists Orders(
        OrderId integer primary key,
        CustomerName text,
        Product text,
        Quantity integer,
        Amount real
    )
""")

con.commit()

print("table created")

data=[
    (1,"Amit","Laptop",1,45000),
    (2,"Neha","Mobile",2,18000),
    (3,"Raj","Keyboard",3,2500),
    (4,"Priya","Monitor",2,12000),
    (5,"Amit","Mouse",2,1500),
    (6,"Karan","Printer",1,8000),
    (7,"Neha","Tablet",3,15000),
    (8,"Raj","Headphones",1,6000),
    (9,"Priya","Laptop Bag",2,3000),
    (10,"Karan","Mobile",2,22000)
    ]



cur.executemany("""
    insert into Orders
    (OrderId,CustomerName,Product,Quantity,Amount)
    values(?,?,?,?,?)
""",data)

con.commit()

print("10 records:")

cur.execute("select*from Orders")

for row in cur.fetchall():
    print(row)


#Display all orders whose Amount is greater than 5000.
cur.execute("select*from Orders where amount >5000")
for row in cur.fetchall():
    print(row)

cur.execute("delete from Orders where Quantity < 2")
con.commit()

print("After deletion:")
cur.execute("select*from orders")

for row in cur.fetchall():
    print(row)



# Calculate total Amount spent by each Customer
cur.execute("""
    SELECT CustomerName, SUM(Amount)
    FROM Orders
    GROUP BY CustomerName
""")

data = cur.fetchall()

# Store customer names and total amounts
customers = []
amounts = []

for row in data:
    customers.append(row[0])
    amounts.append(row[1])

# Draw line chart
plt.plot(customers, amounts, marker="o")

# Add chart title and labels
plt.title("Amount Spent by Each Customer")
plt.xlabel("Customer Name")
plt.ylabel("Total Amount")

# Display grid and chart
plt.grid(True)
plt.show()

# Close database connection
con.close()


