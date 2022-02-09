# Week 04: More SQL

## Announcements

**Wed 9 Feb**:

1. week_02 hw updated in sakai
    1. mostly 15/15
    1. a few students are missing important files, and got docked points; I'm willing to regrade if this was just a mistake with git
    1. recall that late submissions are allowed, -20%/day; usually better to submit correct and late than incorrect and on time

1. recall: this week only, you can redo the POSIX-shell quiz

1. 3 students with <5 on week_00 lab have not resubmitted for a regrade; today is your last chance

1. current median grade in the class: 92.6%

1. TA update

1. I would normally do a quiz at this point... but there'll be a baby any day now

## Lecture

What you must know for the homework/midterm

<!--
1. skipping sections 5,6 of https://www.postgresqltutorial.com/
    1. good to know, but they're not "hard" concepts
    1. I personally don't use them frequently
-->

1. subqueries
    1. section 7 of https://www.postgresqltutorial.com/
    1. compared to joins:
        1. every join can be written as a cross join + subquery
        1. some subqueries can be written as joins
        1. a subquery cannot be written as a join if it contains an aggregate function
    1. alternative reference on subqueries vs joins: https://learnsql.com/blog/subquery-vs-join/

1. set operations
    1. section 5 of https://www.postgresqltutorial.com/
    1. most important operation is `union` vs `union all`

1. joins
    1. sections 3 of https://www.postgresqltutorial.com/
    1. the "standard" explanation of joins uses venn diagrams, but this is technically not correct since relations are not sets; see: https://blog.jooq.org/2016/07/05/say-no-to-venn-diagrams-when-explaining-joins/
    1. joins meme

       <a href=https://www.reddit.com/r/ProgrammerHumor/comments/a0qp9x/this_ones_for_all_the_sql_developers_out_there/><img src=joins.jpg width=300px /></a>

       <img src=cmcqtycmbmg51.jpg width=300px />

1. arrays
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
