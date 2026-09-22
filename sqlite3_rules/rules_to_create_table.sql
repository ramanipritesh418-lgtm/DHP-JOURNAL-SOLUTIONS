-- ============================================================
-- SQLite3 BASIC PRACTICAL CODE SHEET WITH OUTPUT
-- ============================================================


-- ============================================================
-- 1. OPEN / CREATE DATABASE
-- ============================================================

.open college.db

-- OUTPUT:
-- Database is opened/created.
-- No output is normally displayed.


-- ============================================================
-- 2. SHOW DATABASES
-- ============================================================

.databases

-- OUTPUT:
-- main: C:\...\college.db


-- ============================================================
-- 3. CREATE STUDENT TABLE
-- ============================================================

CREATE TABLE STUDENT (
    sno INTEGER PRIMARY KEY,
    sname TEXT,
    age INTEGER,
    total_marks REAL
);

-- OUTPUT:
-- No output means table was created successfully.


-- ============================================================
-- 4. SHOW ALL TABLES
-- ============================================================

.tables

-- OUTPUT:
-- STUDENT


-- ============================================================
-- 5. SHOW TABLE STRUCTURE
-- ============================================================

.schema STUDENT

-- OUTPUT:
-- CREATE TABLE STUDENT (
--     sno INTEGER PRIMARY KEY,
--     sname TEXT,
--     age INTEGER,
--     total_marks REAL
-- );


-- ============================================================
-- 6. CHECK TABLE INFORMATION
-- ============================================================

PRAGMA table_info(STUDENT);

-- OUTPUT:
-- cid  name         type     notnull  dflt_value  pk
-- 0    sno          INTEGER  0        NULL        1
-- 1    sname        TEXT     0        NULL        0
-- 2    age          INTEGER  0        NULL        0
-- 3    total_marks  REAL     0        NULL        0


-- ============================================================
-- 7. INSERT RECORDS
-- ============================================================

INSERT INTO STUDENT VALUES (1, 'Rahul', 18, 450);
INSERT INTO STUDENT VALUES (2, 'Amit', 19, 420);
INSERT INTO STUDENT VALUES (3, 'Neha', 18, 470);
INSERT INTO STUDENT VALUES (4, 'Priya', 20, 400);
INSERT INTO STUDENT VALUES (5, 'Raj', 17, 380);

-- OUTPUT:
-- No output means records were inserted successfully.


-- ============================================================
-- 8. DISPLAY ALL RECORDS
-- ============================================================

.headers on
.mode column

SELECT * FROM STUDENT;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  18   450.0
-- 2    Amit   19   420.0
-- 3    Neha   18   470.0
-- 4    Priya  20   400.0
-- 5    Raj    17   380.0


-- ============================================================
-- 9. DISPLAY SPECIFIC COLUMNS
-- ============================================================

SELECT sname, age FROM STUDENT;

-- OUTPUT:
-- sname  age
-- -----  ---
-- Rahul  18
-- Amit   19
-- Neha   18
-- Priya  20
-- Raj    17


-- ============================================================
-- 10. WHERE - AGE = 18
-- ============================================================

SELECT * FROM STUDENT
WHERE age = 18;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  18   450.0
-- 3    Neha   18   470.0


-- ============================================================
-- 11. WHERE - AGE > 18
-- ============================================================

SELECT * FROM STUDENT
WHERE age > 18;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 2    Amit   19   420.0
-- 4    Priya  20   400.0


-- ============================================================
-- 12. WHERE - AGE < 18
-- ============================================================

SELECT * FROM STUDENT
WHERE age < 18;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 5    Raj    17   380.0


-- ============================================================
-- 13. WHERE - AGE >= 18
-- ============================================================

SELECT * FROM STUDENT
WHERE age >= 18;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  18   450.0
-- 2    Amit   19   420.0
-- 3    Neha   18   470.0
-- 4    Priya  20   400.0


-- ============================================================
-- 14. WHERE - AGE <= 18
-- ============================================================

SELECT * FROM STUDENT
WHERE age <= 18;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  18   450.0
-- 3    Neha   18   470.0
-- 5    Raj    17   380.0


-- ============================================================
-- 15. TOP 3 RECORDS
-- ============================================================

SELECT * FROM STUDENT
LIMIT 3;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  18   450.0
-- 2    Amit   19   420.0
-- 3    Neha   18   470.0


-- ============================================================
-- 16. ORDER BY - HIGHEST MARKS FIRST
-- ============================================================

SELECT * FROM STUDENT
ORDER BY total_marks DESC;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 3    Neha   18   470.0
-- 1    Rahul  18   450.0
-- 2    Amit   19   420.0
-- 4    Priya  20   400.0
-- 5    Raj    17   380.0


-- ============================================================
-- 17. ORDER BY - LOWEST MARKS FIRST
-- ============================================================

SELECT * FROM STUDENT
ORDER BY total_marks ASC;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 5    Raj    17   380.0
-- 4    Priya  20   400.0
-- 2    Amit   19   420.0
-- 1    Rahul  18   450.0
-- 3    Neha   18   470.0


-- ============================================================
-- 18. BETWEEN
-- ============================================================

SELECT * FROM STUDENT
WHERE age BETWEEN 18 AND 20;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  18   450.0
-- 2    Amit   19   420.0
-- 3    Neha   18   470.0
-- 4    Priya  20   400.0


-- ============================================================
-- 19. DISTINCT
-- ============================================================

SELECT DISTINCT age FROM STUDENT;

-- OUTPUT:
-- age
-- ---
-- 18
-- 19
-- 20
-- 17


-- ============================================================
-- 20. UPDATE RECORD
-- ============================================================

UPDATE STUDENT
SET age = 19
WHERE sno = 1;

-- OUTPUT:
-- No output means record was updated successfully.


-- CHECK UPDATED RECORD

SELECT * FROM STUDENT
WHERE sno = 1;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  19   450.0


-- ============================================================
-- 21. DELETE SPECIFIC RECORD
-- ============================================================

DELETE FROM STUDENT
WHERE sno = 5;

-- OUTPUT:
-- No output means record was deleted successfully.


-- CHECK RECORDS

SELECT * FROM STUDENT;

-- OUTPUT:
-- sno  sname  age  total_marks
-- ---  -----  ---  -----------
-- 1    Rahul  19   450.0
-- 2    Amit   19   420.0
-- 3    Neha   18   470.0
-- 4    Priya  20   400.0


-- ============================================================
-- 22. DELETE ALL RECORDS
-- ============================================================

-- WARNING:
-- This deletes ALL records but keeps the table.

-- DELETE FROM STUDENT;


-- ============================================================
-- 23. DROP TABLE
-- ============================================================

-- WARNING:
-- This deletes the complete table and its data.

-- DROP TABLE STUDENT;


-- ============================================================
-- 24. CREATE TABLE IF NOT EXISTS
-- ============================================================

CREATE TABLE IF NOT EXISTS EMPLOYEE (
    eid INTEGER PRIMARY KEY,
    ename TEXT,
    salary REAL
);

-- OUTPUT:
-- No output means table was created successfully.


-- ============================================================
-- 25. SHOW ALL TABLES
-- ============================================================

.tables

-- OUTPUT:
-- EMPLOYEE  STUDENT


-- ============================================================
-- 26. SQLITE HELP
-- ============================================================

.help

-- OUTPUT:
-- Shows the list of SQLite commands and their descriptions.


-- ============================================================
-- 27. EXIT SQLITE
-- ============================================================

.quit

-- OR

.exit


-- ============================================================
-- IMPORTANT SQLITE3 RULES
-- ============================================================

-- SQLite Commands:
-- .help
-- .databases
-- .tables
-- .schema STUDENT
-- .headers on
-- .mode column
-- .quit
-- .exit

-- SQL Commands:
-- CREATE TABLE
-- INSERT INTO
-- SELECT
-- UPDATE
-- DELETE
-- DROP TABLE

-- SQL statements normally end with semicolon (;)
-- SQLite dot commands normally do NOT need semicolon.


-- ============================================================
-- END OF SQLITE3 BASIC PRACTICAL CODE SHEET
-- ============================================================
