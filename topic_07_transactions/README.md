# Transactions and Locks

<img src=concurrency-why-did-it-have-to-be-concurrency.jpg width=400px>

**Quiz Details:**

1. Wednesday after spring break

1. We won't cover everything in class, so you'll need to use the references.

1. References:

    1. <https://www.postgresql.org/docs/current/view-pg-locks.html>

    1. <https://www.postgresql.org/docs/current/transaction-iso.html >

       responsible for: `READ UNCOMITTED`, `READ COMMITTED`, and `REPEATABLE READ` isolation levels

       not responsible for: `SERIALIZABLE` isolation level (because the differences `REPEATABLE READ` and `SERIALIZABLE` can't be realistically tested)

    1. <https://www.postgresql.org/docs/current/explicit-locking.html>

       responsible for: table/row-level locks, deadlocks
       
       not responsible for: page-level locks, advisory locks 

## Lecture Notes

1. [ACID](https://en.wikipedia.org/wiki/ACID)

    1. Atomicity: In a transaction involving two or more discrete pieces of information, either all of the pieces are committed or none are.

    1. Consistency: A transaction either creates a new and valid state of data, or, if any failure occurs, returns all data to its state before the transaction was started.

    1. Isolation: A transaction in process and not yet committed must remain isolated from any other transaction.

    1. Durability: Committed data is saved by the system such that, even in the event of a failure and system restart, the data is available in its correct state.

1. Implementing durability is a hard CS problem that we will ignore.
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
    (You almost certainly shouldn't do this in a real world scenario... but it's possible.)

    Unlogged tables: https://www.compose.com/articles/faster-performance-with-unlogged-tables-in-postgresql/

    Disable fsync: https://www.2ndquadrant.com/en/blog/postgresql-fsync-off-warning-in-config-file/

    Impact of full page writes: https://www.2ndquadrant.com/en/blog/on-the-impact-of-full-page-writes/

    <img src=nosql.jpeg width=500px />

**Life Pro Tips:**

1. Wrap all of your SQL scripts in a transaction.

    1. Postgres is the only database that allows DDL commands in transactions, not just DQL

        DDL: Data Definition Language (e.g. `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`)

        DQL: Data Query Language (e.g. `SELECT`, `INSERT`, `DELETE`, `UPDATE`)

1. Wrap all of your `DELETE` calls within a transaction, especially in psql.

    <img src=Strip-Bas-ed-eonnée-effacée-650-finalenglish.jpg width=500px/>

    1. The Junior Dev who deleted the production database:

       https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/

1. Avoid deadlocks in your `INSERT` code by avoiding `UNIQUE`/`FOREIGN KEY` constraints that aren't necessary

   <img src=deadlock.jpg width=500px>

   but don't remove the constraints that actually ARE necessary, or you'll corrupt your data

   <img src=you-cant-have-a-deadlock-if-you-remove-the-locks.jpg width=500px>

   Some data types like `UUID` are "probabilistically unique" and so don't need a constraint
