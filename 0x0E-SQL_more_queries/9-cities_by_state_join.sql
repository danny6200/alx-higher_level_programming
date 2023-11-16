-- Reads cities contained in hbtn_0d_usa.
-- A record should have: cities.id - cities.name - states.name
-- Records must be sorted in ascending order by cities.id


SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
