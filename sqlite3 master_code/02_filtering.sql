-- ============================================
-- UNIT 1 : DATA FILTERING
-- SQLite
-- ============================================


-- ============================================
-- 1. CREATE TABLE
-- ============================================

CREATE TABLE employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    salary INTEGER,
    city TEXT,
    department TEXT
);


-- ============================================
-- 2. INSERT DATA
-- ============================================

INSERT INTO employee VALUES
(101, 'Rahul', 30000, 'Surat', 'IT');

INSERT INTO employee VALUES
(102, 'Amit', 40000, 'Ahmedabad', 'HR');

INSERT INTO employee VALUES
(103, 'Neha', 35000, 'Surat', 'IT');

INSERT INTO employee VALUES
(104, 'Priya', 45000, 'Vadodara', 'Sales');

INSERT INTO employee VALUES
(105, 'Raj', 25000, 'Surat', 'Sales');


-- ============================================
-- 3. DISPLAY ALL DATA
-- ============================================

SELECT * FROM employee;

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 102|Amit|40000|Ahmedabad|HR
-- 103|Neha|35000|Surat|IT
-- 104|Priya|45000|Vadodara|Sales
-- 105|Raj|25000|Surat|Sales


-- ============================================
-- 4. WHERE
-- ============================================

SELECT * FROM employee
WHERE city = 'Surat';

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 103|Neha|35000|Surat|IT
-- 105|Raj|25000|Surat|Sales


-- ============================================
-- 5. COMPARISON OPERATOR
-- ============================================

SELECT * FROM employee
WHERE salary > 30000;

-- Output:
-- 102|Amit|40000|Ahmedabad|HR
-- 103|Neha|35000|Surat|IT
-- 104|Priya|45000|Vadodara|Sales


-- ============================================
-- 6. BETWEEN
-- ============================================

SELECT * FROM employee
WHERE salary BETWEEN 30000 AND 40000;

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 102|Amit|40000|Ahmedabad|HR
-- 103|Neha|35000|Surat|IT


-- ============================================
-- 7. IN
-- ============================================

SELECT * FROM employee
WHERE city IN ('Surat', 'Ahmedabad');

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 102|Amit|40000|Ahmedabad|HR
-- 103|Neha|35000|Surat|IT
-- 105|Raj|25000|Surat|Sales


-- ============================================
-- 8. NOT IN
-- ============================================

SELECT * FROM employee
WHERE city NOT IN ('Surat');

-- Output:
-- 102|Amit|40000|Ahmedabad|HR
-- 104|Priya|45000|Vadodara|Sales


-- ============================================
-- 9. AND
-- ============================================

SELECT * FROM employee
WHERE city = 'Surat'
AND salary > 30000;

-- Output:
-- 103|Neha|35000|Surat|IT


-- ============================================
-- 10. OR
-- ============================================

SELECT * FROM employee
WHERE city = 'Surat'
OR city = 'Vadodara';

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 103|Neha|35000|Surat|IT
-- 104|Priya|45000|Vadodara|Sales
-- 105|Raj|25000|Surat|Sales


-- ============================================
-- 11. LIKE
-- ============================================

SELECT * FROM employee
WHERE emp_name LIKE 'R%';

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 105|Raj|25000|Surat|Sales


-- ============================================
-- 12. WILDCARDS
-- ============================================

-- % = Zero or more characters
SELECT * FROM employee
WHERE emp_name LIKE 'R%';

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 105|Raj|25000|Surat|Sales


-- _ = Exactly one character
SELECT * FROM employee
WHERE emp_name LIKE '_a%';

-- Output:
-- 105|Raj|25000|Surat|Sales


-- Names ending with 'a'
SELECT * FROM employee
WHERE emp_name LIKE '%a';

-- Output:
-- 103|Neha|35000|Surat|IT
-- 104|Priya|45000|Vadodara|Sales


-- Names containing 'h'
SELECT * FROM employee
WHERE emp_name LIKE '%h%';

-- Output:
-- 101|Rahul|30000|Surat|IT
-- 103|Neha|35000|Surat|IT


-- ============================================
-- 13. DISTINCT
-- ============================================

SELECT DISTINCT city
FROM employee;

-- Output:
-- Surat
-- Ahmedabad
-- Vadodara


-- ============================================
-- 14. ORDER BY ASCENDING
-- ============================================

SELECT * FROM employee
ORDER BY salary ASC;

-- Output:
-- 105|Raj|25000|Surat|Sales
-- 101|Rahul|30000|Surat|IT
-- 103|Neha|35000|Surat|IT
-- 102|Amit|40000|Ahmedabad|HR
-- 104|Priya|45000|Vadodara|Sales


-- ============================================
-- 15. ORDER BY DESCENDING
-- ============================================

SELECT * FROM employee
ORDER BY salary DESC;

-- Output:
-- 104|Priya|45000|Vadodara|Sales
-- 102|Amit|40000|Ahmedabad|HR
-- 103|Neha|35000|Surat|IT
-- 101|Rahul|30000|Surat|IT
-- 105|Raj|25000|Surat|Sales


-- ============================================
-- 16. GROUP BY
-- ============================================

SELECT city, COUNT(*)
FROM employee
GROUP BY city;

-- Output:
-- Ahmedabad|1
-- Surat|3
-- Vadodara|1


-- ============================================
-- 17. HAVING
-- ============================================

SELECT city, COUNT(*)
FROM employee
GROUP BY city
HAVING COUNT(*) > 1;

-- Output:
-- Surat|3


-- ============================================
-- 18. CASE
-- ============================================

SELECT emp_name, salary,
CASE
    WHEN salary >= 40000 THEN 'High Salary'
    WHEN salary >= 30000 THEN 'Medium Salary'
    ELSE 'Low Salary'
END AS salary_category
FROM employee;

-- Output:
-- Rahul|30000|Medium Salary
-- Amit|40000|High Salary
-- Neha|35000|Medium Salary
-- Priya|45000|High Salary
-- Raj|25000|Low Salary


-- ============================================
-- WILDCARD QUICK NOTES
-- ============================================

-- %  = Zero or more characters
-- _  = Exactly one character


-- ============================================
-- END OF DATA FILTERING
-- ============================================
