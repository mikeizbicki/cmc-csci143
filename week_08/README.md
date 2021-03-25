# Combining Postgres+Python / starting indexes

---

Common midterm mistakes:

1. (-1) hard coding id values, e.g.

    ```
    WHERE country_id != 103
    ```
    instead of
    ```
    WHERE country != 'United States';
    ```

1. (-1) including too many columns in the results
    
    ```
    SELECT
        country,
        count(customer_id)
    ```
    instead of just 
    ```
    SELECT country
    ```

1. (-1) extraneous subqueries, e.g.

   ```
   SELECT
        count(*)
    FROM (
        SELECT
            customer_id
        FROM customer
        INNER JOIN address USING (address_id)
        INNER JOIN city USING (city_id)
        INNER JOIN country USING (country_id)
        WHERE country != 'United States'
        ORDER BY customer_id
    ) AS p
    ;
   ```
   could be replaced by
   ```
   SELECT
       count(*)
   FROM customer
   INNER JOIN address USING (address_id)
   INNER JOIN city USING (city_id)
   INNER JOIN country USING (country_id)
   WHERE country != 'United States'
   ORDER BY customer_id
   ;
   ```


   and

   ```
   SELECT
       actor_id
   FROM film_actor
   WHERE film_id = (SELECT film_id FROM film WHERE title='AMERICAN CIRCUS')
   ```
   is better as an inner join
   ```
   SELECT
       actor_id
   FROM film_actor
   JOIN film USING (film_id)
   WHERE title='AMERICAN CIRCUS'
   ```

1. (-2) misordering smallint/varchar(2) on problem 5

1. SIDE NOTE: writing joins like this is REALLY hard to read
   ```
   INNER JOIN address
   USING (address_id)
   INNER JOIN city
   USING (city_id)
   INNER JOIN country
   USING (country_id)
   ```
   also it's really weird to write
   ```
   INNER JOIN film f1 USING (film_id)
   JOIN film_actor fa2 ON (fa2.actor_id = fa1.actor_id)
   ```

---

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

   <img src=Strip-Bas-ed-eonnée-effacée-650-finalenglish.jpg />

1. Working with denormalized data

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

       Reference: http://adpgtech.blogspot.com/2014/09/importing-json-data.html

       **WARNING**:
       The `sed 's/\\u0000//g'` command above removes the `\0` character from strings before passing them to postgres.
       This means we are not storing exactly the same information that is being stored in the input file.
       This is required because postgres cannot store the `\0` character directly.
       This is a rarely used character (it is reserved to mean "end of string" in C-like languages),
       but this is an annoying thing about postgres.
       The problem is known, but fixing the problem is too hard and will probably never happen (similar to fixing column tetris).

    1. store data in `JSONB` columns

        1. JSONB stands for JSON + Binary formatted;
           there is also a JSON column type, but it is strictly inferior

        1. access data using the operators
            1. `->'key'` returns the value of `'key'` as a `JSONB` type
            1. `->>'key'` returns the value of `'key'`, but resolves the type 
            1. typical to chain them like `data->'key1'->'key2'->>'key3'`
            1. the `COALESCE` function is useful for providing default values

        1. every row can have a different schema, just like every JSON object can have different keys;
            1. postgres can't do as many optimizations, so selects a bit slower and rows take up more disk space
            1. the application needs to ensure that the data is correct, postgres won't do it for you
            1. for certain applications, it's much more conenient

    1. NoSQL:
        1. Last week we mentioned that one "advantage" of NoSQL databases over postgres is that they are faster because they do not offer ACID guarantees. (I put advantage in scare quotes because it's possible to turn off Postgres's ACID guarantees to improve performance.)
        1. The other killer feature of NoSQL databases is the ability to store raw JSON documents... but Postgres can do that too!  (And Postgres let's you combine these documents using arbitrary SQL, which NoSQL dbs cannot do.)

    1. When to store data in postgres in a denormalized form?

        1. If it's given to you in a denormalized form (often from an API), then I'd keep it denormalized.
        1. If you generate the data yourself, then I'd store it normalized.

1. Connecting to Postgres from Python

    1. SQLAlchemy library provides a generic interface for connecting to many RDBMs.
       SQLAlchemy contains both a basic interfact for using raw SQL (which we'll use),
       and an ORM for "hiding" the SQL behind python classes.
       The SQLAlchemy ORM is fairly popular (the reddit source code uses it, and you used it in your flask app from week2),
       but we won't use it.

       Reference: https://docs.sqlalchemy.org/en/13/core/connections.html

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
       
          https://find-and-update.company-information.service.gov.uk/company/10542519

       1. Company named `"><SCRIPT SRC=HTTPS://MJT.XSS.HT> LTD` forced to change its name by the Companies House
       
          https://www.reddit.com/r/programming/comments/jpdo21/company_named_script_srchttpsmjtxssht_ltd_forced/

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
