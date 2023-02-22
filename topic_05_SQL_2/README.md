# Topic 05: SQL II

## Announcements

Get a good workflow going for your assignments

<img src=gates.jpg width=600px />

<br/>

<img src=the-three-chief-virtues-of-a-programmer-are-laziness-impatience-and-hubris-larry-wall.jpg width=600px />

## Lecture

What you must know for the homework/midterm/quiz

1. skipping section 6 of <https://www.postgresqltutorial.com/>
    1. syntactic sugar for complicated GROUP BY clauses
    1. good to know, but they're not "hard" concepts
    1. "less technical" technical interviews often ask about these topics

1. subqueries
    1. section 7 of https://www.postgresqltutorial.com/
    1. compared to joins (power):
        1. every join can be written as a cross join + subquery
        1. some subqueries can be written as joins
        1. a subquery cannot be written as a join if it contains an aggregate function
    1. compared to joins (general):
        1. subqueries are easier for beginners to understand than joins
        1. joins are easier for experts to understand
        1. which is faster depends
    1. alternative reference on subqueries vs joins: https://learnsql.com/blog/subquery-vs-join/

1. set operations
    1. section 5 of https://www.postgresqltutorial.com/
    1. most important operation is `union` vs `union all`

1. joins
    1. sections 3 of https://www.postgresqltutorial.com/
    1. the "standard" explanation of joins uses venn diagrams, but this is technically not correct since relations are not sets; see: https://blog.jooq.org/2016/07/05/say-no-to-venn-diagrams-when-explaining-joins/

       <a href=https://www.reddit.com/r/ProgrammerHumor/comments/a0qp9x/this_ones_for_all_the_sql_developers_out_there/><img src=joins.jpg width=300px /></a>

    1. if this all seems weird/hard/confusing... that's because it is

       <img src=cmcqtycmbmg51.jpg width=300px />

1. arrays
    1. postgresql specific extension, not on quiz
    1. a "denormalized" method for storing join tables
        1. there's speed/memory tradeoffs between different representations which we'll talk about later
        1. for now, just focus on using arrays to get the right answer
    1. https://www.postgresqltutorial.com/postgresql-array/
    1. `unnest` is the only array function you'll want to use (for this week's homework)

<!--
1. `CREATE TABLE`
    1. https://www.postgresqltutorial.com/postgresql-create-table/
    1. https://www.postgresqltutorial.com/postgresql-data-types/
    1. Examples in the tutorial use `VARCHAR`, but you shouldn't use this type in postgresql.
       Instead, you should use the `TEXT` type.
       See: https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_varchar.28n.29_by_default

1. `INSERT` / `UPDATE` / `DELETE`
    1. <img src=Strip-Bas-ed-eonnée-effacée-650-finalenglish.jpg width=60%/>
    1. sections 9 of https://www.postgresqltutorial.com/
-->
