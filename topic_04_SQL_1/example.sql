SELECT last_name || ', ' || first_name AS "full name" 
FROM actor
ORDER BY first_name DESC,last_name DESC 
LIMIT 10;

-- SQL is not case sensitive
select last_name || ', ' || first_name AS "full name"
from actor
order by first_name DESC,last_name DESC
LIMIT 10;


select 'I''m not ' || last_name || ', ' || first_name AS "full name"
from actor
order by first_name DESC,last_name DESC
LIMIT 10;



select $blah$I'm $$not$$ $blah$ || last_name || ', ' || first_name AS "full "" name"
from actor
order by first_name DESC,last_name DESC
LIMIT 10;
