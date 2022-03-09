--  lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT name FROM states UNION EXCEPT SELECT name FROM cities ORDER BY cities.id
