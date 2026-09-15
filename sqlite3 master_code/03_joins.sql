-- ============================================
-- UNIT 1 : JOIN
-- SQLite
-- ============================================

-- Create Department Table
CREATE TABLE department (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
);

-- Create Employee Table
CREATE TABLE employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    salary INTEGER,
    dept_id INTEGER
);


-- Insert Data
INSERT INTO department VALUES (1, 'IT');
INSERT INTO department VALUES (2, 'HR');
INSERT INTO department VALUES (3, 'Sales');

INSERT INTO employee VALUES (101, 'Rahul', 30000, 1);
INSERT INTO employee VALUES (102, 'Amit', 40000, 2);
INSERT INTO employee VALUES (103, 'Neha', 35000, 1);
INSERT INTO employee VALUES (104, 'Priya', 45000, 3);


-- ============================================
-- INNER JOIN
-- ============================================

SELECT employee.emp_name,
       department.dept_name
FROM employee
INNER JOIN department
ON employee.dept_id = department.dept_id;

-- Output:
-- Rahul|IT
-- Amit|HR
-- Neha|IT
-- Priya|Sales


-- ============================================
-- LEFT JOIN
-- ============================================

SELECT employee.emp_name,
       department.dept_name
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id;

-- Output:
-- Rahul|IT
-- Amit|HR
-- Neha|IT
-- Priya|Sales


-- ============================================
-- END OF JOIN
-- ============================================
