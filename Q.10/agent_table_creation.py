# ============================================================
# PRACTICAL ASSIGNMENT - 2
# DATABASE HANDLING USING PYTHON
# ============================================================

"""
QUESTION:

Write a Python program to connect a database and create a
SQLite table within the database.

Fields:
agent_code char(6),
agent_name char(40),
working_area char(35),
commission decimal(10,2),
phone_no char(15) NULL
"""


# ============================================================
# STEP 1: Import sqlite3 module
# ============================================================

import sqlite3


# ============================================================
# STEP 2: Connect to SQLite Database
# ============================================================

con = sqlite3.connect("Agent.db")


# ============================================================
# STEP 3: Create Cursor
# ============================================================

cursor = con.cursor()


# ============================================================
# STEP 4: Create Agent Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Agent (
    agent_code CHAR(6),
    agent_name CHAR(40),
    working_area CHAR(35),
    commission DECIMAL(10,2),
    phone_no CHAR(15) NULL
)
""")


# ============================================================
# STEP 5: Commit Changes
# ============================================================

con.commit()


# ============================================================
# STEP 6: Display Table Created Message
# ============================================================

print("Agent table created successfully.")


# ============================================================
# STEP 7: Close Database Connection
# ============================================================

con.close()


# ============================================================
# OUTPUT
# ============================================================

# Agent table created successfully.
