# Week 11: More Indexes, Full Text Search

**Homework:**

1. Week 9/10 homework was extended until this Sunday
1. twitter\_postgres2 assignment due next Sunday, 25 April

## Hash Index

1. reference: https://habr.com/ru/company/postgrespro/blog/442776/
1. btree index (this class) is to balanced binary search tree (data structures)

   as hash index (this class) is to hash tables (data structures)

    1. trees have O(log n) worst case lookup/insert/delete operations
    1. hash tables have O(1) amortized average case lookup/insert/delete operations
    1. Python dictionaries use hash tables for their implementation

1. used for:
    1. very rarely
    1. it can sometimes be marginally faster than a btree for equality search, but it supports much fewer operations, and so btree tends to be more practical
1. limitations:
    1. only support equality search
    1. does not sort results
    1. cannot decrease in size when items deleted
    1. no support for index only scans (only hash values are stored in the index, and so the table must always be checked for hash collisions)
    1. does not support multicolumn indexes
    1. older versions of postgresql have significantly more limitations
1. runtime (index scan and bitmap index scan):
    1. table pages accessed = `O(k)`, same as b-tree
    1. index pages accessed = `O(k/b)`, negligibly (why?) less than b-tree
        1. the buffer cache optimization causes b-tree index pages accessed to be effectively `O(k/b)` instead of `O(k/b + log_b n)`
            1. store the most recently accessed pages in memory
            1. top levels of a btree are accessed frequently, so they'll be in the buffer cache
            1. `shared_buffer_size` controls how many pages will be stored in memory
            1. these pages are shared by all indexes/tables
            1. makes lookups MUCH faster by avoiding disk access,
               makes insert/update/delete MUCH more complicated to implement with ACID guarantees
            1. famous joke:
               > There are 2 hard problems in computer science: cache invalidation, naming things, and off by one errors
            1. there's actually dozens of caches like this that postgres uses, and how caches work is typically covered in operating systems and computer architecture class
        1. buffer cache reference: https://habr.com/en/company/postgrespro/blog/491730/
    1. comparison operations = `O(k)` less than b-tree
    1. must consider the runtime of hashing,
       which can be large for large datatypes
1. The syntax for creating a hash index is
   ```
   CREATE INDEX tweet_tags_idx_hash ON tweet_tag USING hash (tag);
   ```

## Joining Tables

Join Strategies

1. Algorithms for computing the join of two tables
   ```
   SELECT [columns]
   FROM A
   [LEFT/RIGHT/FULL] JOIN B ON join_condition
   ```
1. Reference: https://www.cybertec-postgresql.com/en/join-strategies-and-performance-in-postgresql/

1. Three types of join strategies:
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
          1. if the data is already sorted, there's no 
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
    1. The order that joins are performed in can have a HUGE impact on the join performance
    1. It's analogous to the importance of multiplying matrices in the correct order for optimal performance
1. Postgresql's query planner tries to pick an optimal join order for you automatically
    1. If it has good statistics of the underlying tables,
       it is guaranteed to pick an optimal join order
    1. The algorithms for picking the optimal join order given good table statistics are beyond the scope of this class
    1. The important thing is to ensure that your table statistics are accurate by running the `ANALYZE` command.
1. Reference: https://www.cockroachlabs.com/blog/join-ordering-pt1/

## (Some) Difficulties of Full Text Search

Consider the following query that finds tweets containing the word `corona`:
```
SELECT id_tweets
FROM tweets
WHERE text LIKE '%corona%';
```
1. Recall that the `%` in a `LIKE`/`ILIKE` clause is a wildcard character that matches any string, much like the glob `*` in the shell.

1. Neither btree nor hash index cannot speed up this query.

1. If we only had a single wildcard,
   then we could use a btree index.
   For example, the following condition:
   ```
   WHERE text LIKE 'corona%'
   ```
   can be rewritten as
   ```
   WHERE text >= 'corona' AND text < 'coronb'
   ```
   and btree indexes support inequality search efficiently.

   **NOTE:**
   A hash index would not be able to speed up this query because it only supports exact equality search.

   **QUESTION:**
   If we replace `LIKE` with `ILIKE` in the above queries,
   how does that affect the performance of a btree index?

1. These "one-sided" wildcard queries are not useful for full text search,
   but they are useful when finding hashtags about coronavirus.
   For example, the following query finds all tweets with hashtags that start with `#corona`,
   and a btree index can be used to speed it up.
   ```
   SELECT id_tweets
   FROM tweet_tags
   WHERE tag LIKE '#corona%'
   ```

## Full Text Search (FTS) outside Postgres

1. There is no SQL standard for FTS

1. Most FTS systems are not SQL-based (i.e. NoSQL)

    1. No ACID transactions 
        1. data loss when servers crash
        1. at scale, server crashes are guaranteed => data loss guaranteed
        1. for most applications, no one will notice if you're missing a few documents in your search results, so small data loss is acceptable

           this is in contrast with other applications where data loss would be unacceptable

    1. Examples:

        1. ElasticSearch
            1. Most popular FTS engine
            1. Reasonably powerful FTS, but cannot be combined with SQL
            1. Requires installing a full service with similar complexity of postgres => difficult to configure
               <img src=one-does-not-ao1pfo.jpg />
            1. Can be embedded in postgres via [zombodb extension](https://github.com/zombodb/zombodb),
               but that's even more complicated
            1. No longer open source
                1. Originally licensed using Apache 2
                1. Elastic (the company) made money by offering their own hosted ElasticSearch solutions ($2 billion market cap)
                1. Amazon started offering ElasticSearch as a service on AWS
                1. In response, Elastic has relicensed the ElasticSearch library as SSPL
                    1. Created by MongoDB
                    1. Doesn't allow 3rd parties to offer paid hosting
                    1. Not an "open source license" officially approved by the Open Source Initiative (OSI)
                1. In response, Amazon has forked ElasticSearch, and will continue development of their forked version and offering it on AWS
                1. See:
                    1. https://opensourceconnections.com/blog/2021/01/15/is-elasticsearch-no-longer-open-source-software/
                    1. https://news.ycombinator.com/item?id=26780848
        1. Lucene / Solr
            1. Similar to Elastic, but came before, and no longer as popular
        1. Groonga
            1. Embedded FTS engine => FTS library => "easy" to include in other projects 
            1. Good Asian language support
            1. Can be embedded in postgres via [pgroonga extension](https://github.com/pgroonga/pgroonga)
                1. Easy to do
                1. No ACID guarantees on the FTS indexes => crash means you must rebuild the index (hours/days for large datasets)
                1. Doesn't respect some postgres settings about memory/disk usage

    1. Advantages of postgres:
        1. Can use full SQL capabilites (i.e. joins)
        1. Postgres FTS generally considered superior to all other RDBMs FTS (MySQL, SQL Server, Oracle, etc.)

    1. Disadvantages of postgres:
        1. must store tables/indexes separately
            1. use about 2x the disk space... sort of... when using a NoSQL solution, you still have to store your original raw data somewhere
            1. be a bit slower for inserts/update/delete and reads that have to touch table pages
            1. there's active development around removing this restriction, and it'll probably land in postgres 14 or 15
        1. doesn't support as many ranking algorithms for search
            1. again, active development to fix this issue
            1. currently (with pspacy library), postgres supports more languages than any of the NoSQL FTS solutions
        1. recall:
            1. Postgres didn't use to support `JSONB`, and so MongoDB/CassandraDB/other NoSql solutions developed around this need
            1. Postgres implemented the first JSON+SQL engine (and is still by far the best JSON support in an RDBMS, see https://www.youtube.com/watch?v=tF3Lb2BvGpk&list=PLuJmmKtsV1dP8IGGH6Z_sYQKxfDqtoSLj&index=10)
            1. Now, Postgres is "better at being Mongo than Mongo"
                1. fully supports JSON
                1. it won't lose your data
                1. it can be much faster due to good indexing
                1. you can turn off ACID guarantees to get even faster
            1. Expect the same thing to happen to FTS NoSql engines over the next few years

    1. Lots of debate about how postgres compares to NoSQL solutions: 
        1. Reference:
            1. FTS in Postgres is good enough: http://rachbelaid.com/postgres-full-text-search-is-good-enough/
            1. discussion thread: https://news.ycombinator.com/item?id=12621950
        1. No one would think it's weird if you used any of these dedicated FTS engines for a project
        1. People who don't know postgres might think it's weird to use postgres, but most people who know postgres would think it's smart, especially if you're already using postgres
        1. We'll (eventually) talk about an extension to postgres called pspacy (that I'm currently developing) that makes postgres FTS even more powerful

## FTS in postgres

1. All of the basic theory we'll discus will apply to all other FTS solutions

1. We'll start our discussion with just English text, and then later talk about non-English text

1. Two important types: `tsvector` and `tsquery`

    1. We'll only cover a basic survey here, more details in the documentation

       <img src=a5skfy5y88x11.jpg width=300px />

       Refrences:

       1. http://rachbelaid.com/postgres-full-text-search-is-good-enough/

       1. https://www.postgresql.org/docs/13/datatype-textsearch.html

       1. https://www.postgresql.org/docs/13/functions-textsearch.html

    1. `tsvector` and `tsquery` represent fully normalized text documents and queries;
       they should typically be constructed with the `to_tsvector` and `to_tsquery` functions.

       Compare the following two examples:

       ```
       SELECT 'this is a test'::tsvector;
       SELECT to_tsvector('this is a test');
       ```

    1. The following query does English language text search for tweets containing the string `coronavirus`:
       ```
       SELECT text
       FROM tweets
       WHERE to_tsvector('english', text) @@ to_tsquery('english', 'coronavirus');
       ```
       The `@@` operator should be read as "contains".

    1. The GIN/RUM indexes can be used to speed up queries that use the `@@` operator, most prominently FTS.
       ```
       CREATE INDEX tweets_idx_fts on tweets USING gin(to_tsvector('english', text));
       ```

## FTS Indexes

GIN index (Generalized Inverted iNdex)
1. reference: https://habr.com/ru/company/postgrespro/blog/448746/
1. used for:
    1. full text search
    1. indexing `JSONB`
    1. indexing arrays
    1. basically, anything that uses the `@@`, `@>`, or `<@` operators
1. limitations:
    1. elements (i.e. lexemes) never deleted
    1. slow to modify (fast mode vs slow mode)
    1. does not store auxiliary information (fixed in rum index)
        1. position of lexemes in the document
        1. timestamp/pagerank of the document
        1. must recheck the table pages
    1. does not support index scan / index only scan;
       only supports bitmap scans;

       this implies that the `LIMIT` operation is not efficient

       `gin_fuzzy_search_limit` is an alternative

       (fixed in RUM index)

    1. does not sort the results (fixed in RUM index)
    1. does not support `CLUSTER`

RUM Index
1. Reference: https://habr.com/ru/company/postgrespro/blog/452116/
1. Like the GIN index, but:
    1. also let's you store "metainformation" (e.g. pagerank, timestamp) in the index
    1. results can be returned sorted according to the metainformation
    1. can perform index only scan on the metainformation
        1. speedup from fewer pages accessed
        1. speedup from LIMIT clauses
1. limitations:
    1. slower than the GIN index for insert/update
    1. uses more space than the GIN index (due to metainfo)
    1. not built-in to postgres, and must compile/install a separate extension

GIST Index
1. Reference: https://habr.com/ru/company/postgrespro/blog/444742/
1. We won't cover in detail
1. Faster inserts, slower lookups
    1. For most applications, fast lookups are much more important than fast inserts
    1. So GIST not often used in practice for FTS
