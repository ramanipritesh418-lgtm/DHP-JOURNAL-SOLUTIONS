# ============================================================
# PRACTICAL ASSIGNMENT - 2
# DATABASE HANDLING USING PYTHON
# ============================================================

"""
QUESTION:

Employee(Eno number, Ename text, Desg text, Salary number,
City text, Email text)

Write a SQL trigger named emp_trigger that is designed to
execute before inserting records into the emp table.

The trigger should perform the following action:

1) Check if the 'Email' field in the newly inserted record
   follows a specific email address pattern.

Example: abc@gmail.com
"""


# ============================================================
# STEP 1: Import sqlite3 module
# ============================================================

import sqlite3


# ============================================================
# STEP 2: Create / Connect SQLite Database
# emp_trigger.db will be created automatically if it does
# not exist.
# ============================================================

con = sqlite3.connect("emp_trigger.db")


# ============================================================
# STEP 3: Create Cursor
# ============================================================

cursor = con.cursor()


# ============================================================
# STEP 4: Create Employee Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS emp (
    Eno INTEGER PRIMARY KEY,
    Ename TEXT,
    Desg TEXT,
    Salary REAL,
    City TEXT,
    Email TEXT
)
""")


# ============================================================
# STEP 5: Create BEFORE INSERT Trigger
# Trigger checks whether Email ends with @gmail.com.
# ============================================================

cursor.execute("""
CREATE TRIGGER IF NOT EXISTS emp_trigger
BEFORE INSERT ON emp
FOR EACH ROW
WHEN NEW.Email NOT LIKE '%@gmail.com'
BEGIN
    SELECT RAISE(ABORT, 'Invalid Email Address');
END
""")


# ============================================================
# STEP 6: Insert Valid Employee Record
# Email follows the required pattern.
# ============================================================

cursor.execute("""
INSERT INTO emp
VALUES (
    101,
    'Rahul',
    'Manager',
    50000,
    'Surat',
    'rahul@gmail.com'
)
""")

con.commit()


# ============================================================
# STEP 7: Display Employee Records
# ============================================================

print("Employee Records:")

cursor.execute("SELECT * FROM emp")

data = cursor.fetchall()

for row in data:
    print(row)


# ============================================================
# STEP 8: Test Invalid Email
# This record will NOT be inserted because the Email is invalid.
# ============================================================

try:
    cursor.execute("""
    INSERT INTO emp
    VALUES (
        102,
        'Amit',
        'Clerk',
        25000,
        'Surat',
        'amit123'
    )
    """)

    con.commit()

except sqlite3.IntegrityError as e:
    print("\nError:", e)


# ============================================================
# STEP 9: Close Database Connection
# ============================================================

con.close()


# ============================================================
# END OF PRACTICAL ASSIGNMENT - 2
# ============================================================
