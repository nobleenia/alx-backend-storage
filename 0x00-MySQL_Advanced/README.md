# 0x00. MySQL advanced

0. 0-uniq_users.sql: An SQL script that creates a table users (We are all unique!)
1. 1-country_users.sql: An SQL script that creates a table users (In and not out)
2. 2-fans.sql: An SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
3. 3-glam_rock.sql: An SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
4. 4-store.sql: An SQL script that creates a trigger that decreases the quantity of an item after adding a new order
5. 5-valid_email.sql: An SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed
6. 6-bonus.sql: An SQL script that creates a stored procedure AddBonus that adds a new correction for a student
7. 7-average_score.sql: An SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
8. 8-index_my_names.sql: An SQL script that creates an index idx_name_first on the table names and the first letter of name
9. 9-index_name_score.sql: An SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score
10. 10-div.sql: An SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0
11. 11-need_meeting.sql: An SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month