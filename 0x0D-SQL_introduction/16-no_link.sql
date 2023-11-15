--  lists all records in second_table in hbtn_0c_0 database

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
