# Week 03: Basic SQL

Relational DataBase Management Systems (RDBMSs):

    1. It doesn't matter what the problem is, a database is the solution

       <img src=dilbert2.jpg width=80% />

    1. Structured Query Language (SQL) is the language for accessing the database
        1. don't pronounce it es-cue-el; that's a shiboleth for not knowing much about databases

           <img src=dilbert.gif width=80% />

        1. SQL was originally SEQUAL, but shortened due to trademark reasons
        1. You can find the official ANSI SQL standards and history at https://blog.ansi.org/2018/10/sql-standard-iso-iec-9075-2016-ansi-x3-135/

    1. Comparison of main database systems:
        1. http://howfuckedismydatabase.com/
        1. [SQLite vs MySQL vs PostgreSQL](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)
        1. my summary:
            1. if you can't install docker (e.g. writing a cell phone app), use sqlite3 
            1. otherwise, use postgresql

    <!--
    1. There are two other categories of databases:
        1. NoSQL databases (MongoDB, CassandraDB, etc.)
        1. Graph databases; use SparQL instead of SQL
    -->

    1. Outline of the rest of the class:
        1. 4 weeks: how to make SQL correct
        1. 7 weeks: how to make SQL fast

Important stories:

    1. Junior dev given API keys and deletes the database: https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/
    1. Even Microsoft uses Postgres instead of SQLServer for large scale database needs: https://www.citusdata.com/blog/2019/12/07/petabyte-scale-analytics-postgres-on-azure-with-citus/

SQL

    1. What you must know for the homework/midterm
        1. `CREATE TABLE`
            1. https://www.postgresqltutorial.com/postgresql-create-table/
            1. https://www.postgresqltutorial.com/postgresql-data-types/
        1. `INSERT` / `UPDATE` / `DELETE`
            1. sections 9 of https://www.postgresqltutorial.com/
        1. `SELECT`
            1. sections 1-4 of https://www.postgresqltutorial.com/
            1. <a href=https://www.reddit.com/r/ProgrammerHumor/comments/a0qp9x/this_ones_for_all_the_sql_developers_out_there/><img src=joins.jpg /></a>

    1. weird syntax
        1. whitespace doesn't matter, every command must end in a semicolon
        1. case insensitive
        1. `'` is for quoting literals, `"` is for quoting table/column names
        1. escape quotes by doubling them, not a backslash `'isn''t'` not `'isn\'t'`
        1. dollarsign quotes
            1. `$$this is a quote$$` is equivalent to `'this is a quote'`
            1. useful to avoid having to escape quotes in complex strings: you can write `$$isn't$$` instead of `'isn''t'`
            1. you can "name" the quotation marker: `$blah$isn't$blah$` instead of `$$isn't$$`
        1. concatenate strings with `||` not `+`

    1. Useful psql commands:
        1. https://www.postgresqltutorial.com/psql-commands/
