# ============================================================
#                 PYTHON FILE HANDLING
# ============================================================
# Concepts Covered:
# 1. open()
# 2. write()
# 3. read()
# 4. readline()
# 5. readlines()
# 6. Append Mode
# 7. close()
# 8. with Statement
# ============================================================


# ------------------------------------------------------------
# 1. OPENING A FILE + write() + close()
# ------------------------------------------------------------

file = open("student.txt", "w")

file.write("Name: Pritesh\n")
file.write("Course: BCA\n")
file.write("Semester: 3\n")

file.close()

print("File created and data written successfully!")


# OUTPUT:
# File created and data written successfully!


# ------------------------------------------------------------
# 2. READING COMPLETE FILE - read()
# ------------------------------------------------------------

file = open("student.txt", "r")

data = file.read()

print("\n--- Using read() ---")
print(data)

file.close()


# OUTPUT:
# --- Using read() ---
# Name: Pritesh
# Course: BCA
# Semester: 3


# ------------------------------------------------------------
# 3. READING ONE LINE - readline()
# ------------------------------------------------------------

file = open("student.txt", "r")

line = file.readline()

print("--- Using readline() ---")
print(line)

file.close()


# OUTPUT:
# --- Using readline() ---
# Name: Pritesh


# ------------------------------------------------------------
# 4. READING ALL LINES - readlines()
# ------------------------------------------------------------

file = open("student.txt", "r")

lines = file.readlines()

print("--- Using readlines() ---")

for line in lines:
    print(line.strip())

file.close()


# OUTPUT:
# --- Using readlines() ---
# Name: Pritesh
# Course: BCA
# Semester: 3


# ------------------------------------------------------------
# 5. APPENDING DATA - "a" MODE
# ------------------------------------------------------------

file = open("student.txt", "a")

file.write("College: ABC College\n")
file.write("Subject: Python\n")

file.close()

print("\nNew data appended successfully!")


# OUTPUT:
# New data appended successfully!


# ------------------------------------------------------------
# 6. THE with STATEMENT
# ------------------------------------------------------------
# The with statement automatically closes the file.

with open("student.txt", "r") as file:

    print("\n--- Using with Statement ---")

    data = file.read()

    print(data)


# OUTPUT:
# --- Using with Statement ---
# Name: Pritesh
# Course: BCA
# Semester: 3
# College: ABC College
# Subject: Python


# ------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------

print("File Handling demonstration completed successfully! ✅")


# OUTPUT:
# File Handling demonstration completed successfully! ✅


# ============================================================
#                    END OF PROGRAM
# ============================================================
