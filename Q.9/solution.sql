/*
==========================================================
Q.9 Consider the following tables ACTIVITY & COACH and 
    answer (a) & (b) parts of this question.

Table: ACTIVITY
+-------+---------------+-------------+------------------+------------+---------------+
| ACode | ActivityName  | Stadium     | ParticipantsNum  | PrizeMoney | ScheduleDate  |
+-------+---------------+-------------+------------------+------------+---------------+
| 1001  | Relay 100x4   | Star Annex  |       16         |   10000    | 23-Jan-2004   |
| 1002  | High Jump     | Star Annex  |       10         |   12000    | 12-Dec-2003   |
| 1003  | Shot Put      | Super Power |       10         |    8000    | 24-Feb-2004   |
| 1005  | Long Jump     | Star Annex  |       12         |    9000    | 01-Jan-2004   |
| 1008  | Discuss Throw | Super Power |       10         |   15000    | 29-Mar-2004   |
+-------+---------------+-------------+------------------+------------+---------------+

Table: COACH
+-------+---------------+-------+
| PCode | Name          | ACode |
+-------+---------------+-------+
|   1   | Ahmad Hussain | 1001  |
|   2   | Ravinder      | 1008  |
|   3   | Jamila        | 1001  |
|   4   | Naaz          | 1003  |
+-------+---------------+-------+

(a) Write SQL commands for the following statements:
1. To display the names of all activities with their 
   ACodes, records in descending order.
2. To display sum of prizemoney for the activities 
   played in each of the stadium separately.
3. To display the coach's name & ACodes in ascending 
   order of ACode from the table COACH.
4. To display the content of the ACTIVITY table whose 
   schedule date is earlier than 01-01-2004, in ascending 
   order of participants num.

(b) Give the output of the following SQL queries:
1. SELECT COUNT(DISTINCT PARTICIPANTSNUM) FROM ACTIVITY;
2. SELECT MAX(SCHEDULEDATE), MIN(SCHEDULEDATE) FROM ACTIVITY;
3. SELECT NAME, ACTIVITYNAME FROM ACTIVITY A, COACH C 
   WHERE A.ACODE = C.ACODE AND A.PARTICIPANTSNUM = 10;
4. SELECT DISTINCT ACODE FROM COACH;
==========================================================
*/


-- ==========================================================
-- SCHEMA + DATA (SQLite3) -- run this first to create and 
-- populate the tables, then run the queries below.
-- ==========================================================

DROP TABLE IF EXISTS ACTIVITY;
DROP TABLE IF EXISTS COACH;

CREATE TABLE ACTIVITY (
    ACODE            INTEGER PRIMARY KEY,
    ACTIVITYNAME     TEXT,
    STADIUM          TEXT,
    PARTICIPANTSNUM  INTEGER,
    PRIZEMONEY       INTEGER,
    SCHEDULEDATE     TEXT
);

CREATE TABLE COACH (
    PCODE  INTEGER PRIMARY KEY,
    NAME   TEXT,
    ACODE  INTEGER,
    FOREIGN KEY (ACODE) REFERENCES ACTIVITY(ACODE)
);

INSERT INTO ACTIVITY VALUES (1001, 'Relay 100x4',   'Star Annex',  16, 10000, '23-Jan-2004');
INSERT INTO ACTIVITY VALUES (1002, 'High Jump',     'Star Annex',  10, 12000, '12-Dec-2003');
INSERT INTO ACTIVITY VALUES (1003, 'Shot Put',      'Super Power', 10,  8000, '24-Feb-2004');
INSERT INTO ACTIVITY VALUES (1005, 'Long Jump',     'Star Annex',  12,  9000, '01-Jan-2004');
INSERT INTO ACTIVITY VALUES (1008, 'Discuss Throw', 'Super Power', 10, 15000, '29-Mar-2004');

INSERT INTO COACH VALUES (1, 'Ahmad Hussain', 1001);
INSERT INTO COACH VALUES (2, 'Ravinder',      1008);
INSERT INTO COACH VALUES (3, 'Jamila',        1001);
INSERT INTO COACH VALUES (4, 'Naaz',          1003);


-- ==========================================================
-- (a) 1. Display names of all activities with their ACodes,
--        records in descending order.
-- ==========================================================
SELECT ACTIVITYNAME, ACODE 
FROM ACTIVITY 
ORDER BY ACODE DESC;

/*
OUTPUT:
+---------------+-------+
| ACTIVITYNAME  | ACODE |
+---------------+-------+
| Discuss Throw | 1008  |
| Long Jump     | 1005  |
| Shot Put      | 1003  |
| High Jump     | 1002  |
| Relay 100x4   | 1001  |
+---------------+-------+
*/


-- ==========================================================
-- (a) 2. Display sum of prizemoney for the activities 
--        played in each of the stadium separately.
-- ==========================================================
SELECT STADIUM, SUM(PRIZEMONEY) AS TOTAL_PRIZEMONEY
FROM ACTIVITY 
GROUP BY STADIUM;

/*
OUTPUT:
+-------------+------------------+
| STADIUM     | TOTAL_PRIZEMONEY |
+-------------+------------------+
| Star Annex  |      31000       |
| Super Power |      23000       |
+-------------+------------------+
*/


-- ==========================================================
-- (a) 3. Display coach's name & ACodes in ascending order 
--        of ACode from the table COACH.
-- ==========================================================
SELECT NAME, ACODE 
FROM COACH 
ORDER BY ACODE ASC;

/*
OUTPUT:
+---------------+-------+
| NAME          | ACODE |
+---------------+-------+
| Ahmad Hussain | 1001  |
| Jamila        | 1001  |
| Naaz          | 1003  |
| Ravinder      | 1008  |
+---------------+-------+
*/


-- ==========================================================
-- (a) 4. Display content of ACTIVITY table whose schedule 
--        date is earlier than 01-01-2004, in ascending 
--        order of participants num.
-- ==========================================================
SELECT * 
FROM ACTIVITY 
WHERE SCHEDULEDATE < '01-JAN-2004' 
ORDER BY PARTICIPANTSNUM ASC;

/*
OUTPUT:
+-------+---------------+-------------+------------------+------------+---------------+
| ACODE | ACTIVITYNAME  | STADIUM     | PARTICIPANTSNUM  | PRIZEMONEY | SCHEDULEDATE  |
+-------+---------------+-------------+------------------+------------+---------------+
| 1002  | High Jump     | Star Annex  |       10         |   12000    | 12-Dec-2003   |
+-------+---------------+-------------+------------------+------------+---------------+

Note: Only "High Jump" (12-Dec-2003) falls strictly before 
01-Jan-2004 based on the given dates.
*/


-- ==========================================================
-- (b) 1. Count of distinct participants numbers
-- ==========================================================
SELECT COUNT(DISTINCT PARTICIPANTSNUM) 
FROM ACTIVITY;

/*
OUTPUT:
+----------------------------------+
| COUNT(DISTINCT PARTICIPANTSNUM)  |
+----------------------------------+
|               3                  |
+----------------------------------+
(distinct values: 16, 10, 12)
*/


-- ==========================================================
-- (b) 2. Max & Min schedule date
-- ==========================================================
SELECT MAX(SCHEDULEDATE), MIN(SCHEDULEDATE) 
FROM ACTIVITY;

/*
OUTPUT:
+---------------------+---------------------+
| MAX(SCHEDULEDATE)   | MIN(SCHEDULEDATE)   |
+---------------------+---------------------+
| 29-Mar-2004         | 12-Dec-2003         |
+---------------------+---------------------+
*/


-- ==========================================================
-- (b) 3. Name & activity name where participants = 10
-- ==========================================================
SELECT NAME, ACTIVITYNAME 
FROM ACTIVITY A, COACH C 
WHERE A.ACODE = C.ACODE AND A.PARTICIPANTSNUM = 10;

/*
OUTPUT:
+----------+---------------+
| NAME     | ACTIVITYNAME  |
+----------+---------------+
| Naaz     | Shot Put      |
| Ravinder | Discuss Throw |
+----------+---------------+

Note: High Jump (ACode 1002) also has 10 participants, 
but no coach record has ACode 1002, so it's excluded 
by the join.
*/


-- ==========================================================
-- (b) 4. Distinct ACodes from COACH
-- ==========================================================
SELECT DISTINCT ACODE 
FROM COACH;

/*
OUTPUT:
+-------+
| ACODE |
+-------+
| 1001  |
| 1008  |
| 1003  |
+-------+
*/
