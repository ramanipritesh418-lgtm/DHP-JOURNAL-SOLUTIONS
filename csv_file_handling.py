# ============================================================
#                 CSV FILE HANDLING IN PYTHON
# ============================================================
#
# 📚 THEORY:
# CSV stands for Comma-Separated Values.
# A CSV file is used to store data in rows and columns.
#
# Python provides a built-in "csv" module to create,
# read and write CSV files easily.
#
# Main CSV concepts:
# 1. csv.writer()
# 2. writerow()
# 3. writerows()
# 4. csv.reader()
# 5. DictWriter
# 6. writeheader()
# 7. DictReader
# 8. close()
#
# ============================================================


import csv


# ============================================================
# 1️⃣ csv.writer()
# ============================================================
#
# 📚 THEORY:
# csv.writer() is used to create a writer object.
# It helps us write data into a CSV file.
#
# Syntax:
# csv.writer(file)
#
# ============================================================


file = open("students.csv", "w", newline="")

writer = csv.writer(file)

print("Creating students.csv...")


# ============================================================
# 2️⃣ writerow()
# ============================================================
#
# 📚 THEORY:
# writerow() is used to write ONE row into a CSV file.
#
# Syntax:
# writer.writerow(data)
#
# ============================================================


writer.writerow(["Name", "Age", "City"])

print("Header written successfully!")

writer.writerow(["Pritesh", 19, "Surat"])

print("One record written successfully!")


# ============================================================
# 3️⃣ writerows()
# ============================================================
#
# 📚 THEORY:
# writerows() is used to write MULTIPLE rows at once.
#
# Syntax:
# writer.writerows(data)
#
# ============================================================


data = [
    ["Rahul", 20, "Ahmedabad"],
    ["Amit", 21, "Vadodara"],
    ["Neha", 19, "Rajkot"]
]

writer.writerows(data)

print("Multiple records written successfully!")


# ============================================================
# 4️⃣ close()
# ============================================================
#
# 📚 THEORY:
# close() is used to close the opened CSV file.
# It releases the file resources.
#
# Syntax:
# file.close()
#
# ============================================================


file.close()

print("CSV file closed successfully!")


# ------------------------- OUTPUT ----------------------------
#
# Creating students.csv...
# Header written successfully!
# One record written successfully!
# Multiple records written successfully!
# CSV file closed successfully!
#
# -------------------------------------------------------------


# ============================================================
# 5️⃣ csv.reader()
# ============================================================
#
# 📚 THEORY:
# csv.reader() is used to read data from a CSV file.
# It reads the file row by row.
#
# Each row is returned as a LIST.
#
# Syntax:
# csv.reader(file)
#
# ============================================================


print("\n========== USING csv.reader() ==========")

file = open("students.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row)

file.close()


# ------------------------- OUTPUT ----------------------------
#
# ========== USING csv.reader() ==========
# ['Name', 'Age', 'City']
# ['Pritesh', '19', 'Surat']
# ['Rahul', '20', 'Ahmedabad']
# ['Amit', '21', 'Vadodara']
# ['Neha', '19', 'Rajkot']
#
# -------------------------------------------------------------


# ============================================================
# 6️⃣ DictReader
# ============================================================
#
# 📚 THEORY:
# DictReader reads each CSV row as a DICTIONARY.
#
# The first row is normally used as column names.
#
# This allows us to access data using column names.
#
# Example:
# row["Name"]
# row["Age"]
# row["City"]
#
# Syntax:
# csv.DictReader(file)
#
# ============================================================


print("\n========== USING DictReader ==========")

file = open("students.csv", "r")

reader = csv.DictReader(file)

for row in reader:
    print(
        "Name:", row["Name"],
        "| Age:", row["Age"],
        "| City:", row["City"]
    )

file.close()


# ------------------------- OUTPUT ----------------------------
#
# ========== USING DictReader ==========
# Name: Pritesh | Age: 19 | City: Surat
# Name: Rahul | Age: 20 | City: Ahmedabad
# Name: Amit | Age: 21 | City: Vadodara
# Name: Neha | Age: 19 | City: Rajkot
#
# -------------------------------------------------------------


# ============================================================
# 7️⃣ DictWriter
# ============================================================
#
# 📚 THEORY:
# DictWriter is used to write DICTIONARY data into a CSV file.
#
# It uses fieldnames to define the column names.
#
# Syntax:
# csv.DictWriter(file, fieldnames)
#
# ============================================================


print("\n========== USING DictWriter ==========")

file = open("employees.csv", "w", newline="")

fields = ["ID", "Name", "Department", "Salary"]

writer = csv.DictWriter(
    file,
    fieldnames=fields
)


# ============================================================
# 8️⃣ writeheader()
# ============================================================
#
# 📚 THEORY:
# writeheader() writes the field names (column headings)
# into the CSV file.
#
# ============================================================


writer.writeheader()

print("Employee header written successfully!")


# ============================================================
# 9️⃣ DictWriter + writerow()
# ============================================================
#
# 📚 THEORY:
# writerow() can also be used with DictWriter
# to write ONE dictionary record.
#
# ============================================================


writer.writerow({
    "ID": 101,
    "Name": "Pritesh",
    "Department": "IT",
    "Salary": 25000
})

print("One employee record written successfully!")


# ============================================================
# 🔟 DictWriter + writerows()
# ============================================================
#
# 📚 THEORY:
# writerows() can be used with DictWriter
# to write MULTIPLE dictionary records.
#
# ============================================================


employees = [
    {
        "ID": 102,
        "Name": "Rahul",
        "Department": "HR",
        "Salary": 28000
    },
    {
        "ID": 103,
        "Name": "Amit",
        "Department": "Sales",
        "Salary": 30000
    }
]

writer.writerows(employees)

print("Multiple employee records written successfully!")


# ============================================================
# 1️⃣1️⃣ Close Employee CSV File
# ============================================================
#
# 📚 THEORY:
# close() closes the CSV file after completing
# all writing operations.
#
# ============================================================


file.close()

print("Employee CSV file closed successfully!")


# ------------------------- OUTPUT ----------------------------
#
# ========== USING DictWriter ==========
# Employee header written successfully!
# One employee record written successfully!
# Multiple employee records written successfully!
# Employee CSV file closed successfully!
#
# -------------------------------------------------------------


# ============================================================
# 1️⃣2️⃣ Read Employee CSV using DictReader
# ============================================================
#
# 📚 THEORY:
# DictReader reads the employee CSV file.
# Each row is converted into a dictionary.
#
# We can access values using column names.
#
# ============================================================


print("\n========== READING EMPLOYEE CSV ==========")

file = open("employees.csv", "r")

reader = csv.DictReader(file)

for employee in reader:
    print(
        "ID:", employee["ID"],
        "| Name:", employee["Name"],
        "| Department:", employee["Department"],
        "| Salary:", employee["Salary"]
    )

file.close()


# ------------------------- OUTPUT ----------------------------
#
# ========== READING EMPLOYEE CSV ==========
# ID: 101 | Name: Pritesh | Department: IT | Salary: 25000
# ID: 102 | Name: Rahul | Department: HR | Salary: 28000
# ID: 103 | Name: Amit | Department: Sales | Salary: 30000
#
# -------------------------------------------------------------


# ============================================================
# 🧠 QUICK REVISION
# ============================================================
#
# csv.writer()  → Creates writer object
# writerow()    → Writes one row
# writerows()   → Writes multiple rows
# csv.reader()  → Reads CSV rows as lists
# DictReader    → Reads CSV rows as dictionaries
# DictWriter    → Writes dictionary data
# writeheader() → Writes column headings
# close()       → Closes the CSV file
#
# ============================================================


print("\nCSV File Handling completed successfully! ✅")


# ------------------------- FINAL OUTPUT ----------------------
#
# CSV File Handling completed successfully! ✅
#
# ============================================================
#                     END OF PROGRAM
# ============================================================
