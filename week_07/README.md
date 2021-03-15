# Week 07: Review / Multi-version Concurrency Control (MVCC)

1. What we've covered:
    1. Twitter MapReduce
    1. Docker/devops
    1. SQL queries

1. What's next:
    1. Use SQL to answer the Twitter queries is milliseconds
    1. Need to talk about how data is actually inserted/stored in postgres
    1. Indexes

1. Midterm details:
    1. I'll give the midterm at the end of class; you'll have until Sunday to complete it

---

1. [ACID](https://en.wikipedia.org/wiki/ACID)

    1. Atomicity: In a transaction involving two or more discrete pieces of information, either all of the pieces are committed or none are.

    1. Consistency: A transaction either creates a new and valid state of data, or, if any failure occurs, returns all data to its state before the transaction was started.

    1. Isolation: A transaction in process and not yet committed must remain isolated from any other transaction.

    1. Durability: Committed data is saved by the system such that, even in the event of a failure and system restart, the data is available in its correct state.

1. Implementing atomicity, consistency, durability is a hard CS problem that we will ignore.
   The fact that Postgres has these properties ensures that even when hardware fails,
   the data in the database will not be corrupted.

   1. NoSQL databases (e.g. MongoDB, CassandraDB, etc.) are typically not ACID compliant,
      and so the data can be corrupted.
      For some databases, this can happen even under normal operating conditions.

      MongoDB team infamously misrepresented reports about Jepsen Analysis (a standard test suite for checking ACID compliance),
      claiming that they pass tests when they do not: https://www.infoq.com/news/2020/05/Jepsen-MongoDB-4-2-6/

      How MongoDB corrupted a social network's website: http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb/

      How/why The Guardian switched from MongoDB to Postgres: https://www.theguardian.com/info/2018/nov/30/bye-bye-mongo-hello-postgres

   1. NoSQL databases can be faster than Postgres because they do not implement ACID...
      but it's possible to selectively turn off these features in Postgres in order to speed it up.
      (You almost certainly shouldn't do this in a real world scenaio... but it's possible.)

      Unlogged tables: https://www.compose.com/articles/faster-performance-with-unlogged-tables-in-postgresql/

      Disable fsync: https://www.2ndquadrant.com/en/blog/postgresql-fsync-off-warning-in-config-file/

      Impact of full page writes: https://www.2ndquadrant.com/en/blog/on-the-impact-of-full-page-writes/

      <img src=nosql.jpeg width=300px />

1. MVCC is how Postgres implements **isolation** within **transactions**

    1. Transactions interface:
        1. `BEGIN` starts a transaction
        1. `COMMIT` saves changes
        1. `ROLLBACK`/`ABORT` undo all changes made during the transaction
        1. Reference: https://www.postgresqltutorial.com/postgresql-transaction/

    1. Implementation details:
        1. Every transaction has a transaction id (`xid`).
           Run the following command to get it:
           ```
           SELECT txid_current_if_assigned();
           ```

        1. Every row has 6 "system columns" that make up the 23 byte overhead for each row.
           Two of these columns are particularly important for MVCC.
           Quoting [from the documentation on system columns](https://www.postgresql.org/docs/13/ddl-system-columns.html):

           1. `xmin`
              The identity (transaction ID) of the inserting transaction for this row version.

           1. `xmax`
              The identity (transaction ID) of the deleting transaction, or zero for an undeleted row version.
              It is possible for this column to be nonzero in a visible row version.
              That usually indicates that the deleting transaction hasn't committed yet, or that an attempted deletion was rolled back.

        1. A row is visible if `xmin` <= `xid` < `xmax`.

        1. Deleting a row does not actually delete data from the harddrive.
           Instead, it simply sets the `xmax` variable for the row to the current `xid`.
           If no currently running transactions are able to access the row, then the row is called "dead".

        1. Updating a row does not actually update the information on the harddrive.
           Instead, it deletes the old row and inserts a new one.

        1. The `vacuum` procedure scans a table and actually deletes the dead rows.
           You can call it manually via
           ```
           VACUUM tablename;
           ```
           A background process called `autovacuum` runs regularly on each table in order to remove these dead rows and free up disk space.
           Tuning autovacuum is important for database loads with lots of deletes/updates,
           and is a relatively difficult task that requires a fairly deep understanding of db implementation details.
           For most workloads, however, the defaults work well enough.

           Reference: https://www.percona.com/blog/2018/08/06/basic-understanding-bloat-vacuum-postgresql-mvcc/

           <img src=autovacuum.jpeg />

    1. Other oddities:
       The values in a `SERIAL` column need not be sequential.

1. Problem:
   What if two transactions try to delete the same row?
   How do we adjust the `xmax`?

   1. Answer:
      You can't do it.
      Locks prevent two transactions from adjusting the `xmax` of a single row.

      Reference: https://www.citusdata.com/blog/2018/02/15/when-postgresql-blocks/

   1. Deadlocks are what happens when two transactions cannot simultaneously finish.
