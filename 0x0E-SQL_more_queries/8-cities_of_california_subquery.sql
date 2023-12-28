--  lists all cities of California in hbtn_0d_usa

SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
GROUP BY id ORDER BY id ASC;