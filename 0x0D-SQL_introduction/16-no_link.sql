-- Lists all records of the table second_table
-- don’t list rows without a name value
-- displays the score and the name
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
