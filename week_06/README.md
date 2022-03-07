# Modifying the Database (SQL+Python)

## Announcments

**Monday, 07 March**

1. Good to see you all again :)

1. All assignments are graded.

   1. Twitter/MapReduce

      4 students missed points (between -10 to -2)

      The explanations are a bit complex, so see me to go over why (and possibly get points back)

   1. Pagila-hwX

      1. Lots of great scores!

   1. Overall grades

      Median: 97%

      Total points: between 103-133

1. Midterm

   Format:

   - take-home; open note/computer/any other resource you'd like

   - I will distribute it Wednesday afternoon; you have until Friday@midnight

   - Wednesday in-class is a review session for you to ask questions (no class Friday)

   Content:

   - 5 questions, 15 points/question => 75 points

   - 4 questions of SQL problems based on pagila (focus on pagila-hw2/hw3 concepts)

       - you will NOT have access to the desired output

       - I will read your SQL manually to grade (and not do a verbatim check on the output like in the hw)

           - No penalty for incorrect answers

           - I will award partial credit

             (I'm told I'm less generous than other profs)

           - If you misunderstand what the English is asking for, expect no credit on the problem

           - 3 points/problem for the "readability" of your SQL code

   - 1 question of column tetris; you must do both:

       - find the total number of bytes/row

       - rearrange the rows for optimal storage

## Lecture

1. Working with denormalized JSON data in postgres

    1. store data in `JSONB` columns

        1. `JSONB` stands for JSON + Binary formatted;
        1. There is also a `JSON` column type, but it is strictly inferior and included only for historical reasons
        1. For the full history of Postgres JSON support, see <https://www.youtube.com/watch?v=tF3Lb2BvGpk>

           (You may watch this video for your culture caveat task.)

           Summary:
           1. JSON support is the "killer feature" of MongoDB and many other NoSQL systems
           1. For this reason, NoSQL became super popular around the 2010-2014 time frame
           1. In 2014+ Postgres has strictly better JSON support
           1. Postgres team led the standardization effort for getting JSON in ANSI SQL standard
           1. No other RDBMS has good JSON support (MSSQL/MySQL/Sqlite have no support; Oracle has limited support)

    1.  > **NOTE:**
        > `JSON` (in backticks) refers to a specific type implemented in the postgres system;
        > JSON (no backticks) refers to the more abstract platonic JSON ideal without respect to any particular implementation.
        > This subtle grammar point is an important shibboleth for programmer competence.

    1. access data using the operators
        1. `->'key'` returns the value of `'key'` as a `JSONB` type
        1. `->>'key'` returns the value of `'key'`, but resolves the type 
        1. typical to chain them like `data->'key1'->'key2'->>'key3'`

           notice that the right most arrow is a `->>` and all other arrows are `->`
        1. `jsonb_array_elements` is like the `unnest` function, but for json arrays
        1. the `COALESCE` function is useful for providing default values
        1. if you're confused about the type of a variable, use `pg_typeof`

    1. every row can have a different schema, just like every JSON object can have different keys;
        1. postgres can't do as many optimizations, so selects a bit slower and rows take up more disk space
        1. the application needs to ensure that the data is correct, postgres won't do it for you
            1. _**this should TERRIFY you**_
            1. the database is the "ground truth" of you business logic... if it contains wrong data, there's nothing you can do
        1. for certain applications, it's much more convenient

    1. Insert data using the SQL `INSERT` command or `COPY` command.

       `COPY` is much faster and supports directly importing CSV and JSON data (and a few other formats I've never used before).
       The downside is that it only works for denormalized data;
       if you need to normalize the data somehow,
       then you'll have to write some python.

       The `COPY` syntax for copying from a json file into a table is
       ```
       cat <JSONFILE> | sed 's/\\u0000//g' | psql <POSTGRES_DB_URL> -c "COPY <TABLENAME> (<COLUMNNAME>) FROM STDIN csv quote e'\x01' delimiter e'\x02';"
       ```
       where everything in `<...>` needs to be replaced with approriate values.

       Reference: <http://adpgtech.blogspot.com/2014/09/importing-json-data.html>

       > **WARNING**:
       > The `sed 's/\\u0000//g'` command above removes the `\0` character from strings before passing them to postgres.
       > This means we are not storing exactly the same information that is being stored in the input file.
       > This is required because postgres cannot store the `\0` character directly.
       > This is a rarely used character (it is reserved to mean "end of string" in C-like languages),
       > but this is an annoying thing about postgres.
       > The problem is known, but fixing the problem is too hard and will probably never happen (similar to fixing column tetris).

    <!--
    1. NoSQL:
        1. Last week we mentioned that one "advantage" of NoSQL databases over postgres is that they are faster because they do not offer ACID guarantees. (I put advantage in scare quotes because it's possible to turn off Postgres's ACID guarantees to improve performance.)
        1. The other killer feature of NoSQL databases is the ability to store raw JSON documents... but Postgres can do that too!  (And Postgres let's you combine these documents using arbitrary SQL, which NoSQL dbs cannot do.)
    -->

1. When to store data in postgres in a denormalized form?

    1. If it's given to you in a denormalized form (often from an API), then I'd keep it denormalized.
    1. If you generate the data yourself, then I'd store it normalized.

1. Connecting to Postgres from Python

    1. SQLAlchemy library provides a generic interface for connecting to many RDBMs.
       SQLAlchemy contains both a basic interfact for using raw SQL (which we'll use),
       and an ORM for "hiding" the SQL behind python classes.
       The SQLAlchemy ORM is fairly popular (the reddit source code uses it, and you used it in your flask app from week2),
       but we won't use it.

       Reference: <https://docs.sqlalchemy.org/en/13/core/connections.html>

    1. Engine: create once per program
       ```
       engine = sqlalchemy.create_engine(URL)
       ```
       URL format is
       ```
       postgresql://username:password@host:port/database
       ```
       but the "scheme" part of the format could be any other database name (e.g. `mysql`, `sqlite3`, `oracle`, etc.).


    1. Connection: create many connections per engine; web apps create one connection per connected client, otherwise most other apps create just a single connection
       ```
       connection = engine.connect()
       ```

    1. Transactions
       ```
       with connection.begin() as trans:
           # inside of a transaction here
       ```

    1. Queries
       ```
       sql = sqlalchemy.sql.text('''
           SELECT id_tweets
           FROM tweets
           WHERE id_tweets = :id_tweets
           ''')
       res = connection.execute(sql,{
           'id_tweets':tweet['id'],
           })
       ```
       the result `res` is an iterator over all of the results returned by the query.
       ```
       row = res.first()  # this is prefered
       ```
       gets you the first row of the results
       ```
       rows = list(row)
       ```
       gets a list of all the rows
       ```
       for row in res:
           # process row 
       ```
       is a very common pattern for looping over the rows
       ```
       row[i]
       ```
       gets you the `i`th column from `row`

    1. Properly escape your inputs!!!

       Users naturally create weird inputs.
       This woman has problems with icloud because her last name is "True".

       https://twitter.com/RachelTrue/status/1365461618977476610

       <img src=su7tsddd0fl61.jpg width=400px />

       SQL injection is when those weird inputs perform malicious behavior.

       <img src=exploits_of_a_mom.png />

       Examples:

       1. UK company named `; DROP TABLE "COMPANIES";-- LTD`
       
          <https://find-and-update.company-information.service.gov.uk/company/10542519>

       1. Company named `"><SCRIPT SRC=HTTPS://MJT.XSS.HT> LTD` forced to change its name by the Companies House
       
          <https://www.reddit.com/r/programming/comments/jpdo21/company_named_script_srchttpsmjtxssht_ltd_forced/>

1. Special insert syntax

   1. `ON CONFLICT DO NOTHING` says that if you are inserting into a table with a `UNIQUE` constraint,
      and you violate the constraint, then don't throw an error;
      without this line, an error will be thrown in python

   1. `RETURNING column_list` makes the `INSERT` statement behave like a `SELECT` that returns columns from the inserted rows

   1. both used in the `get_id_urls` function:

       ```
       insert into urls
            (url)
            values
            (:url)
       on conflict do nothing
       returning id_urls
       ```

1. It is most efficient to insert in large batches (>100 rows per `INSERT` statement).
   The code in `load_tweets.py` is not very efficient since it does not do this.

1. Practical tip:
   Whenever you delete/update information, perform 2 steps:
   
   1. Do a select statement first to ensure that your where clause is correct.
      If you plan on running 
      ```
      DELETE FROM xxx WHERE yyy;
      ```
      First run
      ```
      SELECT * FROM xxx WHERE yyy; 
      ```
      to ensure you are deleting the right information.

   1. Do it in an explicit transaction.
      This ensures that if you make a mistake,
      it is easy to undo the mistake. 

   Postgres will happily delete everything in the database if you have a typo in your delete/update statements,
   and these tips will ensure that you don't accidentally have this happen to you.

   <img src=Strip-Bas-ed-eonnée-effacée-650-finalenglish.jpg width=400px />

   Stories:
   1. Junior dev given API keys and deletes the database: <https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/>
