-- Add bonus
-- Creates a stored procedure AddBonus
-- that adds a new correction for a student
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Variable to hold project_id
    DECLARE project_id INT DEFAULT 0;

    -- Check if the project exists and get its ID
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- If the project does not exist, create it
    IF project_id = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID(); -- Get the ID of the newly inserted project
    END IF;

    -- Insert the correction record
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$

DELIMITER ;
