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

1. I would normally do a quiz at this point... but we'll do a "take home exercise" instead

    1. tentative due date: Wednesday 16 Feb

**Fri 11 Feb**:

1. Two new files we'll be using in lecture: `create_food*.sql`

   I recommend downloading them into your pagila folder if you want to follow along with what I'm doing

1. Using the `diff` command to understand whether your output is correct or not

   Reference: <https://en.wikipedia.org/wiki/Diff#Usage>

1. How many people have memorized the commands on the [vim cheatsheet](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)?

   About 1/4 of the class has completed the [typespeed caveat task](https://github.com/mikeizbicki/cmc-csci143/blob/2022spring/caveat_tasks/typespeed.md).

   <img src=gates.jpg width=600px />

   <br/>

   <img src=the-three-chief-virtues-of-a-programmer-are-laziness-impatience-and-hubris-larry-wall.jpg width=600px />

## Lecture

What you must know for the homework/midterm

<!--
1. skipping sections 5,6 of https://www.postgresqltutorial.com/
    1. good to know, but they're not "hard" concepts
    1. I personally don't use them frequently
-->

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
    1. the most important subqueries are for use with the `IN` and `NOT IN` operators
       ```
       SELECT * FROM a WHERE a.c1 IN (SELECT b.c2 FROM b);
       ```
       ```
       SELECT * FROM a WHERE a.c1 NOT IN (SELECT b.c2 FROM b);
       ```

1. set operations
    1. section 5 of https://www.postgresqltutorial.com/
    1. most important operation is `union` vs `union all`

1. joins
    1. sections 3 of https://www.postgresqltutorial.com/
    1. the "standard" explanation of joins uses venn diagrams, but this is technically not correct since relations are not sets; see: https://blog.jooq.org/2016/07/05/say-no-to-venn-diagrams-when-explaining-joins/

       <a href=https://www.reddit.com/r/ProgrammerHumor/comments/a0qp9x/this_ones_for_all_the_sql_developers_out_there/><img src=joins.jpg width=300px /></a>

    1. the formal definition of the different join operations is as syntactic sugar over the cross join
        1. inner join is syntactic sugar for a cross join + where clause

           the following are equivalent:
           ```
           SELECT * FROM a JOIN b ON (condition);
           ```
           ```
           SELECT * FROM a,b WHERE condition;
           ```
        1. the left outer join is syntactic sugar for an inner join + set operations

           the following are equivalent:
           ```
           SELECT * FROM a LEFT JOIN b ON (condition);
           ```
           ```
           SELECT * FROM a JOIN b ON (condition)
           UNION ALL
           (
           SELECT a.*,NULL,NULL,NULL,... FROM a         -- there should be one NULL for each column in b
           EXCEPT
           SELECT a.*,NULL,NULL,NULL,... FROM a JOIN b ON (condition)
           );
           ```
           when `condition` is an equality of the form `a.c1=b.c2`, then the following is also equivalent:
           ```
           SELECT * FROM a JOIN b ON (a.c1 = b.c2)
           UNION ALL
           SELECT * FROM a WHERE a.c1 NOT IN (SELECT b.c2 FROM b);
           ```
        1. the right/full outer joins are defined similarly to the left outer join
        1. for all joins, when `condition` has the form `a.c = b.c` (i.e. it is an equality on the same column name), then the `ON` clause can be replaced by a `USING` clause

           the following are equivalent:
           ```
           SELECT * FROM a JOIN b ON (a.c = b.c);
           ```
           ```
           SELECT * FROM a JOIN b USING (c);
           ```
        1. the natural join
            1. is confusingly named... it's not a separate type of join (like inner/left/right/full)
            1. it is a syntactic sugar over the `USING` clause

               it is equivalent to `USING` with all of the columns that share the same name between the two tables
            1. I personally avoid using these for the same reason I avoid using `SELECT *`:

               [Explicit is better than Implicit](https://www.python.org/dev/peps/pep-0020/) makes code easier to read and more robust to changes in the future

               (this is a principle in the zen of python)

    1. if this all seems weird/hard/confusing... that's because it is

       <img src=cmcqtycmbmg51.jpg width=300px />

1. arrays
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
