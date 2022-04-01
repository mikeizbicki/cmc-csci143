# Week 11: B-Trees and Indexes

Indexes are data structures used for making SQL queries (typically `SELECT`) fast.

1. Advantage:
    1. reduce the runtime of finding a row (for `SELECT`/`UPDATE`/`DELETE` statements) from O(n) down to O(log n)
    1. required for the implementation of `UNIQUE` constraints (and thus `FOREIGN KEY` constraints)

1. Disadvantage:
    1. increase the runtime of `INSERT` from O(1) to O(log n)

1. Other highlights:
    1. Careful use of indexes will solve 99% of your SQL performance problems
    1. Most industry devs never properly learn SQL -> don't understand indexes -> can't make their code fast

<img src=Strip-magicien-du-code-650-finalenglish.jpg />

<br/><br/>

<img src=Strips-Fier-600-finalenglish.gif />

Main reference:
1. You are responsible for everything in the blog posts at <https://habr.com/en/company/postgrespro/blog/441962/>
1. Chapter 7 of Internals of Postgres <http://www.interdb.jp/pg/pgsql07.html>

Built-in Indexes (data structures) in postgres:
1. BTree **(most important)**
1. Hash
1. Gin
1. BRIN
1. GIST
1. SP-GIST

Common user-added indexes:
1. RUM <https://github.com/postgrespro/rum>
1. ivfflat <https://github.com/pgvector/pgvector>

<!--
Vocabulary:
1. "access method" = "index"
1. "indexed-field operator expression" is an expression in a `WHERE` clause where the expression to the left of the operator has been indexed
-->

## BTree details

1. You should have a basic intuitive understanding, but you won't need to understand low-level details

    1. BTree is an extension of the balanced binary search tree (AVL-Tree / Red-Black Tree / 2-3 Tree)

    1. optimized for "on-disk" storage instead of "in-memory storage"

        1. **key idea:** fast to find information stored close together, slow to "seek" to new information

            1. increase the number of CPU operations in order to decrease the number of disk/IO (input-output) operations

        1. HDD internals:

           <img src=hdd.png />

           <img src=tm112_1_ol_s5_f1_5.tif.png />

           1. HDD must load a "sector" of information at a time, cannot load individual bytes

        1. A "high fan-out" reduces the number of disk seeks

           in practice, fanout typically 100s in postgres

        1. common runtimes: http://norvig.com/21-days.html#answers

    1. used for:
        1. conditions involving equality and less/greater than
        1. sorting
        1. use with the `like` operator
           https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/like-performance-tuning
        1. basically everything except full text search

1. Many types of B-trees
    1. the official docs are very terse: <https://www.postgresql.org/docs/13/btree.html>
    1. **our main reference**: <https://habr.com/ru/company/postgrespro/blog/443284/>

    1. `README` in the source for real details: https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=src/backend/access/nbtree;h=2e3fb91ac5930dbcc0c6fc9b8b0659d9aa71bbd2;hb=HEAD
    1. postgres uses the Lehman & Yao Algorithm from 1981 ([find the original paper here](<https://www.csd.uoc.gr/~hy460/pdf/p650-lehman.pdf>))

## Algorithms for using Indexes

Table Scanning Strategies

1. Used to calculate the answer to a SQL query of the form:
   ```
   SELECT column_list
   FROM table
   WHERE condition
   ```

   Reference: <https://habr.com/ru/company/postgrespro/blog/441962/>

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
    1. All runtimes are "worst case" bounds

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
