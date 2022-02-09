CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');

-- outer join combines this query with the inner join
select * 
from basket_a 
where i
    fruit_a not in (select fruit_b from basket_b);

select *
from basket_a
inner join basket_b on fruit_a=fruit_b;


-- UNION statement combines results of queries row-wise
-- stacking them on top of each other

--(select *,null,null
select * 
from
(
    (select a,fruit_a,null,null
    from basket_a 
    where
        fruit_a not in (select fruit_b from basket_b)
    )
    union
    (
    select *
    from basket_a
    inner join basket_b on fruit_a=fruit_b
    )
) as t
order by a
;


select *
from basket_b
full join basket_a ON fruit_a=fruit_b;
