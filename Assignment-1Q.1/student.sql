-- ============================================================
-- PRACTICAL ASSIGNMENT - 1
-- DATABASE HANDLING USING PYTHON
-- SQLITE
-- ============================================================


-- ============================================================
-- QUESTION
-- ============================================================

/*
PRACTICAL ASSIGNMENT – 1

1. Create Student Table with appropriate constraints.

STUDENT(
    sno number primary key,
    sname text(20),
    age number,
    total_marks number
)

Write query to perform following tasks:

1) Store the table data into a database and display the list
   of tables in the database.

2) List out top three records from the table.

3) Display all records from table whose age is not less than 18.

4) Display age of student whose sno is 5.
*/


-- ============================================================
-- STEP 1: CREATE / OPEN SQLITE DATABASE
-- ============================================================

/*
SQLite does not use CREATE DATABASE command.

The database is a file.

Database Name:
Student.db

Using DB Browser for SQLite:

1. Open DB Browser for SQLite.
2. Click "New Database".
3. Enter database name: Student.db
4. Click "Save".
5. Open "Execute SQL" tab.
*/


-- ============================================================
-- STEP 2: CREATE STUDENT TABLE
-- ============================================================

CREATE TABLE STUDENT (
    sno INTEGER PRIMARY KEY,
    sname TEXT(20),
    age INTEGER,
    total_marks INTEGER
);


-- ============================================================
-- STEP 3: INSERT RECORDS INTO STUDENT TABLE
-- ============================================================

INSERT INTO STUDENT
VALUES (1, 'Amit', 19, 450);

INSERT INTO STUDENT
VALUES (2, 'Rahul', 17, 380);

INSERT INTO STUDENT
VALUES (3, 'Neha', 20, 470);

INSERT INTO STUDENT
VALUES (4, 'Ravi', 18, 420);

INSERT INTO STUDENT
VALUES (5, 'Pooja', 21, 490);


-- ============================================================
-- STEP 4: DISPLAY ALL STUDENT RECORDS
-- ============================================================

SELECT * FROM STUDENT;


-- ============================================================
-- TASK 1
-- Store table data into database and display list of tables
-- ============================================================

SELECT name
FROM sqlite_master
WHERE type = 'table';


-- ============================================================
-- TASK 2
-- List out top three records from the table
-- ============================================================

SELECT *
FROM STUDENT
LIMIT 3;


-- ============================================================
-- TASK 3
-- Display all records whose age is not less than 18
-- "Not less than 18" means age >= 18
-- ============================================================

SELECT *
FROM STUDENT
WHERE age >= 18;


-- ============================================================
-- TASK 4
-- Display age of student whose sno is 5
-- ============================================================

SELECT age
FROM STUDENT
WHERE sno = 5;


-- ============================================================
-- END OF PRACTICAL ASSIGNMENT - 1
-- ============================================================
