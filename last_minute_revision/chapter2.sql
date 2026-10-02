/*
===========================================================
DHP-303 DATABASE HANDLING USING PYTHON
UNIT 2 - DATABASE BACKUP AND CSV HANDLING
COMPLETE SQLITE CMD CODE SHEET
===========================================================

Topics Covered:
1. Dump entire database
2. Dump specific table
3. Dump table structure
4. Dump data of table using INSERT statements
5. Import CSV into a new table
6. Import CSV into an existing table
7. Export table data to CSV

SQLite CMD:
C:\sqlite>sqlite3 company.db
===========================================================
*/


/* ========================================================
   PART 1 - OPEN DATABASE AND CHECK TABLES
   ======================================================== */

/*
CMD:
C:\sqlite>sqlite3 company.db
*/

.databases
.tables

/*
Expected Output:

main: C:\sqlite\company.db r/w

Tables:
company
student
*/


/* ========================================================
   PART 2 - CREATE SAMPLE TABLES AND DATA
   ======================================================== */

CREATE TABLE IF NOT EXISTS company (
    e_id INTEGER PRIMARY KEY,
    e_name TEXT,
    address TEXT,
    age INTEGER
);

INSERT INTO company VALUES (1, 'Paul', 'California', 32);
INSERT INTO company VALUES (2, 'Allen', 'Texas', 25);
INSERT INTO company VALUES (3, 'Teddy', 'Norway', 23);
INSERT INTO company VALUES (4, 'Mark', 'Rich-Mond', 25);
INSERT INTO company VALUES (5, 'David', 'Texas', 27);

CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);

INSERT INTO student VALUES (1, 'Rahul', 'Surat');
INSERT INTO student VALUES (2, 'Amit', 'Ahmedabad');
INSERT INTO student VALUES (3, 'Jay', 'Vadodara');

SELECT * FROM company;

SELECT * FROM student;

/*
Expected Output:

1|Paul|California|32
2|Allen|Texas|25
3|Teddy|Norway|23
4|Mark|Rich-Mond|25
5|David|Texas|27

1|Rahul|Surat
2|Amit|Ahmedabad
3|Jay|Vadodara
*/


/* ========================================================
   PART 3 - DUMP ENTIRE DATABASE INTO A FILE
   ======================================================== */

/*
.dump
    -> Dumps the complete database structure and data.

.output
    -> Sends SQLite output to a file.
*/

.output C:/sqlite/student.sql
.dump

/*
Expected Result:

A file named:

C:/sqlite/student.sql

is created.

The file contains SQL statements such as:

CREATE TABLE company (...);
INSERT INTO company VALUES (...);

CREATE TABLE student (...);
INSERT INTO student VALUES (...);
*/

.output stdout


/* ========================================================
   PART 4 - DUMP A SPECIFIC TABLE
   ======================================================== */

/*
Syntax:

.output filename
.dump table_name
*/

.output C:/sqlite/department.sql
.dump company

/*
Expected Result:

A file named:

C:/sqlite/department.sql

is created.

It contains the structure and data
of the company table only.
*/

.output stdout


/* ========================================================
   PART 5 - DUMP TABLE STRUCTURE ONLY
   ======================================================== */

/*
.schema
    -> Displays table structure / CREATE TABLE statements.
*/

.output C:/sqlite/structure.sql
.schema

/*
Expected Result:

A file named:

C:/sqlite/structure.sql

is created.

It contains CREATE TABLE statements,
for example:

CREATE TABLE company (
    e_id INTEGER PRIMARY KEY,
    e_name TEXT,
    address TEXT,
    age INTEGER
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);
*/

.output stdout


/* ========================================================
   PART 6 - DUMP DATA USING INSERT STATEMENTS
   ======================================================== */

/*
Step 1:
Set output mode to INSERT.
*/

.mode insert

/*
Step 2:
Send output to a file.
*/

.output C:/sqlite/record.sql

/*
Step 3:
Execute SELECT statement.
*/

SELECT * FROM student;

/*
Expected Result inside record.sql:

INSERT INTO student VALUES(1,'Rahul','Surat');
INSERT INTO student VALUES(2,'Amit','Ahmedabad');
INSERT INTO student VALUES(3,'Jay','Vadodara');
*/

/*
Data from another table can also be dumped:
*/

SELECT * FROM company;

/*
Both SELECT results are written as INSERT statements
into record.sql.
*/

.output stdout

/*
Important:
Always use .output stdout after using .output filename
when you want output back on the screen.
*/


/* ========================================================
   PART 7 - CREATE CSV FILE FOR IMPORT
   ======================================================== */

/*
Create a file named:

C:/sqlite/city.csv

CSV CONTENT:

name,population
Surat,7000000
Ahmedabad,8000000
Vadodara,2000000

The first row contains column names.
*/


/* ========================================================
   PART 8 - IMPORT CSV INTO A NEW TABLE
   ======================================================== */

/*
First set CSV mode.
*/

.mode csv

/*
Import CSV file into cities table.
*/

.import C:/sqlite/city.csv cities

/*
Expected Result:

SQLite creates the cities table automatically
using the first CSV row as column names.

Expected schema:

CREATE TABLE cities(
    "name" TEXT,
    "population" TEXT
);
*/


/* Check table structure */

.schema cities

/*
Expected Output:

CREATE TABLE cities("name" TEXT, "population" TEXT);
*/


/* Check imported data */

SELECT * FROM cities;

/*
Expected Output:

Surat|7000000
Ahmedabad|8000000
Vadodara|2000000
*/


/* ========================================================
   PART 9 - IMPORT CSV INTO AN EXISTING TABLE
   ======================================================== */

/*
First create the table manually.
*/

CREATE TABLE IF NOT EXISTS cities2 (
    name TEXT NOT NULL,
    population INTEGER NOT NULL
);

/*
Important:
When the table already exists, SQLite treats ALL CSV rows
as data.

Therefore, the header row should be removed from CSV.

Create:

C:/sqlite/city_no_header.csv

CSV CONTENT:

Surat,7000000
Ahmedabad,8000000
Vadodara,2000000
*/


/* Set CSV mode */

.mode csv

/* Import CSV without header */

.import C:/sqlite/city_no_header.csv cities2


/* Check imported data */

SELECT * FROM cities2;

/*
Expected Output:

Surat|7000000
Ahmedabad|8000000
Vadodara|2000000
*/


/* ========================================================
   PART 10 - EXPORT TABLE DATA TO CSV
   ======================================================== */

/*
Step 1:
Turn headers ON.
*/

.headers on

/*
Step 2:
Set CSV mode.
*/

.mode csv

/*
Step 3:
Send output to CSV file.
*/

.output C:/sqlite/data.csv

/*
Step 4:
Execute SELECT query.
*/

SELECT e_id, e_name, address, age
FROM company;

/*
Expected data inside data.csv:

e_id,e_name,address,age
1,Paul,California,32
2,Allen,Texas,25
3,Teddy,Norway,23
4,Mark,Rich-Mond,25
5,David,Texas,27
*/


/* Return output to screen */

.output stdout


/* ========================================================
   PART 11 - VERIFY CSV EXPORT
   ======================================================== */

/*
The file:

C:/sqlite/data.csv

contains:

e_id,e_name,address,age
1,Paul,California,32
2,Allen,Texas,25
3,Teddy,Norway,23
4,Mark,Rich-Mond,25
5,David,Texas,27
*/


/* ========================================================
   PART 12 - USEFUL SQLITE COMMANDS
   ======================================================== */

/*
Show databases:
*/

.databases

/*
Show tables:
*/

.tables

/*
Show table structure:
*/

.schema company

/*
Show help:
*/

.help

/*
Exit SQLite:
*/

.quit


/* ========================================================
   QUICK REVISION
   ========================================================

   .dump
       -> Dump entire database

   .dump table_name
       -> Dump specific table

   .output filename
       -> Save output into file

   .output stdout
       -> Bring output back to screen

   .schema
       -> Show table structure

   .mode insert
       -> Convert SELECT output into INSERT statements

   .mode csv
       -> Set CSV mode

   .import file table
       -> Import CSV into table

   .headers on
       -> Include column names

   SELECT ...
       -> Select data for CSV export

   .quit / .exit
       -> Exit SQLite


===========================================================
IMPORTANT EXAM MEMORY TRICK
===========================================================

DATABASE BACKUP
        |
        v
    .output
        |
        v
     .dump
        |
        v
      FILE

SPECIFIC TABLE
        |
        v
.dump table_name

TABLE STRUCTURE
        |
        v
     .schema

DATA AS INSERT
        |
        v
   .mode insert
        |
        v
    .output file
        |
        v
      SELECT

CSV IMPORT
        |
        v
     .mode csv
        |
        v
.import file table

CSV EXPORT
        |
        v
  .headers on
        |
        v
    .mode csv
        |
        v
   .output data.csv
        |
        v
      SELECT

===========================================================
END OF UNIT 2 CODE SHEET
===========================================================
*/
