# Topic 06: Designing the database layout
<!--
FUTURE NOTE:
Implementing the word_ladder game in SQL would be a fantastic assignment!!!

SELECT DISTINCT
SELECT DISTINCT ON
Recursive queries
Cube/rollup
Window functions
-->

## Announcements

upcoming assignments

1. pagila-hw3 due next Tuesday

    1. most problems like problems from pagila 1-2, but no hints
    1. some problems you'll have to look up new techniques
    1. I will (probably) add 1-2 more problems to it tonight

1. twitter homework due next Tuesday

1. quiz next Wednesday

1. midterm posted next Wednesday after class, due Sunday

<!--

**Wed 16 Feb:**

1. pagila-hw graded; all but 2 students got 17/17; those 2 students need to resubmit to get credit, so everyone should check your grade

    1. [solutions posted](https://github.com/mikeizbicki/pagila-hw/tree/solution)

    1. [Google's VP in charge of hiring people says "GPA’s are worthless as a criteria for hiring, and test scores are worthless" because they don’t predict how productive an employee will be.](https://www.nytimes.com/2014/02/23/opinion/sunday/friedman-how-to-get-a-job-at-google.html)
-->


## Lecture

<img src=when-people-ask-me-to-explain-my-database-design-its-58698602.png width=400px />

Goals:
1. measure the disk usage of a database

   disk space usage can be large because:
    1. of overhead that doesn't store data
        1. multiple types: row, page
    1. redundant data stored multiple times

1. other misc. database design decisions

### Row Overhead

1. you are responsible for being able to calculate the number of bytes used by a row of data

   references:
    1. basic tutorial: <https://www.2ndquadrant.com/en/blog/on-rocks-and-sand/>
    1. detailed tutorial: <https://rjuju.github.io/postgresql/2016/09/16/minimizing-tuple-overhead.html>
    1. references contain sql queries that will solve all problems for you automatically

1. postgres has more overhead per row than other dbs
1. each row is divided into a header, data, and padding section
    1. header section:
        1. contains a 23 byte [`HeapTupleHeaderData`](https://www.postgresql.org/docs/current/storage-page-layout.html#HEAPTUPLEHEADERDATA-TABLE) struct + an optional "null bitmap"
        1. null bitmap:
            1. only present if the tuple contains at least one `NULL` value
            1. uses 1 bit per column (whether the column is nullable or not nullable), rounded up to the nearest byte (8-bits)

                1. by default, every column is "nullable"

                   a column is not nullable only if it is defined with the `NOT NULL` parameter

                   ```
                   CREATE TABLE example (
                       a INTEGER,               -- nullable
                       b INTEGER NULL,          -- nullable
                       c INTEGER NOT NULL       -- not nullable
                   );
                   ```
                1. why do nullable columns require an entry in the null bitmap?

                   so that we can add/remove `NULL`/`NOT NULL` constraints in O(1) time with a command like
                   ```
                   ALTER TABLE example ALTER COLUMN a SET NOT NULL;
                   ```

        1. the header must be padded to be a multiple of 8
            1. any table with <= 8 columns will have 24 bytes overhead (the null bitmap is 1 byte)
            1. any table with 8-264 columns will have 32 bytes overhead (the null bitmap is >1 byte)

    1. data section:
        1. every column with a non-null value requires a number of bytes depending on the column type
            <!--
            1. types can be either a fixed or variable number of bytes, for example:

               | type               | size      |
               | ------------------ | --------- |
               | `smallint`         | 2 bytes   |
               | `integer`          | 4 bytes   |
               | `bigint`           | 8 bytes   |
               | `float`            | 4 bytes   |
               | `double precision` | 8 bytes   |
               | `text`             | variable  |
            -->

        1. null values consume 0 bytes disk space
            1. postgres knows they're not present due to the null bitmap

        1. every type has an "alignment", which specifies hardware addresses the type is allowed to start on
            1. required due to hardware implementation details
            1. similar to byte alignment in C structs
            1. every hardware address is represented by a 64-bit (8-byte) integer
            1. for fixed-width types, the type is typically required to "align" onto a hardware address satisfying the following formula:
               ```
               size in byte % 8
               ```
               but not always
        1. to find information about a type, use the query
           ```
           select typname,typalign,typlen from pg_type;
           ```
           1. `pg_type` is a table built-in to all postgres databases that contains all the information about a type
           1. see `pg_type` table documentation: <https://www.postgresql.org/docs/13/catalog-pg-type.html>
           1. one of the nice things about postgres is that all properties of the database are stored in tables like `pg_type` and can be queried using normal sql

           > **NOTE:**
           > Some types have "aliases" that allow them to be called different names,
           > and these aliases are not defined in the `typname` table.
           > For example, the `SMALLINT` type is not listed in the table.
           > In order to find out the necessary information about a `SMALLINT`, you must find the name of the type that it aliases.
           > The easiest way to find these aliases is to google the type you are looking for restricted to the postgres webpage.
           > For example: [site:postgresql.org SMALLINT](https://www.google.com/search?hl=en&q=site%3Apostgresql.org%20SMALLINT)

    1. padding section:
        1. all rows are padded so that their total number of bytes is divisible by 8
        1. the function `pg_column_size` gives the size of the header+data portion only, without the padding

1. "column tetris" is ordering table columns optimally:
    1. do not order columns "logically"
    1. order columns fixed length (largest to smallest), then variable length
    1. gitlab policy: <https://docs.gitlab.com/ee/development/ordering_table_columns.html#real-example>
    1. postgres devs are aware of this "code smell"/"wart", and are working to fix it... but it's super complicated for lots of obnoxious technical reasons: <https://wiki.postgresql.org/index.php?title=Alter_column_position&oldid=23469>

1. TOAST used for variable sized columns
    1. TOAST = The Oversized Attribute Storage Technique

       "the best thing since sliced bread"

    1. advantages:
        1. allows storage of arbitrarily large variable length columns (most commonly text)
           
           1. one of the major advantages of postgres vs other rdbms, since they don't support arbitrarily large columns

           1. there's 2 string types defined by the SQL standard: `CHAR(n)`, `VARCHAR(n)` where `n` is the length of text

              postgres also supports `TEXT`, which is strictly better and should almost always be used: <https://www.depesz.com/2010/03/02/charx-vs-varcharx-vs-varchar-vs-text/>

        1. automatically/transparently compresses "large" (typically >2kb) data

    1. disadvantages:
        1. the format is rather more complicated

           we don't need the gory details, but they're in the docs: <https://www.postgresql.org/docs/current/storage-toast.html>
        1. the "null byte" `\x00` is not allowed in text (or basically any other variable-sized types)

           there's workarounds, but it's a pain: <https://www.commandprompt.com/blog/null-characters-workarounds-arent-good-enough/>

### Redundant data

1. database normalization:

   <img src=1swabl.jpg />

    1. denormalization: combining information into a single relation
    1. normalization: splitting information up into multiple different relations
        1. key feature that makes "relational" databases (RDBMSs) "relational"
        1. "nosql" databases are non-relational, and have little/no support for normalization
        1. always "more correct" from a "beauty" perspective
        1. sometimes faster, sometimes slower
        1. always stores less "realdata", but tables/rows have metadata too, and always results in more metadata;

           the total data stored is the realdata+metadata, which may go up or down

    1. [at least 11 different "normal forms" are in use](https://en.wikipedia.org/wiki/Database_normalization#Normal_forms)
        1. these 11 forms could be furthur divided into an arbitrary number of subcategories, and db researchers semi-regularly propose new forms
        1. database classes often spend a lot of time covering the different forms (we're not going to)
        1. the subtle differences can be important for db implementers
        1. db practitioners basically never talk about specific db forms, usually preferring to talk about "more" or "less" normalized in informal terms
    1. views
        1. "Making liberal use of views is a key aspect of good SQL database design."
           
           <https://www.postgresql.org/docs/13/tutorial-views.html>
        1. [create_view.sql](create_view.sql)
        1. a common use is to provide a denormalized interface to a normalized table
        1. by default, every view can support the `select` statement; special work is needed to support `insert`/`update` commands; for details, see: <https://arjanvandergaag.nl/blog/postgresql-updatable-views.html>

### Other considerations

1. tools for enforcing table correctness:
    1. `NULL` / `NOT NULL`
        1. reference: https://www.postgresqltutorial.com/postgresql-not-null-constraint/
    1. `UNIQUE` constraints
        1. enforces no duplicates in the column
        1. reference: https://www.postgresqltutorial.com/postgresql-unique-constraint/
    1. `CHECK` constraints
        1. enforces complicated conditions
        1. reference: https://www.postgresqltutorial.com/postgresql-check-constraint/
    1. `PRIMARY KEY` 
        1. equivalent to `UNIQUE NOT NULL`
        1. has semantic meaning of "the most important column(s) in the table", and what you should use as the "id"
        1. often used with `SERIAL` type or the `GENERATED BY DEFAULT AS IDENTITY` modifier
        1. reference: https://www.postgresqltutorial.com/postgresql-primary-key/
    1. `FOREIGN KEY`
        1. typically used to reference primary keys in another table that you want to join
        1. reference: https://www.postgresqltutorial.com/postgresql-foreign-key/
 
1. Entity-Relationship (ER) diagram
    1. example: the diagram from the pagila hw
    1. `*` represents primary key
    1. lines represent foreign keys
    1. the ending of the lines represents the type of relation
        1. <img src=ERD-Notation.PNG />
        1. reference: https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning
        1. WARNING: Many of the ERD symbols in the pagila diagram are wrong
        1. these endings are often wrong and I don't personally find them useful; good table/column names should make the relationship "obvious"
    1. Typical real world database: <https://anna.voelkl.at/wp-content/uploads/2016/12/ce2.1.3.png>

1. common table structures
    1. 1-1 relationships
        1. denormalized representation: different columns in the same table
            1. every film has exactly 1 title, and every title corresponds to exactly 1 film
            1. every customer has exactly 1 name, and every name corresponds to exactly one customer (`first_name || ' ' || last_name` is unique)
                1. aside: don't store people's names as `first_name` and `last_name`: https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/
            1. every payment has either 1 or 0 payment dates (nullable column)
        1. normalized representation: create a new table with a foreign key and unique constraint
            1. rental-payment tables

               ```
               CREATE TABLE rental (
                   rental_id SERIAL PRIMARY KEY,
                   ...
               );

               CREATE TABLE payment (
                   payment_id SERIAL PRIMARY KEY,
                   rental_id UNIQUE REFERENCES rental(rental_id), -- NOTICE: UNIQUE + FOREIGN KEY
                   amount numeric(5,2) NOT NULL,
                   payment_date timestamptz NOT NULL
               );

               ```

               notice that every payment must have a rental,
               but not every rental must have a payment
        1. when to use each:
            1. always prefer the denormalized representation when possible
            1. the normalized representation is slightly more powerful in that it can force us to have two columns inserted `null`/`not null` together

               if we implemented the rental/payment tables as:
               ```
               CREATE TABLE rental (
                   rental_id SERIAL PRIMARY KEY,
                   ...
                   amount numeric(5,2),         -- notice these collumns are NULLable
                   payment_date timestamptz
               );
               ```
               then everything that can be represented using the rental/payment tables could be represented using this modified table,
               but we might get some rows that have an `amount` without a `payment_date` or vice versa

               It's possible to create a `CHECK` constraint that enforces that `amount` and `payment_date` are linked:
               ```
               ALTER TABLE rental
               ADD CONSTRAINT rental_check
               CHECK ( (amount is null and payment_date is null) or (amount is not null and payment_date is not null));
               ```
               This is the best representation of this data for 99% of use cases since it uses significantly less disk space.
               The overhead of the `payment` table is:
               ```
               24 bytes standard overhead + 4 bytes for rental_id + 4 bytes for rental_id
               ```
               The denormalized representation + `CHECK` constraint has none of this overhead.
        1. IMNSHO, the pagila table is excessively normalized
            1. rental-payment should be combined
            1. film-language
                1. make `language` a `TEXT` column in `film`
            1. country-city-address-customer
                1. combine all of these into a single `address` field inside the `customer` table

    1. 1-many
        1. denormalized representation: arrays
            1. film-special_features

               ```
               CREATE TABLE film (
                   ...
                   special_features TEXT[],
                   ...
               );
               ```
        1. normalized representation: create a new table with a foreign key
            1. film-inventory
               
               ```
               CREATE TABLE film (
                   film_id SERIAL PRIMARY KEY,
                   ...
               );

               CREATE TABLE inventory (
                   inventory_id SERIAL PRIMARY KEY,
                   film_id INTEGER REFERENCES film(film_id), -- NOTICE: FOREIGN KEY ONLY, NO UNIQUE
                   store_id INTEGER,
                   last_update TIMESTAMPTZ
               );
               ```
            1. customer-rental
            1. store-staff
        1. disadvantages of the denormalized representation:
            1. arrays not a sql standard feature
                1. arrays not supported in MySQL/MSSQL, are supported in Oracle
                1. many people believe you should never use arrays for this reason
            1. can only have a single column as the many
                1. the film-special_features split could be normalized,
                1. no easy way to denormalize film-inventory, customer-rental, or store-staff
            1. confusing to work with
                1. you should always use the `unnest` function with arrays,
                   as this is guaranteed to give asymptotically optimal performance
                1. it is possible to index directly into an array like in standard python,
                   but this is sometimes an O(1) operation and sometimes an O(n) operation,
                   and it is very difficult to predict which situation you're in
                1. see: https://heap.io/blog/engineering/dont-iterate-over-a-postgres-array-with-a-loop
        1. advantages of the denormalized representation:
            1. disk usage of the denormalized representation is significantly less:
               ```
               24 bytes overhead + (len array) * (bytes for the type)
               ```
               and this data can be TOASTed (i.e. compressed) when large

               disk usage of the normalized representation is
               ```
               (number of rows)*(24 bytes overhead per row + bytes for type)
               ```
               this data cannot be TOASTed
        1. personally, I use arrays (denormalization) if the following conditions are met:
            1. only 1 column in the many (i.e. it's possible to use the denormalized form)
            1. joins on the array will be rare
            1. updates/deletes to entries in the array are rare
        1. method: enums
            1. film-rating (the rating column is restricted to be of the `mpaa_enum` type)
            1. supported in postgres, but strongly discouraged; see e.g. https://tapoueh.org/blog/2018/05/postgresql-data-types-enum/

    1. many-many
        1. think bipartite graph

           <img src=bipartite.png width=500px />
        1. no good denormalized representations
        1. normalized representation: create "connector tables" that represent the edges of the bipartite graph
            1. actor-film

               ```
               CREATE TABLE film (
                   film_ID SERIAL PRIMARY KEY,
                   ...
               );

               CREATE TABLE film_actor (
                   film_id INTEGER REFERENCES film(film_id),
                   actor_id INTEGER REFERENCES actor(actor_id),
                   PRIMARY KEY (film_id, actor_id),
               );

               CREATE TABLE actor (
                   actor_id SERIAL PRIMARY KEY,
                   ...
               );
               ```
            1. customer-film (the join of rental and inventory acts as the connector table)

            <!--1. anti-pattern: category-film are given a many-many table structure, but they actually have a 1-1 relationship-->

    1. general graph structures
        1. no good denormalized representations
        1. normalized representation: foreign key that references its own table
            1. no examples in the pagila database
            1. employee table
               ```
               CREATE TABLE employee (
                   employee_id SERIAL PRIMARY KEY,
                   manager INTEGER REFERENCES employee(employee_id)
               );
               ```
            1. no easy way to enforce acyclical references (i.e. make the graph a tree)
        1. all graph algorithms (DFS, BFS, Dijkstra, Prim, Kruskal, A*, etc.) can be implemented with optimal asymptotic efficiency using recursive sql queries
            1. we're not covering how to do this
            1. https://www.postgresqltutorial.com/postgresql-recursive-view/
            1. https://www.postgresqltutorial.com/postgresql-recursive-query/

1. references on good database design:
    1. Good overview <https://relinx.io/2020/09/14/old-good-database-design/>
    1. Database Modelization Anti-Patterns: <https://tapoueh.org/blog/2018/03/database-modelization-anti-patterns/>
    1. Building a scalable e-commerce data model: <https://news.ycombinator.com/item?id=25353148>

<!--
## Lab

For each table below,
reorder the table columns to use the minimal number of bytes.
Assuming all variable length fields are null (i.e. take up no space),
how much space do the reordered tables take up per row?
Submit your reordered tables and the space usage to sakai.

```
CREATE TABLE network_connection (
    id SERIAL,
    source macaddr NOT NULL,
    dest macaddr NOT NULL,
    starttime timestamptz NOT NULL,
    bytes_sent int8 NOT NULL
);
```

```
CREATE TABLE event (
    id BIGSERIAL,
    name TEXT,
    public BOOLEAN,
    max_guests SMALLINT,
    location_id INTEGER NOT NULL,
    starttime timestamp with time zone NOT NULL,
    endtime timestamp with time zone
);
```

```
CREATE TABLE example (
    id SMALLSERIAL NOT NULL,
    a SMALLINT,
    b CHAR,
    c int2,
    d line,
    e JSONB
);
```
-->
