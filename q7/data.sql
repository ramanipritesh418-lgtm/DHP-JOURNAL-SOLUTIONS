/*
==========================================================
Q.7 Consider the following tables SCHOOL & ADMIN and 
    answer the following:

Table: SCHOOL
+------+--------------+-----------+------------+---------+------------+
| CODE | TEACHERNAME  | SUBJECT   | DOB        | PERIODS | EXPERIENCE |
+------+--------------+-----------+------------+---------+------------+
| 1001 | Ravi Shankar | English   | 12/03/2000 |   24    |     10     |
| 1009 | Pooja Rai    | Physics   | 03/09/1998 |   26    |     12     |
| 1203 | Lisa Anand   | English   | 09/04/2000 |   27    |      5     |
| 1045 | Yashraj      | Maths     | 24/08/2000 |   24    |     15     |
| 1123 | Gaman        | Physics   | 16/07/1999 |   28    |      3     |
| 1167 | Harish B     | Chemistry | 19/10/1999 |   27    |      5     |
| 1215 | Umesh        | Physics   | 11/05/1998 |   22    |     16     |
+------+--------------+-----------+------------+---------+------------+

Table: ADMIN
+------+--------+-----------------+
| CODE | GENDER | DESIGNATION     |
+------+--------+-----------------+
| 1001 | Male   | Vice Principal  |
| 1009 | Female | Co-ordinator    |
| 1203 | Female | Co-ordinator    |
| 1045 | Male   | HOD             |
| 1123 | Male   | Senior Teacher  |
| 1167 | Male   | Senior Teacher  |
| 1215 | Male   | HOD             |
+------+--------+-----------------+
==========================================================
*/


-- ==========================================================
-- Q1. Display TEACHERNAME, PERIODS of all teachers whose 
--     periods are more than 25.
-- ==========================================================
SELECT TEACHERNAME, PERIODS 
FROM SCHOOL 
WHERE PERIODS > 25;

/*
OUTPUT:
+--------------+---------+
| TEACHERNAME  | PERIODS |
+--------------+---------+
| Pooja Rai    |   26    |
| Lisa Anand   |   27    |
| Gaman        |   28    |
| Harish B     |   27    |
+--------------+---------+
*/


-- ==========================================================
-- Q2. Display all the information from the table SCHOOL in 
--     descending order of experience.
-- ==========================================================
SELECT * 
FROM SCHOOL 
ORDER BY EXPERIENCE DESC;

/*
OUTPUT:
+------+--------------+-----------+------------+---------+------------+
| CODE | TEACHERNAME  | SUBJECT   | DOB        | PERIODS | EXPERIENCE |
+------+--------------+-----------+------------+---------+------------+
| 1215 | Umesh        | Physics   | 11/05/1998 |   22    |     16     |
| 1045 | Yashraj      | Maths     | 24/08/2000 |   24    |     15     |
| 1009 | Pooja Rai    | Physics   | 03/09/1998 |   26    |     12     |
| 1001 | Ravi Shankar | English   | 12/03/2000 |   24    |     10     |
| 1203 | Lisa Anand   | English   | 09/04/2000 |   27    |      5     |
| 1167 | Harish B     | Chemistry | 19/10/1999 |   27    |      5     |
| 1123 | Gaman        | Physics   | 16/07/1999 |   28    |      3     |
+------+--------------+-----------+------------+---------+------------+

Note: Lisa Anand and Harish B both have experience 5, 
so their relative order may vary between database engines.
*/


-- ==========================================================
-- Q3. Display DESIGNATION without duplicate entries from 
--     the table ADMIN.
-- ==========================================================
SELECT DISTINCT DESIGNATION 
FROM ADMIN;

/*
OUTPUT:
+------------------+
| DESIGNATION      |
+------------------+
| Vice Principal   |
| Co-ordinator     |
| HOD              |
| Senior Teacher   |
+------------------+
*/


-- ==========================================================
-- Q4. Display TEACHERNAME, CODE and corresponding 
--     DESIGNATION from tables SCHOOL and ADMIN of male 
--     teachers.
-- ==========================================================
SELECT S.TEACHERNAME, S.CODE, A.DESIGNATION
FROM SCHOOL S, ADMIN A
WHERE S.CODE = A.CODE AND A.GENDER = 'Male';

/*
OUTPUT:
+--------------+------+-----------------+
| TEACHERNAME  | CODE | DESIGNATION     |
+--------------+------+-----------------+
| Ravi Shankar | 1001 | Vice Principal  |
| Yashraj      | 1045 | HOD             |
| Gaman        | 1123 | Senior Teacher  |
| Harish B     | 1167 | Senior Teacher  |
| Umesh        | 1215 | HOD             |
+--------------+------+-----------------+
*/
