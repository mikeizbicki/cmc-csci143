# Rollup Tables + Probabilistic Data Structures

We'll look at 3 problems and how to fix them.

## Problem 1

**Problem:**
The `count(*)` function is slow, even when using an index only scan.

1. This is a real problem impacting companies like Instagram.

   Likes stored in a table with schema:
   ```
   CREATE TABLE user_likes_media (
       id_users REFERENCES users(id_users),
       id_media REFERENCES media(id_media)
   );
   CREATE INDEX user_likes_media_idx ON user_likes_media(id_media);
   ```

   <img src=instagram_count_star.png />

   Source: https://www.youtube.com/watch?v=hnpzNAPiC0E

1. The index cannot store the count values internally because
    1. the index doesn't know which tuples are valid
    
       (recall: that's stored in the 23 bytes of overhead in the table tuples)

    1. we don't know which aggregate functions will be used in advance;

       there are special tricks we could use for `count`/`min`/`max`/`avg`, but not for `count distinct`/`median`/`mode`

**Solution:**
Cache the results.

1. Implemented natively in postgres with "materialized views".

1. Materialized views didn't exist in postgres when Instagram first launched (2010).
   (Materialized views added to postgres in version 9.3 in 2013.)
   
   So they chose an alternative solution called memcache.
   (Memcache first released in 2003.)

   Maintaining both solutions significantly complicates you system architecture.

   <img src=instagram_memcache.png />

## Problem 2

**Problem:**
Updating the cache requires recomputing the entire query from scratch.

1. This is true for both the memcache and materialized view solutions.

1. In postgres, the following command creates a materialized view
   ```
   CREATE MATERIALIZED VIEW count_view AS (
       SELECT count(*) FROM table WHERE condition;
   );
   ```
   Notice that this is just like the `CREATE VIEW` command, just with the additional word `MATERIALIZED`.
   
   The resulting `count_view` relation can be queried just like any other relation.
   The following query takes time O(1):
   ```
   SELECT count FROM count_view;
   ```

   To refresh the materialized view, issue the command
   ```
   REFRESH MATERIALIZED VIEW count_view;
   ```

**Solution:**
Rollup tables are a technique for "incrementally" updating materialized views.

1. See: https://www.citusdata.com/blog/2018/10/31/materialized-views-vs-rollup-tables/

1. Currently, they must be implemented manually
    1. complex to do (approximately 1000 lines of SQL code per rollup table)
    1. many ways to do it, each with various limitations
        1. https://stackoverflow.com/questions/47211576/refresh-only-part-of-a-materialized-view
        1. https://stackoverflow.com/questions/29437650/how-can-i-ensure-that-a-materialized-view-is-always-up-to-date
        1. https://dba.stackexchange.com/questions/86779/refresh-materalized-view-incrementally-in-postgresql
        1. https://dba.stackexchange.com/questions/165948/refresh-a-postgresql-materialized-view-automatically-without-using-triggers
        1. https://stackoverflow.com/questions/59864339/best-way-to-pre-aggregate-time-series-data-in-postgres

1. The `pgrollup` extension solves this problem by automatically implementing all of these techniques for each materialized view.

   The search engine homework assignment internally uses the `pgrollup` extension in order to cache the counts in the graph.

   1. Requirements:
      1. Every aggregate function must be a monoid homomorphism

      1. `count`/`min`/`max`/`avg` are all examples

      1. Monoid homomorphisms are also a requirement for MapReduce

   1. The oracle database has limited built-in support for rollup tables

# Problem 3

**Problem:**
The `count distinct` function is not a monoid homomorphism.

**Solution:**
The HyperLogLog data structure is a monoid that closely approximates the `count distinct` function.

1. The "most important data structure of big data"

1. Original paper from 2007: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf

1. Applications to both rollup tables and MapReduce

**Note:**
Basically every useful statistic that is not a monoid homomorphism has a probabalistic data structure that does have monoid structure.
For the median:
1. tdigest
1. kll
For the mode:
1. count min sketch
1. topk
