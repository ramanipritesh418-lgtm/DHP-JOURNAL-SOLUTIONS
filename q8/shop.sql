-- ============================================================
-- Q.8 Consider the following tables ACCESSORIES, SHOP & SHOP_LOG
-- ============================================================

-- PART (A)
-- Write SQL statements for the following:


-- 1. Display NAME and PRICE of all accessories
--    in ascending order of price.

SELECT NAME, PRICE
FROM ACCESSORIES
ORDER BY PRICE ASC;


-- 2. Display ID and SNAME of shops located in Nehru Place.

SELECT ID, SNAME
FROM SHOP
WHERE AREA = 'Nehru Place';


-- 3. Display minimum and maximum price of each
--    accessory name.

SELECT NAME, MIN(PRICE) AS MIN_PRICE, MAX(PRICE) AS MAX_PRICE
FROM ACCESSORIES
GROUP BY NAME;


-- 4. Display NAME, PRICE of accessories along with
--    their shop's SNAME.

SELECT A.NAME, A.PRICE, S.SNAME
FROM ACCESSORIES A, SHOP S
WHERE A.ID = S.ID;


-- 5. Create a trigger T1 which executes after inserting
--    a record into SHOP.

CREATE TRIGGER T1
AFTER INSERT ON SHOP
FOR EACH ROW
BEGIN
    INSERT INTO SHOP_LOG (ID, ACTION_DATE)
    VALUES (:NEW.ID, SYSDATE);
END;


-- ============================================================
-- PART (B)
-- Outputs
-- ============================================================


-- 1. Display distinct names of accessories whose price
--    is greater than or equal to 5000.

SELECT DISTINCT NAME
FROM ACCESSORIES
WHERE PRICE >= 5000;

-- OUTPUT:
-- Mother Board
-- Hard Disk
-- LCD


-- 2. Display area and number of shops in each area.

SELECT AREA, COUNT(*)
FROM SHOP
GROUP BY AREA;

-- OUTPUT:
-- CP          2
-- GK II       1
-- Nehru Place 2


-- 3. Display the number of distinct areas in SHOP.

SELECT COUNT(DISTINCT AREA)
FROM SHOP;

-- OUTPUT:
-- 3


-- 4. Display NAME and 5% discount of accessories whose
--    shop IDs are S02 and S03.

SELECT NAME, PRICE * 0.05 AS DISCOUNT
FROM ACCESSORIES
WHERE ID IN ('S02', 'S03');

-- OUTPUT:
-- Keyboard       25
-- Mother Board   650
-- Keyboard       20
-- Hard Disk      225
