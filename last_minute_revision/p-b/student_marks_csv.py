# ============================================================
# DHP 303 - DATABASE HANDLING USING PYTHON
# FILE: 01_Student_Marks.py
#
# QUESTION:
# Create student_marks.csv with fields:
# RollNo, Name, Course, Marks, Attendance.
# Insert at least 8 records using csv module.
#
# 1. Read and display all records.
# 2. Display names and marks above 70.
# 3. Display average, maximum and minimum marks using Pandas.
# 4. Display students whose attendance is below 75%.
#
# CONCEPT:
# CSV file handling, csv module, Pandas, filtering and statistics.
# ============================================================

import csv
import pandas as pd

# Create CSV file and insert 8 student records
with open("student_marks.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["RollNo", "Name", "Course", "Marks", "Attendance"])

    # Write student records
    writer.writerows([
        [1, "Amit", "BCA", 85, 90],
        [2, "Neha", "BCA", 65, 80],
        [3, "Rahul", "BCA", 72, 70],
        [4, "Priya", "BCA", 91, 95],
        [5, "Karan", "BCA", 58, 60],
        [6, "Anjali", "BCA", 76, 72],
        [7, "Meera", "BCA", 69, 88],
        [8, "Arjun", "BCA", 80, 68]
    ])

print("CSV file created successfully.")

# 1. Read and display all records
print("\n1. All Student Records:")

with open("student_marks.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Read CSV file using Pandas
df = pd.read_csv("student_marks.csv")

# 2. Display students who scored more than 70 marks
print("\n2. Students Scoring More Than 70 Marks:")

result = df[df["Marks"] > 70]
print(result[["Name", "Marks"]].to_string(index=False))

# 3. Calculate average, maximum and minimum marks
print("\n3. Marks Statistics:")

print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# 4. Display students whose attendance is below 75%
print("\n4. Students Having Attendance Below 75%:")

result = df[df["Attendance"] < 75]
print(result[["Name", "Attendance"]].to_string(index=False))










# CSV file created successfully.

# 1. All Student Records:
# ['RollNo', 'Name', 'Course', 'Marks', 'Attendance']
# ['1', 'Amit', 'BCA', '85', '90']
# ['2', 'Neha', 'BCA', '65', '80']
# ['3', 'Rahul', 'BCA', '72', '70']
# ['4', 'Priya', 'BCA', '91', '95']
# ['5', 'Karan', 'BCA', '58', '60']
# ['6', 'Anjali', 'BCA', '76', '72']
# ['7', 'Meera', 'BCA', '69', '88']
# ['8', 'Arjun', 'BCA', '80', '68']

# 2. Students Scoring More Than 70 Marks:
#   Name  Marks
#   Amit     85
#  Rahul     72
#  Priya     91
# Anjali     76
#  Arjun     80

# 3. Marks Statistics:
# Average Marks: 74.5
# Maximum Marks: 91
# Minimum Marks: 58

# 4. Students Having Attendance Below 75%:
#   Name  Attendance
#  Rahul          70
#  Karan          60
# Anjali          72
#  Arjun          68
