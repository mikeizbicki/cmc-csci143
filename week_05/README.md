# Week 05: Designing the database layout
### (disk usage + normalization)

1. `CREATE TABLE` disk usage
    1. **for lab/midterm**: you are responsible for being able to calculate the number of bytes used by a row of data with only fixed sized columns
        1. basic tutorial: https://www.2ndquadrant.com/en/blog/on-rocks-and-sand/
            1. contains a sql query that will solve all problems for you automatically
        1. detailed tutorial: https://rjuju.github.io/postgresql/2016/09/16/minimizing-tuple-overhead.html
    1. postgres has more overhead per row than other dbs
        1. every tuple requires at least 23 bytes of overhead
        1. the overhead can be larger for tables with many nullable columns; you're not responsible for the details
        1. the overhead must be padded to be a multiple of 8, so the typical table has 24 bytes overhead, but some will have 32 bytes overhead (specifically, if there are >8 columns and some columns are nullable)
        1. in this class, you can assume that it's always 24 bytes overhead
    1. every column requires a number of bytes depending on the column type
        1. types can be either a fixed or variable number of bytes, for example:
            1. `integer` 4 bytes
            1. `biginteger` 8 bytes
            1. `float` 4 bytes
            1. `double precision` 8 bytes
            1. `text` variable
        1. null values always use 0 bytes
        1. every type has an "alignment", which specifies hardware addresses the type is allowed to start on
            1. required due to hardware implementation details
            1. similar to byte alignment in C structs
            1. every hardware address is represented by an integer
            1. for fixed-width types, the type is typically required to "align" onto a hardware address satisfying the following formula:
               ```
               size in byte % 8
               ```
               but not always
            1. "misalignment" results in padding bytes added
        1. to find information about a type, use the query
           ```
           select typname,typalign,typlen from pg_type;
           ```
           1. `pg_type` is a table built-in to all postgres databases that contains all the information about a type
           1. see pg_type table documentation: https://www.postgresql.org/docs/13/catalog-pg-type.html
           1. one of the nice things about postgres is that all properties of the database are stored in tables like `pg_type` and can be queried using normal sql
    1. TOAST used for variable sized columns
        1. the format is significantly more complicated
        1. TOAST = The Oversized Attribue Storate Technique
        1. "the best thing since sliced bread"
        1. allows storage of arbitrarily large variable length columns (most commonly text)
        1. automatically/transparently compresses "large" (typically >2kb) data
        1. one of the major advantages of postgres vs other rdbms, since they don't support arbitrarily large columns
        1. reference: https://www.postgresql.org/docs/13/storage-toast.html
    1. "column tetris" is ordering table columns optimally:
        1. do not order columns "logically"
        1. order columns fixed length (largest to smallest), then variable length
        1. gitlab policy: https://docs.gitlab.com/ee/development/ordering_table_columns.html#real-example
        1. postgres devs are aware of this "code smell"/"wart", and are working to fix it... but it's super complicated for lots of abnoxious technical reasons: https://wiki.postgresql.org/index.php?title=Alter_column_position&oldid=23469

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
        1. db practitioners basically never talk about specific db forms, usually preferring to talk about "more" or "less" normalized
    1. views
        1. "Making liberal use of views is a key aspect of good SQL database design."
           
           https://www.postgresql.org/docs/13/tutorial-views.html
        1. [create_view.sql](create_view.sql)
        1. a common use is to provide a denormalized interface to a normalized table
        1. by default, every view can support the `select` statement; special work is needed to support `insert`/`update` commands; for details, see: https://arjanvandergaag.nl/blog/postgresql-updatable-views.html

1. tools for enforcing table correctness:
    1. `NULL` / `NOT NULL`
        1. reference: https://www.postgresqltutorial.com/postgresql-not-null-constraint/
    1. `UNIQUE` constraints
        1. enforces no duplicates in the column
        1. reference: https://www.postgresqltutorial.com/postgresql-unique-constraint/
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
    1. Typical real world database: https://anna.voelkl.at/wp-content/uploads/2016/12/ce2.1.3.png

1. common table structures
    1. 1-1
        1. different columns in the same table
        1. example:
            1. every film has exactly 1 title (and every title corresponds to exactly 1 film)
            1. every customer has exactly 1 first name
            1. every payment has either 1 or 0 payment dates (nullable column)

    1. 1-many
        1. create a new table
        1. "list/array" column
        1. example:
            1. film-language (film's have just one language, but there are many films for each language)
            1. film-rating
            1. staff-store
            1. customer-address (modeling assumption; other reasonable assumptions could be 1-1 if each customer is a "household" or many-many if like amazon customers can have multiple addresses )

    1. 1-1 (insert only)
        1. the insert-only table pattern is used with the rental-payment tables
        1. duplication in the customer_id/staff_id columns
        1. follows the 1-many pattern, so there could be many payments for 1 rental, and no way to enforce that there is exactly 1 payment

    1. many-many
        1. example:
            1. actor-film
            1. customer-film (passes through both the rental and inventory table)
    1. hierarchical
        1. example:
            1. no examples in the pagila database
            1. employee table

1. references on good database design:
    1. Good overview https://relinx.io/2020/09/14/old-good-database-design/
    1. Database Modelization Anti-Patterns: https://tapoueh.org/blog/2018/03/database-modelization-anti-patterns/
    1. Building a scalable e-commerce data model: https://news.ycombinator.com/item?id=25353148

1. pagila anti-patterns
    1. don't store people's names as `first_name` and `last_name`: https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/
    1. category and film are given a many-many table structure, but they actually have a 1-1 relationship
    1. enum type for rating / `mpaa_rating`
    1. address/city/country and film/language are probably excessive normalization (especially since the language/country don't use ISO codes)

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
