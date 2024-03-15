-- lists the number of records with same score in table second_table
-- The result should display: score
-- and number of records for this score with label number
-- The list is sorted by number of records-descending
SELECT score, count(*) AS number FROM second_table
GROUP BY score ORDER BY score DESC;
