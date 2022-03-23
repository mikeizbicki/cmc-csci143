# Midterm

<img src=midterm-scores.png width=600px>

2 perfect scores, most people lost most of their points heavily on problems 1 or 4

midterm median: 79%

overall median: 89%

**Rubric:**

1. Solutions posted to <https://github.com/mikeizbicki/pagila-midterm/tree/2022spring-solution>

1. Any problem:

    1. (-3) if you had some minor logic problems in the where clause

    1. (-3) if you didn't remove duplicates

    1. (-5) Must use a unique column in a subquery when doing filtering (penalty was not applied multiple times if you made the mistake in multiple problems)

        Problem 2:
        ```
        SELECT COUNT(DISTINCT customer_id)
        FROM film
        JOIN inventory USING (film_id)
        JOIN rental USING (inventory_id)
        WHERE title IN (
            SELECT title
            FROM film
            JOIN film_actor USING (film_id)
            JOIN actor USING (actor_id)
            WHERE first_name LIKE 'RUSSELL' AND
            last_name LIKE 'BACALL'
            );
        ```

        Problem 3:
        ```
        SELECT DISTINCT(title) FROM film
        WHERE (rating = 'R' OR rating = 'NC-17') AND
        title IN (
            SELECT title FROM film
            INNER JOIN film_category USING (film_id)
            INNER JOIN category USING (category_id)
            WHERE name = 'Children'
            );
        ```

1. Problem 1: (-10) Must use subqueries to filter on actor/customer name, where clause to filter on title

    The following is incorrect:
    ```
    select
        film.title
    from actor
    join film_actor using (actor_id)
    join film using (film_id)
    join inventory using (film_id)
    join rental using (inventory_id)
    join customer using (customer_id)
    where film.title !~ 'F'
      and actor.first_name || ' ' || actor.last_name !~ 'F'
      and customer.first_name || ' ' || customer.last_name !~ 'F'
    group by film.title;
    ```

1. Problem 4: (-10) This doesn't calculate the right thing:

    ```
    select
        f.title,
        count(distinct c.customer_id) as "similarity score"
    from film f
    join inventory using (film_id)
    join rental using (inventory_id)
    join customer c using (customer_id)
    where c.customer_id in (
        select distinct customer_id
        from customer
        join rental using (customer_id)
        join inventory using (inventory_id)
        join film using (film_id)
        where title = 'AMERICAN CIRCUS'
    )
    group by f.title
    order by "similarity score" desc;
    ```

1. Problem 5.1:

    If you missed points, one of the following conditions applied:
    1. -3 points if had anything misordered

        Common mistakes:
        1. `CHAR(256)` has typelen -1, should be on bottom
        1. `UUID` has typelen=16, should be on top

    1. -4 if you had multiple things misordered
    1. -2 if you had things ordered correctly but stated something incorrect in the comments (3 people said `CHAR(256)` has typelen=1?)

1. Problem 5.2

    -3 for any mistake


# Multi-Version Concurrency Control (MVCC)

<img src=concurrency-why-did-it-have-to-be-concurrency.jpg width=400px>

**Low level:**

1. There will be a quiz on the `notes.pdf` file.

   1. Quiz will allow arbitrary references, but no access to postgresql

   1. We will not cover everything in class,
   
      So you must learn to navigate the references

1. References:

    1. https://www.postgresql.org/docs/current/transaction-iso.html 

       responsible for: `READ COMMITTED`, and `REPEATABLE READ` isolation levels

       not responsible for: `SERIALIZABLE` isolation level

    1. https://www.postgresql.org/docs/current/explicit-locking.html

       responsible for: table/row-level locks, deadlocks
       
       not responsible for: page-level locks, advisory locks 

**High level:**

1. [ACID](https://en.wikipedia.org/wiki/ACID)

    1. Atomicity: In a transaction involving two or more discrete pieces of information, either all of the pieces are committed or none are.

    1. Consistency: A transaction either creates a new and valid state of data, or, if any failure occurs, returns all data to its state before the transaction was started.

    1. Isolation: A transaction in process and not yet committed must remain isolated from any other transaction.

    1. Durability: Committed data is saved by the system such that, even in the event of a failure and system restart, the data is available in its correct state.

        1. Implementing durability is a hard CS problem that we will ignore.

1. NoSQL databases (e.g. MongoDB, CassandraDB, etc.) are typically not ACID compliant,
  and so the data can be corrupted.
  For some databases, this can happen even under normal operating conditions.

  MongoDB team infamously misrepresented reports about Jepsen Analysis (a standard test suite for checking ACID compliance),
  claiming that they pass tests when they do not: https://www.infoq.com/news/2020/05/Jepsen-MongoDB-4-2-6/

  How MongoDB corrupted a social network's website: http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb/

  How/why The Guardian switched from MongoDB to Postgres: https://www.theguardian.com/info/2018/nov/30/bye-bye-mongo-hello-postgres

1. NoSQL databases can be faster than Postgres because they do not implement ACID...
  but it's possible to selectively turn off these features in Postgres in order to speed it up.
  (You almost certainly shouldn't do this in a real world scenario... but it's possible.)

  Unlogged tables: https://www.compose.com/articles/faster-performance-with-unlogged-tables-in-postgresql/

  Disable fsync: https://www.2ndquadrant.com/en/blog/postgresql-fsync-off-warning-in-config-file/

  Impact of full page writes: https://www.2ndquadrant.com/en/blog/on-the-impact-of-full-page-writes/

  <img src=nosql.jpeg width=500px />

**Life Pro Tips:**

1. Wrap all of your `DELETE` calls within a transaction.

    <img src=Strip-Bas-ed-eonnée-effacée-650-finalenglish.jpg width=500px/>

    1. The Junior Dev who deleted the production database:

       https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/

1. Avoid deadlocks in your `INSERT` code by avoiding `UNIQUE`/`FOREIGN KEY` constraints that aren't necessary

   <img src=deadlock.jpg width=500px>

   but don't remove the constraints that actually ARE necessary, or you'll corrupt your data

   <img src=you-cant-have-a-deadlock-if-you-remove-the-locks.jpg width=500px>
