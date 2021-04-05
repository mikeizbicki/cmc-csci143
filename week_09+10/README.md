# Week 09+10: B-Trees and Indexes

**No Homework for Week 09.**

Indexes are data structures used for making SQL queries (typically `SELECT`) fast.
1. Advantage:
    1. reduce the runtime of finding a row (for `SELECT`/`UPDATE`/`DELETE` statements) from O(n) down to O(log n)
    1. required for the implementation of `UNIQUE` constraints
1. Disadvantage:
    1. increase the runtime of `INSERT` from O(1) to O(log n)
1. Careful use of indexes will solve 90% of all big data runtime problems

<img src=Strip-magicien-du-code-650-finalenglish.jpg />

<br/><br/>

<img src=Strips-Fier-600-finalenglish.gif />

Types of Indexes in Postgres:
1. BTree
1. Hash
1. Gin
1. RUM
1. BRIN
1. GIST
1. SP-GIST
1. (others can be programmed in using extensions)

<!--
Vocabulary:
1. "access method" = "index"
1. "indexed-field operator expression" is an expression in a `WHERE` clause where the expression to the left of the operator has been indexed
-->

## BTree details

1. A "high fan-out" balanced search tree
    1. optimized for on-disk data storage
        1. HDD internals:

           <img src=hdd.png />

           <img src=tm112_1_ol_s5_f1_5.tif.png />

        1. common runtimes: http://norvig.com/21-days.html#answers

    1. used for:
        1. conditions involving equality and less/greater than
        1. sorting
        1. use with the `like` operator
           https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/like-performance-tuning
        1. basically everything except full text search
1. postgres-specific reference: 
    1. the official docs are very terse: https://www.postgresql.org/docs/13/btree.html
    1. good overview: https://habr.com/ru/company/postgrespro/blog/443284/
    1. `README` in the source for real details: https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=src/backend/access/nbtree;h=2e3fb91ac5930dbcc0c6fc9b8b0659d9aa71bbd2;hb=HEAD

## Algorithms for using Indexes

Table Scanning Strategies

1. Used to calculate the answer to a SQL query of the form:
   ```
   SELECT column_list
   FROM table
   WHERE condition
   ```

   Reference: https://habr.com/ru/company/postgrespro/blog/441962/

1. Basic idea:

    1. You write a `SELECT` statement which describes "what" you want
    1. The *query planner* automatically determines "how" to calculate it 
        1. It will re-write your SQL queries into more efficient expressions
        1. It will choose the best algorithms for your particular combination of hardware, data, indexes, and query expressions
        1. There are various theorems that prove that no system can perform these steps optimally in all circumstances,
           but it still is pretty good
        1. To fully understand the query planner, you should take a course on compilers
        1. Reference: http://www.interdb.jp/pg/pgsql03.html

1. Definitions:

    1. `n` = number of tuples in the table
    1. `b` = branching factor of the B-Tree
    1. `k` = number of rows returned by the `SELECT`
    1. All runtimes assume 
        1. Whenever we use an equality (`a = 5000`)
           or a range query (`a <= 5000 AND a >= 4000`),
           then the runtime is 
        1. "worst case" bounds for the cartoon model of what postgres is doing

1. Sequential Scan

    1. Requirements:
        1. Can always be used
    1. Runtime:
        1. table pages accessed = `O(n)`
        1. index pages accessed = 0
        1. comparison operations = `O(n)`
        1. small constant factor
    1. Used when (OR):
        1. no index is defined
        1. `n` is small
        1. the `SELECT` statement will return a "significant" fraction of the data

1. Index Only Scan
    1. Requirements:
        1. The index is a "covering index"
        1. That is, all of the columns returned by the `SELECT` query and all columns in the `WHERE` clause are present in the index
    1. Runtime:
        1. table pages accessed = 0
            1. this assumes that there are no "invisble" tuples in the table, which is checked using the visibility map
            1. this value can be non-zero if we must examine the `xmin`/`xmax` system columns to determine if the tuple is visible
            1. regular vacuuming helps keep the visibility map "clean" and ensures this scan is fast
        1. index pages accessed = `O(log_b n + k/b)`
        1. comparison operations = `O(b*log_b n + k)`
        1. small constant factor
    1. Used when:
        1. Essentially whenever possible... this is the best case scenario for indexes

1. Index Scan

    1. The access method returns TID values one by one until the last matching row is reached
    1. Requirements:
        1.  At least one column of the `WHERE` clause is present in the index... and it should be a highly selective one
    1. Runtime:
        1. table pages accessed = `O(k)`
            1. Note that the number of pages is O(n/b), and k is only guaranteed to be <= n, so this can potentially access more pages than exist in the table!
            1. No guarantee that the same page will not be accessed multiple times
            1. Caching of pages in memory somewhat mitigates this problem
        1. index pages accessed = `O(log_b n + k/b)`
        1. comparison operations = `O(b*log_b n + k)`
        1. medium constant factor
    1. Used when (AND):
        1. `k << n/b`
        1. only one index will be consulted

1. Bitmap Scan
    1. More complicated scan method that uses indexes

    1. Runtime
        1. table pages accessed = `O(k)`
            1. typically much less than for an index scan
            1. guaranteed to never access the same page twice; equivalent to guaranteeing that we access the minimum number of pages necessary
        1. index pages accessed = `O(log_b n + k/b)`
        1. comparison operations = `O(b*log_b n + k)`
        1. high constant factor
    1. Used when (OR):
        1. multiple indexes will be consulted (the bitmaps of each index get AND/ORed together)
        1. `k` is relatively large, so the chance of multiple tuples from the same page is high
    1. Downside:
        1. Cannot return results 1 at a time (like all other scans),
           must return them as a large batch

Aggregate Strategies
1. HashAggregate
1. GroupAggregate
1. Reference:
    1. https://www.slideshare.net/AlexeyBashtanov/pgday-uk-2016-performace-for-queries-with-grouping
    1. https://www.cybertec-postgresql.com/en/postgresql-speeding-up-group-by-and-joins/

Join Strategies

1. Algorithms for computing the join in a SQL query
1. Three types of join strategies:
    1. Nested loop join
    1. Hash join
    1. Merge join
1. Reference: https://www.cybertec-postgresql.com/en/join-strategies-and-performance-in-postgresql/

Parallelism
1. Most query plans in postgres can be parallelized
    1. For those that cannot, lots of engineering work is going into enabling parallelism
1. Parallelism incurs a (small) constant overhead to setup,
   and so very small queries will not be parallelized
1. References
    1. https://www.postgresql.org/docs/13/parallel-plans.html
    1. https://www.postgresql.org/docs/13/how-parallel-query-works.html 
    1. Extensive details: https://wiki.postgresql.org/wiki/Parallel_Internal_Sort

`EXPLAIN`

1. Shows which algorithms postgres will use for any query
1. Used to debug all performance problems in postgres

   <img src=explain_analyze.jpg />

## Other Indexes

Hash index
1. reference: https://habr.com/ru/company/postgrespro/blog/442776/
1. limitations:
    1. only support equality search
    1. cannot decrease in size
    1. no support for index only scans
    1. cannot support multicolumn indexes
1. runtime (index scan and bitmap index scan):
    1. table pages accessed = `O(k)`, same as b-tree
    1. index pages accessed = `O(k/b)`, negligibly (why?) less than b-tree
    1. comparison operations = `O(k)` less than b-tree
    1. must consider the runtime of hashing,
       which can be large for large datatypes

GIN index
1. reference: https://habr.com/ru/company/postgrespro/blog/448746/
1. internally uses b-trees to arrange lexemes and for posting lists
1. used for:
    1. full text search
    1. indexing arrays
    1. indexing `JSONB`
1. limitations:
    1. elements never deleted
    1. slow to modify
    1. does not store auxiliary information (fixed in rum index)
        1. position of lexemes in the document
        1. timestamp/pagerank of the document
    1. does not support index scan / index only scan;
       only supports bitmap scans;

       this implies that the `LIMIT` operation is not efficient

       `gin_fuzzy_search_limit` is an alternative

RUM Index
1. Reference: https://habr.com/ru/company/postgrespro/blog/452116/
1. Like the GIN index, but also let's you store "metainformation" (e.g. pagerank, timestamp) in the index, and return results sorted by the metainfo

<!--
## Other Topics

Key ideas:
1. indexing null
1. multicolumn indexes
1. expression indexes
1. partial indexes
1. sorting the index
1. `UNIQUE`, `INCLUDE`
1. index with `WHERE col LIKE 'A%'` clause

1. set enable_indexscan=off;
1. concurrent building / share locks

1. `FOREIGN KEY` creates an index on the target, but not the source; problematic for joins and deletes on the target https://www.cybertec-postgresql.com/en/index-your-foreign-key/
1. load first, create indexes later, `fill_factor`

Key parameters:
1. `maintenance_work_mem` is the amount of memory used for creating index from scratch
   (a sort must be done, and more memory = faster sort)
1. `work_mem` is the amount of memory used for each query
1. `shared_buffers` is the total number of pages that will be cached in memory
    1. general caching detail: https://severalnines.com/database-blog/overview-caching-postgresql
    1. redfin engineering: https://redfin.engineering/how-to-boost-postgresql-cache-performance-8db383dc2d8f
    1. most details: https://madusudanan.com/blog/understanding-postgres-caching-in-depth/
1. postgres docs for all parameters: https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-SHARED-BUFFERS


-->
