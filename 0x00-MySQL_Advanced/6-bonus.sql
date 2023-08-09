-- creates a stored procedure AddBonus that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score DECIMAL(10, 2))
BEGIN
    -- Insert the correction and create the project if it doesn't exist
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (
        p_user_id,
        COALESCE((SELECT id FROM projects WHERE name = p_project_name), 
                 (INSERT INTO projects (name) VALUES (p_project_name), LAST_INSERT_ID())),
        p_score
    );
END;
$$

DELIMITER ;
