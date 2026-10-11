# ============================================================
# Paper C - Question 2 (10 Marks)
#
# QUESTION:
# Create Library(BookID, Title, Author, Category, Price)
# and insert at least 5 records.
# 1. Export table data into library.csv.
# 2. Display books where Price > 500.
# 3. Display books whose Title starts with 'B'.
# 4. Dump the Library table structure into Library.sql.
#
# CONCEPT:
# 1. CREATE TABLE creates the Library table.
# 2. csv.writer() exports records to CSV.
# 3. WHERE Price > 500 filters expensive books.
# 4. LIKE 'B%' finds titles starting with B.
# 5. sqlite_master stores SQLite table definitions.
# 6. The CREATE TABLE statement is written to Library.sql.
# ============================================================

import sqlite3
import csv

con = sqlite3.connect("Library.db")
cur = con.cursor()

# Create Library table
cur.execute("""
CREATE TABLE IF NOT EXISTS Library(
    BookID INTEGER PRIMARY KEY,
    Title TEXT,
    Author TEXT,
    Category TEXT,
    Price REAL
)
""")

cur.execute("DELETE FROM Library")

# Insert at least 5 records
data = [
    (1, "Basic Python", "Amit", "Programming", 650),
    (2, "Database System", "Raj", "Database", 800),
    (3, "Web Design", "Neha", "Web", 450),
    (4, "Business Studies", "Kiran", "Commerce", 550),
    (5, "C Programming", "Mehul", "Programming", 700)
]

cur.executemany(
    "INSERT INTO Library VALUES (?, ?, ?, ?, ?)", data
)
con.commit()

# 1. Export entire table to library.csv
cur.execute("SELECT * FROM Library")
rows = cur.fetchall()

with open("library.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["BookID", "Title", "Author", "Category", "Price"])
    writer.writerows(rows)

print("Data exported to library.csv")

# 2. Display books where Price > 500
print("\nBooks with Price > 500:")

cur.execute("SELECT * FROM Library WHERE Price > 500")

for row in cur.fetchall():
    print(row)

# 3. Display books whose Title starts with B
print("\nBooks whose Title starts with B:")

cur.execute("SELECT * FROM Library WHERE Title LIKE 'B%'")

for row in cur.fetchall():
    print(row)

# 4. Dump table structure into Library.sql
cur.execute("""
SELECT sql FROM sqlite_master
WHERE type = 'table' AND name = 'Library'
""")

table_structure = cur.fetchone()[0]

with open("Library.sql", "w") as file:
    file.write(table_structure + ";\n")

print("\nTable structure exported to Library.sql")

con.close()

# OUTPUT:
# Data exported to library.csv
#
# Books with Price > 500:
# (1, 'Basic Python', 'Amit', 'Programming', 650.0)
# (2, 'Database System', 'Raj', 'Database', 800.0)
# (4, 'Business Studies', 'Kiran', 'Commerce', 550.0)
# (5, 'C Programming', 'Mehul', 'Programming', 700.0)
#
# Books whose Title starts with B:
# (1, 'Basic Python', 'Amit', 'Programming', 650.0)
# (2, 'Database System', 'Raj', 'Database', 800.0)
# (4, 'Business Studies', 'Kiran', 'Commerce', 550.0)
#
# Table structure exported to Library.sql