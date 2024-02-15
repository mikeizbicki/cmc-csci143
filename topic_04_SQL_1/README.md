# Topic 04: Basic SQL

## Announcements

1. Due tonight @ midnight:
    1. twitter coronavirus  (25/46 submitted)
    1. flask-on-docker      (13/46 submitted)

    Additional office hours today from 12pm-1pm.

1. Recall:
    1. ```
       late penalty = 2**(# days late - 1)
       ```
    1. Very little partial credit awarded.
        Usually better to submit correct work late than incorrect work on time.

1. No quiz this week :)

1. Outline of the rest of the class:
    1. 4 weeks: how to make SQL correct
        - most important section of the course
            - covers the SQL material commonly found in data science technical interviews
        - material much more straightforward
            - no integration of many concepts which have only loosely been covered in class
            - no fighting weird error messages
            - the purpose of covering docker was so that we could introduce PostgreSQL
        - midterm (SQL only, no docker)
            - takehome exam (maybe Mar 7-11, maybe Mar 14-25)
            - designed to take < 1 hour
            - scores usually very good
    1. 6 weeks: how to make SQL fast

## Lecture

Relational DataBase Management Systems (RDBMSs):

1. It doesn't matter what the problem is, a database is the solution

   <img src=dilbert2.jpeg width=80% />

1. Structured Query Language (SQL) is the language for accessing the database
    1. Most "real programmers" pronounce it like "sequel" not "es-cue-el"

        <img src=dilbert.gif width=80% />
    
        Why?
        1. Programmers are lazy; "sequel" is 2 syllables and "es-cue-el" is 3
        1. SQL was originally SEQUEL (Structured English Query Language), but shortened due to trademark reasons
            1. You can find the official ANSI SQL standards and history at <https://blog.ansi.org/2018/10/sql-standard-iso-iec-9075-2016-ansi-x3-135/>
            1. Invented in the 70s (just like the POSIX-shell), and so has lots of weird warts for backwards-compatibility reasons
    1. Comparison to other languages:
        1. Imperative languages (e.g. Python/Shell) specify **how** to compute 
        1. Declarative languages (e.g. SQL) specify **what** to compute.
           A compiler will convert the declarative code into imperative code.
           The resulting code has provably guaranteed excellent performance (both asymptotically and constant factors).
    1. Object Relational Mappers (ORMs):
        1. Libraries that "hide" the SQL interface to the database
        1. Make it so that you don't have to learn SQL, and can rely on your "normal" imperative programming knowledge
        1. They're easy to get started with, but much harder once you need to scale
            1. reddit uses the SQLAlchemy ORM

                (the flask-on-docker homework also used SQLAlchemy)
            1. twitter started with Ruby on Rails, but left due to bad performance
        1. [What ORMs have taught me: Just learn SQL](https://news.ycombinator.com/item?id=24845300)

1. There are two other categories of databases:
    1. NoSQL databases (MongoDB, CassandraDB, etc.)
        1. No standard language for accessing them
        1. No guarantees that the data will actually be in the database
    1. Graph databases
        1. Use SparQL instead of SQL

1. Comparison of main RDBMSs:
    1. <http://howfuckedismydatabase.com/>
    1. [database popularity from stackoverflow](https://survey.stackoverflow.co/2022/#section-most-popular-technologies-databases)
    1. my summary:
        1. if you can't install docker (e.g. writing a cell phone app), use sqlite3 
        1. otherwise, use postgresql
    1. [Even Microsoft uses Postgres instead of SQLServer for large scale database needs](https://techcommunity.microsoft.com/t5/azure-database-for-postgresql/architecting-petabyte-scale-analytics-by-scaling-out-postgres-on/ba-p/969685)

<!--
Important stories:

1. Junior dev given API keys and deletes the database: https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/
-->

What you must know for the homework/midterm

1. midterm questions will be the sorts of SQL questions found in data science technical interviews

1. `SELECT`
    1. sections 1,2,4 of <https://www.postgresqltutorial.com/>
    1. aggregate functions `count`, `max`, `min`, `sum`, `avg`
    1. never use the `BETWEEN` keyword: <https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_BETWEEN_.28especially_with_timestamps.29>

1. `JOIN`
    1. section 3 of <https://www.postgresqltutorial.com/>
    1. for this quiz/homework, you will only need inner joins; next homework will need all types of joins
    1. the "standard" explanation of joins uses venn diagrams, but this is technically not correct since relations are not sets; see: https://blog.jooq.org/2016/07/05/say-no-to-venn-diagrams-when-explaining-joins/
    1. joins memes

       <!--
       <a href=https://www.reddit.com/r/ProgrammerHumor/comments/a0qp9x/this_ones_for_all_the_sql_developers_out_there/><img src=joins.jpg /></a>
       -->

       <img src=cmcqtycmbmg51.jpg width=600px />

1. weird syntax
    1. whitespace doesn't matter, every command must end in a semicolon
    1. case insensitive
    1. `'` is for quoting literals, `"` is for quoting table/column names
    1. escape quotes by doubling them, not a backslash `'isn''t'` not `'isn\'t'`
    1. dollar sign quotes
        1. `$$this is a quote$$` is equivalent to `'this is a quote'`
        1. useful to avoid having to escape quotes in complex strings: you can write `$$isn't$$` instead of `'isn''t'`
        1. you can "name" the quotation marker: `$blah$isn't$blah$` instead of `$$isn't$$`
    1. concatenate strings with `||` not `+`


References:
1. cheatsheets
    1. https://postgresql-backup.com/postgresql-blog/wp-content/uploads/2016/06/PostgreSQL-Cheat-Sheet_-String-Functions.pdf
    1. https://www.postgresqltutorial.com/wp-content/uploads/2018/03/PostgreSQL-Cheat-Sheet.pdf

1. psql command reference: https://www.postgresqltutorial.com/psql-commands/

## Lab

TBA

## Homework

The homework is posted in the [pagila-hw](https://github.com/mikeizbicki/pagila-hw) github submodule.
