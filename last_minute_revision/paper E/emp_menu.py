# ============================================================
# DHP 303 - Database Handling Using Python (PR)
# B.C.A. Semester III - December 2025
#
# QUESTION 2:
# Write a menu-driven Python script to perform the following:
#
# 1. Display the details of Sales department.
# 2. Display details of employee whose emp_id is 105.
#
# ============================================================
# CONCEPT:
# Menu-driven program - Uses a menu to select an operation.
# while loop          - Repeats the menu.
# if-elif-else        - Executes the selected operation.
# WHERE               - Filters database records.
# ============================================================

import sqlite3

# Connect to the same database created in Question 1
con = sqlite3.connect("Employee.db")
cur = con.cursor()

# Display menu until the user exits
while True:

    print("\n----- EMPLOYEE MENU -----")
    print("1. Display Sales Department Details")
    print("2. Display Employee with emp_id 105")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Option 1: Display Sales department employees
    if choice == "1":

        print("\nSales Department Details:")

        cur.execute("""
            SELECT * FROM Employee
            WHERE department_name = 'Sales'
        """)

        rows = cur.fetchall()

        for row in rows:
            print(row)

    # Option 2: Display employee with emp_id 105
    elif choice == "2":

        print("\nEmployee Details for emp_id 105:")

        cur.execute("""
            SELECT * FROM Employee
            WHERE emp_id = 105
        """)

        rows = cur.fetchall()

        for row in rows:
            print(row)

    # Option 3: Exit the program
    elif choice == "3":

        print("Program ended.")
        break

    # Invalid menu choice
    else:
        print("Invalid choice! Please try again.")

# Close database connection
con.close()

# ============================================================
# EXPECTED OUTPUT:
#
# ----- EMPLOYEE MENU -----
# 1. Display Sales Department Details
# 2. Display Employee with emp_id 105
# 3. Exit
# Enter your choice: 1
#
# Sales Department Details:
# (101, 'Amit', '9876543210', 'Sales', '2023-01-15')
# (104, 'Priya', '9876543213', 'Sales', '2023-04-12')
# (106, 'Riya', '9876543215', 'Sales', '2023-06-18')
# (110, 'Meera', '9876543219', 'Sales', '2023-10-25')
#
# Enter your choice: 2
#
# Employee Details for emp_id 105:
# (105, 'Karan', '9876543214', 'Finance', '2023-05-20')
#
# Enter your choice: 3
# Program ended.
#
# ============================================================
# EXPLANATION:
#
# 1. The menu displays three choices.
# 2. Choice 1 selects employees from the Sales department.
# 3. Choice 2 selects the employee with emp_id 105.
# 4. Choice 3 ends the loop and exits the program.
# 5. Invalid choices display an error message.
#
# ============================================================