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
    1. postgres uses the [Lehman & Yao Algorithm from 1981](https://www.csd.uoc.gr/~hy460/pdf/p650-lehman.pdf)

## Algorithms for using Indexes

1. Basic idea:

    1. You write a `SELECT` statement which describes "what" you want
    1. The *query planner* automatically determines "how" to calculate it 
        1. It will re-write your SQL queries into more efficient expressions
        1. It will choose the best algorithms for your particular combination of hardware, data, indexes, and query expressions
        1. There are various theorems that prove that no system can perform these steps optimally in all circumstances,
           but it still is pretty good
        1. To fully understand the query planner, you should take a course on compilers
        1. Reference: <http://www.interdb.jp/pg/pgsql03.html>

    1. `EXPLAIN`
        1. Shows which algorithms postgres will use for any query
        1. Used to debug all performance problems in postgres

           <img src=explain_analyze.jpg />


1. Definitions:

    1. `n` = number of tuples in the table
    1. `a` = number of tuples per page in the table
    1. `b` = branching factor of the B-Tree
    1. `k` = number of rows returned by the `SELECT`
    1. All runtimes are "worst case" bounds

### Table Scanning Strategies

Used to calculate the answer to a SQL query of the form:
```
SELECT column_list
FROM table
WHERE condition
```

<!--   Reference: <https://habr.com/ru/company/postgrespro/blog/441962/> -->

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
            1. if not vacuumed regularly, then potentially up to `O(k)`
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
            1. Note that the number of pages is `O(n/a)`, and k is only guaranteed to be <= n, so this can potentially access more pages than exist in the table!
            1. No guarantee that the same page will not be accessed multiple times
            1. Caching of pages in memory somewhat mitigates this problem
        1. index pages accessed = `O(log_b n + k/b)`
        1. comparison operations = `O(b*log_b n + k)`
        1. medium constant factor
    1. Used when (AND):
        1. `k << n/a`
        1. only one index will be consulted

1. Bitmap Scan
    1. Most complicated scan method
        1. For each condition in the `WHERE` clause that matches an index:
            1. Create a list of all TIDs in the index that match the condition
            1. Compute a "bitmap" of all pages that contain these tuples
        1. Compute the `AND`/`OR` of the bitmaps as appropriate
        1. Scan only the pages in the final bitmap
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
        1. Cannot return results in sorted order


### Sorting Strategies

Used for:

1. Adding an `ORDER BY` clause
1. When other components need sorted data

Two basic strategies:

1. Explicit sort
    1. Technically, 3 different types:
        1. If the table scan data fits into `work_mem` (typically 20MB), then:
            1. Top-N Heap Sort if `LIMIT N` clause

                Comparison Ops: `O(n + N log N)`

            1. otherwise Quicksort

                Comparison Ops: `O(n log n)`
        1. Otherwise a specialized merge sort that saves intermediate steps to the harddrive

        1. Reference: <https://www.cybertec-postgresql.com/en/postgresql-improving-sort-performance/>

    1. Really good/fancy code here... but it's sorting is intrinsically slow `Omega(n)`... and so you should try to avoid sorting

    <img src=sort.jpg width=400px />

1. Use an index
    1. Only applicable for index only/index scan (i.e. not bitmap scan)

### Aggregate Strategies

Used for:

1. `GROUP BY` clause
1. Aggregate functions (e.g. `count`, `sum`, `max`, etc.)

Two Strategies:

1. GroupAggregate
    1. Dis:
        1. Requires sorted input data
    1. Adv:
        1. Needs less memory
        1. Returns sorted data
        1. Returns data continuously
        1. Can perform complex aggregates like `COUNT (DISTINCT x)`

1. HashAggregate
    1. Adv:
        1. Always applicable
    1. Dis:
        1. Needs more memory
        1. Returns unsorted data
        1. Must finish all computation before returning data
        1. Can only perform basic aggregations
    
Reference:
1. <https://www.slideshare.net/AlexeyBashtanov/pgday-uk-2016-performace-for-queries-with-grouping>
1. <https://www.cybertec-postgresql.com/en/postgresql-speeding-up-group-by-and-joins/>

### Join Strategies

Used for:
1. Any type of join (e.g. cross/inner/left outer/right outer/full outer)
1. Only join exactly 2 tables at a time

Reference:
1. <https://www.cybertec-postgresql.com/en/join-strategies-and-performance-in-postgresql/>

Three types of join strategies:

1. Nested loop join
   1. works in all scenarios
   1. without an index
      1. pseudocode looks like
         ```
         for each row a in A:
             for each row b in B:
                 if a,b satisfy join condition:
                     output a,b
         ```
      1. runtime is `O(mn)`, where `m` is size of `A` and `n` is size of `B`
   1. with an index
      1. replace the inner for loop with an index only/index/bitmap scan:
      1. pseudocode looks like
         ```
         for each row a in A:
             find rows b in B satisfying join condition:
                 output a,b
         ```
      1. runtime is `O(m log n)`
   1. Recall that joins are commutative
      1. That is,
         ```
         SELECT [columns]
         FROM A
         [LEFT/RIGHT/FULL] JOIN B USING join_condition
         ```
         is equivalent to 
         ```
         SELECT [columns]
         FROM B
         [LEFT/RIGHT/FULL] JOIN A USING join_condition
         ```
      1. So we can also do
         ```
         for each row b in B:
             find rows a in A satisfying join condition:
                 output a,b
         ```
      1. runtime is `O(n log m)`

1. Hash join
   1. requires:
      1. equality join condition
      1. hash table must fit inside `work_mem` parameter
      1. large initial overhead to build the hash table before we can start outputing tuples
   1. pseudocode looks like
      ```
      Build hash table for join column on B
      for each row a in A:
          if join column in hash table:
              recheck row b in B for a hash collision
              if no collision:
                  output a,b
      ```
   1. runtime is `O(m + n)`, with a large overhead
       1. if we have a `LIMIT k` clause, and every row in A has a corresponding row in B, then the runtime is `O(n + k)` because the for loop will stop early, but we still must build the hash table

1. Merge join
   1. like the merge step in merge sort
   1. requires:
      1. sorted inputs
      1. equality join condition
   1. advantages:
      1. if the data is already sorted, there's no setup overhead
      1. can early stop if only a small number of rows needed
   1. pseudocode looks like
      ```
      i,j = 0
      while i<m and j<n:
          a = A[i]
          b = B[j]
          if a,b satisfy join condition:
              output a,b
          if join column of a < join column of b:
              i += 1
          else:
              j += 1
      ```
   1. runtime is `O(m + n)` with a small overhead
       1. if we have a `LIMIT k` clause, then the runtime is `O(k)` because while loop will stop early

1. Conclusions:
   1. merge/hash join faster than nested loop join whenever tables are reasonably large
   1. asymptotically, indexes don't give us much benefit unless you have a `LIMIT k` clause in your query
   1. they can remove the need for the sort step, allowing for faster merge joins


Join Order

1. Join strategies only join 2 tables at a time
    1. When we join multiple tables, we must decide the order to do the joins in

        The order that joins are performed in can have a HUGE impact on the join performance

        See: <https://www.querifylabs.com/blog/introduction-to-the-join-ordering-problem>

    1. It's analogous to the importance of multiplying matrices in the correct order for optimal performance

        Famous dynamic [programming algorithm for solving](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)

1. Postgresql's query planner tries to pick an optimal join order for you automatically
    1. If it has good statistics of the underlying tables,
       it will pick a good join order
    1. The algorithms for picking the join order given good table statistics are beyond the scope of this class
    1. The important thing is to ensure that your table statistics are accurate by running the `ANALYZE` command.

1. Reference: <https://www.cockroachlabs.com/blog/join-ordering-pt1/>

### Parallelism

Postgres will automatically parallelize queries

<img src='5ParallelismFTW.jpg' width=300px />

1. All SQL queries can be parallelized in theory
    1. In practice, not 100% of queries can be parallelized in postgres due to technical engineering issues
    1. The devs are working to fix this
1. Parallelism incurs a (small) constant overhead to setup,
   and so very small queries will not be parallelized

1. References
    1. <https://www.postgresql.org/docs/13/parallel-plans.html>
    1. <https://www.postgresql.org/docs/13/how-parallel-query-works.html>
    1. Extensive details: <https://wiki.postgresql.org/wiki/Parallel_Internal_Sort>

1. You need to be able to read the documentation and answer arbitrary questions about it

### Other Concepts

You must know how the following concepts relate to all of the query plan strategies discussed above.

1. Multicolumn indexes
1. Expression indexes
1. Partial indexes
1. `UNIQUE` indexes (with and without an `INCLUDE` statement)

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
