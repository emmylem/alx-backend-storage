--  creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);
    
    -- Compute the average score for the user
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
    
    -- Update or insert the average score for the user
    INSERT INTO average_scores (user_id, score)
    VALUES (user_id, avg_score)
    ON DUPLICATE KEY UPDATE score = avg_score;
END;
$$

DELIMITER ;

