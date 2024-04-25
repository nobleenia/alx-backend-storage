-- Average score
-- Creates a stored procedure ComputeAverageScoreForUser
-- that computes and stores the average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Variable to store the calculated average score
    DECLARE calculated_avg FLOAT;

    -- Calculate the average score for the given user_id
    SELECT AVG(score) INTO calculated_avg FROM corrections WHERE user_id = user_id;

    -- Update the user's average_score with the calculated average
    UPDATE users SET average_score = calculated_avg WHERE id = user_id;
END$$

DELIMITER ;
