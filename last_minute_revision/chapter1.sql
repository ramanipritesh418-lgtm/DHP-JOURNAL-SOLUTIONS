-- ============================================================
-- DHP 303 - DATABASE HANDLING USING PYTHON
-- CHAPTER 1 - COMPLETE SQLITE CMD CODE SHEET
-- ============================================================
--
-- 💻 This file is designed for SQLite3 CMD practice.
--
-- 📚 CHAPTER 1 TOPICS:
--
-- 1. SQLite Basics
-- 2. SQLite Data Types
-- 3. Dynamic Typing
-- 4. Type Affinity
-- 5. Manifest Typing
-- 6. Transactions
-- 7. ACID Properties
-- 8. DISTINCT
-- 9. WHERE
-- 10. BETWEEN
-- 11. IN / NOT IN
-- 12. LIKE
-- 13. UNION
-- 14. INTERSECT
-- 15. EXCEPT
-- 16. LIMIT
-- 17. GROUP BY
-- 18. HAVING
-- 19. ORDER BY
-- 20. CASE
-- 21. INNER JOIN
-- 22. LEFT OUTER JOIN
-- 23. CROSS JOIN
-- 24. SELF JOIN
-- 25. TRIGGER
-- 26. OLD / NEW
-- 27. DROP TRIGGER
--
-- ============================================================


-- ============================================================
-- 🚀 PART 1: OPEN SQLITE3 FROM CMD
-- ============================================================

-- Open CMD and go to the folder containing sqlite3.exe.
--
-- Example:
--
-- D:
-- cd D:\SQLite
--
-- Then run:
--
-- sqlite3
--
-- Expected:
--
-- SQLite version 3.x.x
-- Enter ".help" for usage hints.
-- sqlite>
--
-- Open/Create database:
--
.open chapter1.db
--
-- Expected:
-- The database chapter1.db is opened/created.


-- Show database:
.databases

-- Expected:
-- main: ...\chapter1.db r/w


-- Show available tables:
.tables

-- Expected:
-- No tables yet, if this is a new database.


-- Show help:
.help

-- Expected:
-- SQLite command list is displayed.


-- ============================================================
-- 🏗️ PART 2: CREATE COMPANY TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS COMPANY(
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    AGE INTEGER,
    ADDRESS TEXT,
    SALARY REAL
);

-- Expected:
-- Table COMPANY is created.


-- ============================================================
-- ➕ PART 3: INSERT RECORDS
-- ============================================================

INSERT INTO COMPANY VALUES
(1, 'Paul', 32, 'California', 20000.0);

INSERT INTO COMPANY VALUES
(2, 'Allen', 25, 'Texas', 15000.0);

INSERT INTO COMPANY VALUES
(3, 'Teddy', 23, 'Norway', 20000.0);

INSERT INTO COMPANY VALUES
(4, 'Mark', 25, 'Rich-Mond', 65000.0);

INSERT INTO COMPANY VALUES
(5, 'David', 27, 'Texas', 85000.0);

INSERT INTO COMPANY VALUES
(6, 'Kim', 22, 'South-Hall', 45000.0);

INSERT INTO COMPANY VALUES
(7, 'James', 24, 'Houston', 10000.0);

-- Expected:
-- Records inserted successfully.


-- Display all records:
SELECT * FROM COMPANY;

-- Expected Output:
--
-- 1|Paul|32|California|20000.0
-- 2|Allen|25|Texas|15000.0
-- 3|Teddy|23|Norway|20000.0
-- 4|Mark|25|Rich-Mond|65000.0
-- 5|David|27|Texas|85000.0
-- 6|Kim|22|South-Hall|45000.0
-- 7|James|24|Houston|10000.0


-- ============================================================
-- 🧱 PART 4: SQLITE DATA TYPES
-- ============================================================
--
-- SQLite has five main storage classes:
--
-- NULL
-- INTEGER
-- REAL
-- TEXT
-- BLOB
-- ============================================================

CREATE TABLE IF NOT EXISTS DATATYPES(
    ID INTEGER,
    NAME TEXT,
    VALUE REAL
);


-- NULL
INSERT INTO DATATYPES VALUES
(1, NULL, NULL);

-- INTEGER
INSERT INTO DATATYPES VALUES
(2, 'Age', 20);

-- REAL
INSERT INTO DATATYPES VALUES
(3, 'Salary', 25000.50);

-- TEXT
INSERT INTO DATATYPES VALUES
(4, 'Name', 'Pritesh');

-- BLOB
INSERT INTO DATATYPES VALUES
(5, 'File', X'48656C6C6F');


SELECT * FROM DATATYPES;

-- Expected Output:
--
-- 1|| 
-- 2|Age|20.0
-- 3|Salary|25000.5
-- 4|Name|25000.5
-- 5|File|...


-- ============================================================
-- 🔄 PART 5: DYNAMIC TYPING
-- ============================================================

CREATE TABLE IF NOT EXISTS DYNAMIC_TEST(
    DATA
);

INSERT INTO DYNAMIC_TEST VALUES (100);

INSERT INTO DYNAMIC_TEST VALUES (25.50);

INSERT INTO DYNAMIC_TEST VALUES ('Hello');

INSERT INTO DYNAMIC_TEST VALUES (NULL);


SELECT * FROM DYNAMIC_TEST;

-- Expected Output:
--
-- 100
-- 25.5
-- Hello
--
--


-- ============================================================
-- 🧲 PART 6: TYPE AFFINITY
-- ============================================================

CREATE TABLE IF NOT EXISTS AFFINITY_TEST(
    NAME TEXT,
    AGE INTEGER,
    SALARY REAL
);

INSERT INTO AFFINITY_TEST
VALUES ('Pritesh', 19, 25000.50);


SELECT * FROM AFFINITY_TEST;

-- Expected Output:
--
-- Pritesh|19|25000.5


-- ============================================================
-- 🧠 PART 7: MANIFEST TYPING
-- ============================================================
--
-- Manifest typing means:
-- The data type is associated with the value stored,
-- not strictly with the column.
--
-- SQLite can store different types of values in a column.
-- ============================================================

CREATE TABLE IF NOT EXISTS MANIFEST_TEST(
    DATA
);

INSERT INTO MANIFEST_TEST VALUES (100);

INSERT INTO MANIFEST_TEST VALUES ('SQLite');

INSERT INTO MANIFEST_TEST VALUES (25.50);


SELECT * FROM MANIFEST_TEST;

-- Expected Output:
--
-- 100
-- SQLite
-- 25.5


-- ============================================================
-- 🔄 PART 8: TRANSACTION
-- ============================================================
--
-- Main Transaction Commands:
--
-- BEGIN
-- COMMIT
-- ROLLBACK
-- ============================================================


-- ------------------------------------------------------------
-- ❌ ROLLBACK EXAMPLE
-- ------------------------------------------------------------

-- Start transaction:
BEGIN;

-- Delete records with AGE 25:
DELETE FROM COMPANY
WHERE AGE = 25;

-- Check data before rollback:
SELECT * FROM COMPANY;

-- Expected before ROLLBACK:
--
-- 1|Paul|32|California|20000.0
-- 3|Teddy|23|Norway|20000.0
-- 5|David|27|Texas|85000.0
-- 6|Kim|22|South-Hall|45000.0
-- 7|James|24|Houston|10000.0
--
-- Allen and Mark are temporarily deleted.


-- Cancel transaction:
ROLLBACK;


-- Check again:
SELECT * FROM COMPANY;

-- Expected after ROLLBACK:
--
-- 1|Paul|32|California|20000.0
-- 2|Allen|25|Texas|15000.0
-- 3|Teddy|23|Norway|20000.0
-- 4|Mark|25|Rich-Mond|65000.0
-- 5|David|27|Texas|85000.0
-- 6|Kim|22|South-Hall|45000.0
-- 7|James|24|Houston|10000.0
--
-- ✅ Deleted records come back.


-- ------------------------------------------------------------
-- 💾 COMMIT EXAMPLE
-- ------------------------------------------------------------

BEGIN;

DELETE FROM COMPANY
WHERE AGE = 25;

COMMIT;


SELECT * FROM COMPANY;

-- Expected Output:
--
-- 1|Paul|32|California|20000.0
-- 3|Teddy|23|Norway|20000.0
-- 5|David|27|Texas|85000.0
-- 6|Kim|22|South-Hall|45000.0
-- 7|James|24|Houston|10000.0
--
-- Allen and Mark are permanently deleted.


-- ============================================================
-- ⭐ PART 9: ACID PROPERTIES
-- ============================================================
--
-- A = Atomicity
-- C = Consistency
-- I = Isolation
-- D = Durability
--
-- Atomicity:
-- All operations succeed or all are rolled back.
--
-- Consistency:
-- Database remains in a valid state.
--
-- Isolation:
-- Transactions work independently.
--
-- Durability:
-- Committed changes remain saved.
-- ============================================================


-- ============================================================
-- 🎯 PART 10: DISTINCT
-- ============================================================

CREATE TABLE IF NOT EXISTS STUDENT(
    ID INTEGER,
    NAME TEXT,
    CITY TEXT,
    MARKS INTEGER
);


INSERT INTO STUDENT VALUES
(1, 'Amit', 'Surat', 80);

INSERT INTO STUDENT VALUES
(2, 'Rahul', 'Surat', 75);

INSERT INTO STUDENT VALUES
(3, 'Neha', 'Mumbai', 90);

INSERT INTO STUDENT VALUES
(4, 'Priya', 'Mumbai', 85);


SELECT DISTINCT CITY
FROM STUDENT;

-- Expected Output:
--
-- Surat
-- Mumbai
--
-- DISTINCT removes duplicate values.


-- ============================================================
-- 🔎 PART 11: WHERE
-- ============================================================

SELECT *
FROM COMPANY
WHERE AGE > 25;

-- Expected:
--
-- Paul
-- David


SELECT *
FROM COMPANY
WHERE SALARY = 20000;

-- Expected:
--
-- Paul
-- Teddy


-- AND:
SELECT *
FROM COMPANY
WHERE AGE > 25
AND SALARY > 20000;

-- Expected:
--
-- David


-- OR:
SELECT *
FROM COMPANY
WHERE AGE = 25
OR AGE = 27;

-- Expected:
--
-- Allen
-- Mark
-- David


-- NOT:
SELECT *
FROM COMPANY
WHERE NOT AGE = 25;

-- Expected:
-- All records except Allen and Mark.


-- ============================================================
-- 🔢 PART 12: BETWEEN
-- ============================================================

SELECT *
FROM COMPANY
WHERE AGE BETWEEN 23 AND 27;

-- Expected:
--
-- Teddy 23
-- Allen 25
-- Mark 25
-- David 27
-- James 24


-- Equivalent:
SELECT *
FROM COMPANY
WHERE AGE >= 23
AND AGE <= 27;


-- ============================================================
-- 📋 PART 13: IN
-- ============================================================

SELECT *
FROM COMPANY
WHERE AGE IN (23, 25, 27);

-- Expected:
--
-- Teddy
-- Allen
-- Mark
-- David


-- Equivalent:
SELECT *
FROM COMPANY
WHERE AGE = 23
OR AGE = 25
OR AGE = 27;


-- ============================================================
-- 🚫 PART 14: NOT IN
-- ============================================================

SELECT *
FROM COMPANY
WHERE AGE NOT IN (23, 25, 27);

-- Expected:
--
-- Paul
-- Kim
-- James


-- ============================================================
-- 🔤 PART 15: LIKE
-- ============================================================

-- Names starting with P:
SELECT *
FROM COMPANY
WHERE NAME LIKE 'P%';

-- Expected:
--
-- Paul


-- Names ending with l:
SELECT *
FROM COMPANY
WHERE NAME LIKE '%l';

-- Expected:
--
-- Paul


-- Names containing a:
SELECT *
FROM COMPANY
WHERE NAME LIKE '%a%';

-- Expected:
--
-- Paul
-- Mark
-- David
-- James


-- One-character wildcard:
SELECT *
FROM COMPANY
WHERE NAME LIKE '_aul';

-- Expected:
--
-- Paul


-- % = zero or more characters
-- _ = exactly one character


-- ============================================================
-- 🔗 PART 16: UNION
-- ============================================================

SELECT CITY
FROM STUDENT
WHERE MARKS >= 80

UNION

SELECT CITY
FROM STUDENT
WHERE MARKS >= 90;

-- Expected Output:
--
-- Mumbai
-- Surat
--
-- UNION removes duplicate results.


-- ============================================================
-- 🔗 PART 17: INTERSECT
-- ============================================================

SELECT CITY
FROM STUDENT
WHERE MARKS >= 80

INTERSECT

SELECT CITY
FROM STUDENT
WHERE MARKS >= 90;

-- Expected Output:
--
-- Mumbai
--
-- INTERSECT returns common results.


-- ============================================================
-- ➖ PART 18: EXCEPT
-- ============================================================

SELECT CITY
FROM STUDENT
WHERE MARKS >= 75

EXCEPT

SELECT CITY
FROM STUDENT
WHERE MARKS >= 90;

-- Expected Output:
--
-- Surat
--
-- EXCEPT returns results from first query
-- that are not in second query.


-- ============================================================
-- 🔢 PART 19: LIMIT
-- ============================================================

SELECT *
FROM COMPANY
LIMIT 3;

-- Expected:
-- First 3 records.


-- LIMIT + OFFSET:
SELECT *
FROM COMPANY
LIMIT 3 OFFSET 2;

-- Expected:
-- 3 records starting after first 2 records.


-- ============================================================
-- 👥 PART 20: GROUP BY
-- ============================================================

SELECT AGE, COUNT(*)
FROM COMPANY
GROUP BY AGE;

-- Expected Output:
--
-- 22|1
-- 23|1
-- 24|1
-- 27|1
--
-- If records with same AGE exist,
-- they are grouped together.


SELECT ADDRESS, COUNT(*)
FROM COMPANY
GROUP BY ADDRESS;

-- Expected:
-- Each address with its number of records.


-- ============================================================
-- 🎯 PART 21: HAVING
-- ============================================================

SELECT AGE, COUNT(*)
FROM COMPANY
GROUP BY AGE
HAVING COUNT(*) > 1;

-- Expected:
--
-- If an age occurs more than once,
-- that age is displayed.


-- IMPORTANT:
--
-- WHERE  -> Filters individual records
-- HAVING -> Filters groups
-- ============================================================


-- ============================================================
-- ↕️ PART 22: ORDER BY
-- ============================================================

-- Ascending:
SELECT *
FROM COMPANY
ORDER BY SALARY ASC;

-- Expected:
-- Salary from LOW to HIGH.


-- Descending:
SELECT *
FROM COMPANY
ORDER BY SALARY DESC;

-- Expected:
-- Salary from HIGH to LOW.


-- ============================================================
-- 🧠 PART 23: CASE
-- ============================================================

SELECT
    NAME,
    AGE,
    CASE
        WHEN AGE >= 30 THEN 'Senior'
        WHEN AGE >= 25 THEN 'Adult'
        ELSE 'Young'
    END AS AGE_GROUP
FROM COMPANY;

-- Expected example:
--
-- Paul|32|Senior
-- Allen|25|Adult
-- Teddy|23|Young
-- Mark|25|Adult
-- David|27|Adult
-- Kim|22|Young
-- James|24|Young


-- Salary CASE:
SELECT
    NAME,
    SALARY,
    CASE
        WHEN SALARY >= 50000 THEN 'High Salary'
        WHEN SALARY >= 20000 THEN 'Medium Salary'
        ELSE 'Low Salary'
    END AS SALARY_GROUP
FROM COMPANY;

-- Expected:
--
-- Salary >= 50000 -> High Salary
-- Salary >= 20000 -> Medium Salary
-- Otherwise       -> Low Salary


-- ============================================================
-- 🔗 PART 24: CREATE DEPARTMENT TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS DEPARTMENT(
    ID INTEGER,
    DEPT_NAME TEXT
);


INSERT INTO DEPARTMENT VALUES
(1, 'Computer');

INSERT INTO DEPARTMENT VALUES
(2, 'Science');

INSERT INTO DEPARTMENT VALUES
(3, 'Commerce');


SELECT * FROM DEPARTMENT;

-- Expected:
--
-- 1|Computer
-- 2|Science
-- 3|Commerce


-- ============================================================
-- 🔗 PART 25: INNER JOIN
-- ============================================================

SELECT
    COMPANY.ID,
    COMPANY.NAME,
    DEPARTMENT.DEPT_NAME
FROM COMPANY
INNER JOIN DEPARTMENT
ON COMPANY.ID = DEPARTMENT.ID;

-- Expected:
--
-- 1|Paul|Computer
-- 2|Allen|Science
-- 3|Teddy|Commerce
--
-- INNER JOIN returns matching rows.


-- ============================================================
-- ⬅️ PART 26: LEFT OUTER JOIN
-- ============================================================

SELECT
    COMPANY.ID,
    COMPANY.NAME,
    DEPARTMENT.DEPT_NAME
FROM COMPANY
LEFT OUTER JOIN DEPARTMENT
ON COMPANY.ID = DEPARTMENT.ID;

-- Expected:
--
-- All COMPANY records are displayed.
-- Matching department is displayed.
-- Non-matching department = NULL.


-- ============================================================
-- ✖️ PART 27: CROSS JOIN
-- ============================================================

SELECT
    COMPANY.NAME,
    DEPARTMENT.DEPT_NAME
FROM COMPANY
CROSS JOIN DEPARTMENT;

-- Expected:
--
-- Every COMPANY record is combined
-- with every DEPARTMENT record.
--
-- If COMPANY has 7 rows
-- and DEPARTMENT has 3 rows:
--
-- Total rows = 7 x 3 = 21


-- ============================================================
-- 🔄 PART 28: SELF JOIN
-- ============================================================

SELECT
    A.NAME AS EMPLOYEE,
    B.NAME AS OTHER_EMPLOYEE
FROM COMPANY A
JOIN COMPANY B
ON A.ID <> B.ID;

-- Expected:
--
-- Records are generated by joining
-- COMPANY with itself.
--
-- A = First copy of COMPANY
-- B = Second copy of COMPANY


-- ============================================================
-- 🔥 PART 29: CREATE LEADS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS leads(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);


-- ============================================================
-- 🚨 PART 30: BEFORE INSERT TRIGGER
-- ============================================================

CREATE TRIGGER IF NOT EXISTS validate_email_before_insert_leads
BEFORE INSERT ON leads
BEGIN
    SELECT
    CASE
        WHEN NEW.email NOT LIKE '%_@_%._%'
        THEN RAISE(ABORT, 'Invalid email address')
    END;
END;


-- ============================================================
-- ✅ PART 31: TEST VALID EMAIL
-- ============================================================

INSERT INTO leads
VALUES (1, 'Pritesh', 'pritesh@gmail.com');


SELECT * FROM leads;

-- Expected:
--
-- 1|Pritesh|pritesh@gmail.com


-- ============================================================
-- ❌ PART 32: TEST INVALID EMAIL
-- ============================================================

-- Uncomment this command to test the trigger:
--
-- INSERT INTO leads
-- VALUES (2, 'Test', 'wrongemail');
--
-- Expected:
--
-- Runtime error: Invalid email address
--
-- The trigger stops the invalid INSERT.


-- ============================================================
-- 🆕 PART 33: OLD AND NEW
-- ============================================================
--
-- INSERT:
-- NEW is available.
--
-- UPDATE:
-- OLD and NEW are available.
--
-- DELETE:
-- OLD is available.
--
-- Remember:
--
-- INSERT -> NEW
-- UPDATE -> OLD + NEW
-- DELETE -> OLD
-- ============================================================


-- ============================================================
-- ⏱️ PART 34: TRIGGER TYPES
-- ============================================================
--
-- BEFORE INSERT
-- AFTER INSERT
--
-- BEFORE UPDATE
-- AFTER UPDATE
--
-- BEFORE DELETE
-- AFTER DELETE
--
-- INSTEAD OF INSERT
-- INSTEAD OF UPDATE
-- INSTEAD OF DELETE
--
-- BEFORE and AFTER can be used on tables.
-- INSTEAD OF is used on views.
-- ============================================================


-- ============================================================
-- 🔍 PART 35: VIEW ALL TRIGGERS
-- ============================================================

SELECT name
FROM sqlite_master
WHERE type = 'trigger';

-- Expected:
--
-- validate_email_before_insert_leads


-- ============================================================
-- 🗑️ PART 36: DROP TRIGGER
-- ============================================================

DROP TRIGGER IF EXISTS validate_email_before_insert_leads;

-- Expected:
-- Trigger is deleted.


SELECT name
FROM sqlite_master
WHERE type = 'trigger';

-- Expected:
-- No output for this trigger.


-- ============================================================
-- 🛠️ PART 37: USEFUL SQLITE COMMANDS
-- ============================================================

-- Show tables:
.tables

-- Show table structure:
.schema COMPANY

-- Show complete database schema:
.schema

-- Show databases:
.databases

-- Show help:
.help

-- Exit SQLite:
.quit


-- ============================================================
-- ⭐ PART 38: IMPORTANT FULL FORMS
-- ============================================================
--
-- DBMS = Database Management System
--
-- SQL = Structured Query Language
--
-- ACID = Atomicity, Consistency, Isolation, Durability
--
-- BLOB = Binary Large Object
--
-- DML = Data Manipulation Language
--
-- DDL = Data Definition Language
--
-- API = Application Programming Interface
--
-- CMD = Command Prompt
--
-- CRUD = Create, Read, Update, Delete
--
-- NOTE:
-- NULL is not a standard full form.
-- NULL represents no value / missing or unknown value.
--
-- ============================================================


-- ============================================================
-- ⭐ PART 39: CHAPTER 1 QUICK REVISION
-- ============================================================
--
-- DATA TYPES:
-- NULL
-- INTEGER
-- REAL
-- TEXT
-- BLOB
--
-- TRANSACTION:
-- BEGIN
-- COMMIT
-- ROLLBACK
--
-- ACID:
-- Atomicity
-- Consistency
-- Isolation
-- Durability
--
-- FILTERING:
-- DISTINCT
-- WHERE
-- BETWEEN
-- IN
-- NOT IN
-- LIKE
-- UNION
-- INTERSECT
-- EXCEPT
-- LIMIT
--
-- GROUPING:
-- GROUP BY
-- HAVING
-- ORDER BY
--
-- CONDITIONAL:
-- CASE
--
-- JOIN:
-- INNER JOIN
-- LEFT OUTER JOIN
-- CROSS JOIN
-- SELF JOIN
--
-- TRIGGER:
-- BEFORE
-- AFTER
-- INSTEAD OF
-- INSERT
-- UPDATE
-- DELETE
-- OLD
-- NEW
-- DROP TRIGGER
--
-- ============================================================
-- 🎯 CHAPTER 1 COMPLETE
-- ============================================================
