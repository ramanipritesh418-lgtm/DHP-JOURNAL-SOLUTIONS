# ============================================================
# DHP 303 - Database Handling Using Python (PR)
# B.C.A. Semester III - December 2025
#
# QUESTION 2:
# Create a text file data.txt and perform the following tasks:
#
# 1. Write few lines into the file.
# 2. Read the file.
# 3. Count the total number of lines.
# 4. Display the first line of the file.
#
# ============================================================
# CONCEPT:
# open()     - Opens a file.
# write()    - Writes text into a file.
# readlines()- Reads all lines into a list.
# len()      - Counts the number of lines.
# close()    - Closes the file.
# ============================================================

# Step 1: Write a few lines into data.txt
file = open("data.txt", "w")

file.write("Python is a programming language.\n")
file.write("Python supports file handling.\n")
file.write("Python is easy to learn.\n")
file.write("Python is used for data analysis.\n")

file.close()

print("Data written to data.txt successfully!")

# Step 2: Read the file
file = open("data.txt", "r")

lines = file.readlines()

print("\nContents of data.txt:")

for line in lines:
    print(line, end="")

# Step 3: Count the total number of lines
print("\n\nTotal number of lines:", len(lines))

# Step 4: Display the first line
print("First line of the file:", lines[0].strip())

# Close the file
file.close()

# ============================================================
# EXPECTED OUTPUT:
#
# Data written to data.txt successfully!
#
# Contents of data.txt:
# Python is a programming language.
# Python supports file handling.
# Python is easy to learn.
# Python is used for data analysis.
#
# Total number of lines: 4
# First line of the file: Python is a programming language.
#
# ============================================================
# EXPLANATION:
#
# 1. open("data.txt", "w") creates or overwrites the file.
# 2. write() writes four lines into the file.
# 3. open("data.txt", "r") opens the file for reading.
# 4. readlines() reads all lines into a list.
# 5. len(lines) counts the total number of lines.
# 6. lines[0] accesses the first line.
# 7. strip() removes the newline character from the output.
#
# ============================================================