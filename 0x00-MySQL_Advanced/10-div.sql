-- Safe divide
-- Creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0
-- if the second number is equal to 0.
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    -- Check if the denominator is zero
    IF b = 0 THEN
        RETURN 0;
    ELSE
        -- Perform the division if the denominator is not zero
        RETURN a / b;
    END IF;
END$$

DELIMITER ;
