-- lists all records of table second_table of db
-- Doesnot list rows without name value
-- Results to display the score and the name in that order
-- Records to be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
