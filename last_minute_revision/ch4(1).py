# ================================================================
# 📘 UNIT 4 - PYTHON INTERACTION WITH TEXT AND CSV
# ================================================================
# 📁 File Handling + 📊 CSV Handling
#
# This code sheet covers:
# 1. open()
# 2. File Access Modes
# 3. close()
# 4. try...finally
# 5. write()
# 6. read()
# 7. readline()
# 8. readlines()
# 9. with statement
# 10. CSV File
# 11. csv module
# 12. Opening CSV File
# 13. csv.reader()
# 14. csv.writer()
# 15. writerow()
# 16. writerows()
# 17. DictReader()
# 18. DictWriter()
# 19. writeheader()
# 20. Closing CSV File
# ================================================================


# ================================================================
# 1️⃣ FILE HANDLING IN PYTHON 📁
# ================================================================
# File handling allows us to store data permanently inside a file.
#
# Python provides functions/methods to:
# 📖 Open a file
# ✏️ Read or write data
# 🔒 Close the file


# ================================================================
# 2️⃣ OPENING A FILE - open() 📂
# ================================================================
# open() is used to open a file.
#
# Syntax:
# file_object = open(file_name, access_mode, buffer_size)
#
# Example: Open a file for reading.

file_object = open("file.txt", "r")

print("📂 File is opened successfully")

file_object.close()


# ================================================================
# 3️⃣ FILE ACCESS MODES 🔑
# ================================================================
# r  -> Read 📖
# w  -> Write ✏️
# a  -> Append ➕
# r+ -> Read + Write 🔄
# w+ -> Write + Read 🔄
# a+ -> Append + Read 🔄
# rb -> Read Binary 📖
# wb -> Write Binary ✏️
# ab -> Append Binary ➕
# x  -> Create 🆕
#
# ⭐ Important:
# r  -> Read
# w  -> Write
# a  -> Append
# r+ -> Read + Write
# w+ -> Write + Read
# a+ -> Append + Read


# ================================================================
# 4️⃣ write() METHOD ✏️
# ================================================================
# write() is used to write data into a file.

f = open("file.txt", "w")

f.write("Hello Python")

f.close()

print("✏️ Data written successfully")


# ================================================================
# 5️⃣ read() METHOD 📖
# ================================================================
# read() reads complete data from the file.

f = open("file.txt", "r")

data = f.read()

print("\n📖 Output of read():")
print(data)

f.close()


# ================================================================
# 6️⃣ readline() METHOD 📄
# ================================================================
# readline() reads one line at a time.

f = open("file.txt", "w")

f.write("Hello Python\n")
f.write("Welcome to Unit 4\n")
f.write("File Handling")

f.close()


f = open("file.txt", "r")

print("\n📄 Output of readline():")

print(f.readline())

f.close()


# ================================================================
# 7️⃣ readlines() METHOD 📚
# ================================================================
# readlines() reads all lines from a file.
# It returns the lines as a list.

f = open("file.txt", "r")

data = f.readlines()

print("\n📚 Output of readlines():")

print(data)

f.close()


# ================================================================
# 8️⃣ close() METHOD 🔒
# ================================================================
# close() is used to close an opened file.
#
# Syntax:
# file_object.close()
#
# Why close a file?
# 🔹 It releases system resources.
# 🔹 It ensures that the file is properly closed.
# 🔹 Further operations cannot be performed after closing.

f = open("file.txt", "r")

print("\n🔓 File is opened successfully")

f.close()

print("🔒 File is closed successfully")


# ================================================================
# 9️⃣ try...finally WITH FILE HANDLING 🛡️
# ================================================================
# finally ensures that the file is closed
# even if an exception occurs.

file_object = open("file.txt", "r")

try:

    data = file_object.read()

    print("\n🛡️ try...finally output:")
    print(data)

finally:

    file_object.close()

    print("🔒 File closed using finally")


# ================================================================
# 🔟 with STATEMENT 📦
# ================================================================
# The with statement is useful for file handling.
#
# It automatically closes the file after the operation.
# Therefore, we do not need to manually write:
#
# f.close()

with open("file.txt", "r") as f:

    content = f.read()

    print("\n📦 Output using with statement:")
    print(content)


# ================================================================
# 1️⃣1️⃣ with STATEMENT - WRITING ✏️
# ================================================================
# Another example of using with for writing.

with open("college.txt", "w") as f:

    f.write("Hello College")

print("\n✏️ Data written using with statement")


# ================================================================
# 1️⃣2️⃣ CSV FILE 📊
# ================================================================
# CSV = Comma Separated Values
#
# A CSV file is a type of plain text file.
# It is used to store tabular data.
# Data is generally separated using a comma (,).
# Each line represents a record.
# The first line generally contains column/field names.
#
# Example:
#
# Name,Branch,Year,CGPA
# Rahul,COE,2,9.0
# Sandhya,COE,2,9.1
# Amit,IT,2,9.3


# ================================================================
# 1️⃣3️⃣ CSV MODULE 🐍📊
# ================================================================
# Python provides the csv module to work with CSV files.
#
# Important functions/classes:
#
# csv.reader()
# csv.writer()
# writerow()
# writerows()
# csv.DictReader()
# csv.DictWriter()

import csv


# ================================================================
# 1️⃣4️⃣ OPENING A CSV FILE 📂
# ================================================================
# A CSV file can be opened using Python's open() function.
#
# The opened file object is passed to csv.reader().

with open("example.csv", "w", newline="") as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow(["Name", "Branch", "Year", "CGPA"])
    writer.writerow(["Rahul", "COE", "2", "9.0"])
    writer.writerow(["Sandhya", "COE", "2", "9.1"])
    writer.writerow(["Amit", "IT", "2", "9.3"])


# ================================================================
# 1️⃣5️⃣ csv.reader() 📖
# ================================================================
# csv.reader() is used to read data from a CSV file.
#
# Syntax:
# csv.reader(csvfile, dialect='excel', **fmtparams)
#
# Each row returned by reader is a list.

with open("example.csv") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    print("\n📖 Reading CSV using csv.reader():")

    for row in csv_reader:

        print(row)


# ================================================================
# 1️⃣6️⃣ csv.writer() ✏️
# ================================================================
# csv.writer() is used to write data into a CSV file.
#
# Syntax:
# csv.writer(csvfile, dialect='excel', **optional_parameters)

with open("student.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(["SID", "NAME", "CLASS"])

    writer.writerow([101, "Sujay", "BBA"])
    writer.writerow([102, "Priti", "BCA"])
    writer.writerow([103, "Kavya", "BSc"])

print("\n✏️ Data write successfully!!!")


# ================================================================
# 1️⃣7️⃣ writerow() ✏️
# ================================================================
# writerow() is used to write ONE row at a time.
#
# Example:
# writer.writerow(["SID", "NAME", "CLASS"])
#
# Each row is written as a list.

with open("one_row.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(["SID", "NAME", "CLASS"])

    writer.writerow([101, "Sujay", "BBA"])


# ================================================================
# 1️⃣8️⃣ writerows() ✏️📋
# ================================================================
# writerows() is used to write MULTIPLE rows at once.

fieldnames = ["Name", "Branch", "Year", "CGPA"]

rows = [

    ["Mihir", "COE", "2", "9.0"],
    ["Sandhya", "COE", "2", "9.1"],
    ["Akshay", "IT", "2", "9.3"],
    ["Smit", "SE", "1", "9.5"],
    ["Parth", "MCE", "3", "7.8"],
    ["Sahil", "EP", "2", "9.1"]

]

filename = "student_records.csv"

with open(filename, "w", newline="") as csvfile:

    csvwriter = csv.writer(csvfile)

    # Write header row
    csvwriter.writerow(fieldnames)

    # Write multiple rows
    csvwriter.writerows(rows)

print("\n📋 Multiple rows written using writerows()")


# ================================================================
# 1️⃣9️⃣ DISPLAY CSV OUTPUT 📊
# ================================================================
# Reading the generated CSV file.

with open("student_records.csv", "r") as f:

    print("\n📊 student_records.csv:")

    print(f.read())


# ================================================================
# 2️⃣0️⃣ DictReader() 📖🗂️
# ================================================================
# DictReader() reads each row as a dictionary.
#
# The CSV column names become dictionary keys.
#
# Example:
# {
#     "Name": "Mihir",
#     "Branch": "COE",
#     "Year": "2",
#     "CGPA": "9.0"
# }

with open("student_records.csv") as csv_file:

    csv_reader = csv.DictReader(csv_file)

    print("\n🗂️ Reading CSV using DictReader():")

    for row in csv_reader:

        print(row)


# ================================================================
# 2️⃣1️⃣ DictReader() - ACCESS USING COLUMN NAMES 🗂️
# ================================================================
# Each row can be accessed using column names.

with open("student_records.csv") as csv_file:

    csv_reader = csv.DictReader(csv_file)

    print("\n🗂️ Accessing values using column names:")

    for row in csv_reader:

        print("Name   :", row["Name"])
        print("Branch :", row["Branch"])
        print("Year   :", row["Year"])
        print("CGPA   :", row["CGPA"])
        print("------------------------")


# ================================================================
# 2️⃣2️⃣ DictWriter() ✏️🗂️
# ================================================================
# DictWriter() writes dictionary data into a CSV file.
#
# Important parameters:
#
# csvfile      -> file object having write() method
# fieldnames   -> keys that identify the columns
# restval      -> value written when a key is missing
# extrasaction -> action for extra keys
# dialect      -> type of dialect used

student_data = [

    {
        "Name": "Mihir",
        "Branch": "COE",
        "Year": "2",
        "CGPA": "9.0"
    },

    {
        "Name": "Sandhya",
        "Branch": "COE",
        "Year": "2",
        "CGPA": "9.1"
    }

]

fieldnames = ["Name", "Branch", "Year", "CGPA"]

filename = "dict_students.csv"

with open(filename, "w", newline="") as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames
    )

    # Write the header
    writer.writeheader()

    # Write multiple dictionary rows
    writer.writerows(student_data)

print("\n🗂️ Dictionary data written successfully")


# ================================================================
# 2️⃣3️⃣ writeheader() 📋
# ================================================================
# writeheader() writes the first/header row
# using the field names.
#
# Syntax:
#
# writer.writeheader()
#
# It is already demonstrated in the DictWriter example above.


# ================================================================
# 2️⃣4️⃣ writerows() WITH DictWriter() 📊
# ================================================================
# writerows() can write multiple dictionary rows.
#
# Example:
#
# writer.writerows(student_data)
#
# This is already demonstrated above.


# ================================================================
# 2️⃣5️⃣ DISPLAY DictWriter CSV OUTPUT 📊
# ================================================================

with open("dict_students.csv", "r") as f:

    print("\n📋 dict_students.csv:")

    print(f.read())


# ================================================================
# 2️⃣6️⃣ CLOSING A CSV FILE 🔒
# ================================================================
# A CSV file can be closed using close().
#
# Syntax:
# file.close()
#
# When using with statement, the file is automatically closed.

f = open("student.csv", "r")

data = f.read()

print("\n📖 student.csv data:")
print(data)

f.close()

print("🔒 CSV file closed successfully")


# ================================================================
# 2️⃣7️⃣ CSV FILE USING with STATEMENT 📦
# ================================================================
# Here, close() is not required.
# The with statement automatically closes the file.

with open("student.csv", "r") as f:

    data = f.read()

    print("\n📦 CSV using with statement:")
    print(data)


# ================================================================
# 2️⃣8️⃣ BINARY FILE MODES - rb / wb / ab 📦
# ================================================================
# rb -> Read Binary
# wb -> Write Binary
# ab -> Append Binary
#
# These modes are used for binary files.

with open("binary_file.bin", "wb") as f:

    f.write(b"Hello Binary File")

print("\n📦 Binary file written using wb mode")


with open("binary_file.bin", "rb") as f:

    data = f.read()

    print("📖 Binary file data:")
    print(data)


# ================================================================
# 2️⃣9️⃣ CREATE MODE - x 🆕
# ================================================================
# x mode creates a new file.
# If the file already exists, FileExistsError occurs.
#
# try...except is used here so the program can run safely again.

try:

    f = open("new_file.txt", "x")

    f.write("This file is created using x mode.")

    f.close()

    print("\n🆕 New file created using x mode")

except FileExistsError:

    print("\n🆕 File already exists - x mode cannot create it again")


# ================================================================
# 🔥 UNIT 4 QUICK REVISION
# ================================================================
#
# 📁 FILE HANDLING
#
# open()      -> Open file
# close()     -> Close file
# write()     -> Write data
# read()      -> Read complete data
# readline()  -> Read one line
# readlines() -> Read all lines
# with        -> Automatically handles file closing
#
# 🔑 FILE MODES
#
# r   -> Read
# w   -> Write
# a   -> Append
# r+  -> Read + Write
# w+  -> Write + Read
# a+  -> Append + Read
# rb  -> Read Binary
# wb  -> Write Binary
# ab  -> Append Binary
# x   -> Create
#
# 📊 CSV
#
# CSV = Comma Separated Values
#
# import csv
#
# csv.reader()   -> Read CSV
# csv.writer()   -> Write CSV
# writerow()     -> Write one row
# writerows()    -> Write multiple rows
# DictReader()   -> Read CSV as dictionaries
# DictWriter()   -> Write dictionaries to CSV
# writeheader()  -> Write header row
#
# ================================================================
# ✅ END OF UNIT 4 CODE SHEET
# ================================================================
