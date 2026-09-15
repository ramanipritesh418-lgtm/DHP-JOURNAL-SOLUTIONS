-- ============================================
-- UNIT 1 : TRANSACTION
-- SQLite
-- ============================================


-- ============================================
-- 1. CREATE TABLE
-- ============================================

CREATE TABLE account (
    id INTEGER PRIMARY KEY,
    name TEXT,
    balance INTEGER
);

-- Output:
-- Table created successfully


-- ============================================
-- 2. INSERT DATA
-- ============================================

INSERT INTO account VALUES (1, 'Rahul', 5000);
INSERT INTO account VALUES (2, 'Amit', 3000);

-- Output:
-- Data inserted successfully


-- ============================================
-- 3. DISPLAY DATA
-- ============================================

SELECT * FROM account;

-- Output:
-- 1|Rahul|5000
-- 2|Amit|3000


-- ============================================
-- 4. COMMIT TRANSACTION
-- ============================================

BEGIN TRANSACTION;

UPDATE account
SET balance = balance - 1000
WHERE id = 1;

UPDATE account
SET balance = balance + 1000
WHERE id = 2;

COMMIT;


-- Display Updated Data
SELECT * FROM account;

-- Output:
-- 1|Rahul|4000
-- 2|Amit|4000


-- ============================================
-- 5. ROLLBACK TRANSACTION
-- ============================================

BEGIN TRANSACTION;

UPDATE account
SET balance = balance - 500
WHERE id = 1;

ROLLBACK;


-- Display Data After Rollback
SELECT * FROM account;

-- Output:
-- 1|Rahul|4000
-- 2|Amit|4000


-- ============================================
-- END OF TRANSACTION
-- ============================================
