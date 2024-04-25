-- Email validation to sent
-- Creates a trigger that resets the attribute valid_email
-- only when the email has been changed.
DELIMITER $$

-- Drop the trigger if it exists to avoid errors on re-creation
DROP TRIGGER IF EXISTS reset_valid_email $$

-- Create the trigger
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
