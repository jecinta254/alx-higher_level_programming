-- listing all records of the table second_table of db hbtn_0c_0
-- records sorted by score in the descending order, where score >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
