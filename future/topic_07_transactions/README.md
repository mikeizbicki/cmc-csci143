# Transactions and Locks

## Announcements

1. Midterms Graded

    <img src=grades-midterm.png width=400px>

    <img src=grades-overall.png width=400px>

    Answer key posted to <https://github.com/mikeizbicki/csci143-midterm/blob/2024spring/sql/midterm-key.sql>.

1. If you're not satisfied with your grade, check out the [SQL extra credit github issue](https://github.com/mikeizbicki/cmc-csci143/issues/472).

## Lecture Notes

<img src=concurrency-why-did-it-have-to-be-concurrency.jpg width=400px>

1. Concurrency is when multiple programs use the database at the same time.

    1. For reading data, this is "trivial".

    1. For writing data, this is HARD.

        1. Widely considered the hardest problem in computer science.

            1. Concurrency is a major source of *nondeterminism*.
                This makes reproducing bugs very difficult.

            1. Impossibility theorems prove that there are certain things you want to do but cannot.

        1. Lots of ongoing research, very little "best practices".

        1. In this course, we will only scratch the surface.

1. There are many tools to manage concurrency

    1. These tools usually introduced in an Operating Systems course

        1. Semaphores
        1. Barriers
        1. Spinlocks
        1. Mutexes
        1. See wikipedia for more: <https://en.wikipedia.org/wiki/Synchronization_(computer_science)>

    1. Because OS-level concurrency primitives are so hard to work with, modern programming languages have introduced language-specific behavior.
        1. Common techniques include:
            1. [callbacks](https://en.wikipedia.org/wiki/Callback_(computer_programming))
            1. [async/await pattern](https://en.wikipedia.org/wiki/Async/await)
            1. [coroutines](https://en.wikipedia.org/wiki/Coroutine)
        1. In python: [asyncio module](https://docs.python.org/3/library/asyncio-sync.html)

            1. Initially added in 2015 (python 3.5)
            1. Every new version of python has been backwards incompatible
            1. We briefly covered async programming in CSCI046.

                (See the [Wardialing homework](https://github.com/mikeizbicki/wardial).)

    1. We will focus on Transactions and Locks,
        which are the tools used by databases.

**Quiz Details:**

1. Because this topic is so hard (and important),
    there will be no homework this week.
    You should spend all of your time preparing for the quiz, which will be worth 16 points.

1. The quiz will be next week Thursday (28 Mar).

1. See the files `quiz_notes.pdf` and `quiz_example.pdf`.

1. We won't cover everything in class, so you'll need to reference the postgres documentation.

    > **NOTE:**
    > Part of the reason there is no homework this week is so you have time to properly learn this quiz material.
    > I strongly recommend you read (not just skim) the references.
    >
    > <img src=read-docs.png width=250px >
    
    Postgres documentation is famously excellent.
    Part of the purpose of this class is to get you familiar with using realworld documentation.

    1. <https://www.postgresql.org/docs/current/transaction-iso.html>

       responsible for: `READ UNCOMMITTED`, `READ COMMITTED`, and `REPEATABLE READ` isolation levels

       not (for this quiz) responsible for: `SERIALIZABLE` isolation level <!-- (because the differences `REPEATABLE READ` and `SERIALIZABLE` can't be realistically tested) -->

    1. <https://www.postgresql.org/docs/current/explicit-locking.html>

       responsible for: table-level locks, row-level locks, deadlocks
       
       not (for this quiz) responsible for: page-level locks, advisory locks 

    1. <https://www.postgresql.org/docs/current/view-pg-locks.html>

        this reference explains the following useful queries for table-level locks

        ```
        SELECT relation::REGCLASS,mode,granted,pid FROM pg_locks;
        SELECT pg_backend_pid(); 
        ```

        they can be combined to get

        ```
        SELECT relation::REGCLASS,mode,granted,pid=pg_backend_pid() AS this_pid FROM pg_locks;
        ```

    1. <https://www.postgresql.org/docs/current/pgrowlocks.html>

        this reference explains the following useful query for row-level locks
        ```
        SELECT *
        FROM t, pgrowlocks('t') AS p
        WHERE p.locked_row = t.ctid;
        ```

        note that pgrowlocks is an "extension" and you must enable that extension before you can run this query

        ```
        CREATE EXTENSION pgrowlocks;
        ```

    The following two tutorial-style references might be more approachable:

    1. for isolation levels: <https://dev.to/techschoolguru/understand-isolation-levels-read-phenomena-in-mysql-postgres-c2e>

    1. for locks: <https://postgrespro.com/blog/pgsql/5967999>

    1. for UNIQUE constraints and deadlocks: <https://rcoh.me/posts/postgres-unique-constraints-deadlock/>

**ACID Guarantees**

1. RDBMSs are famous for their [ACID](https://en.wikipedia.org/wiki/ACID) guarantees.

    1. Atomicity: In a transaction involving two or more discrete pieces of information, either all of the pieces are committed or none are.

    1. Consistency: A transaction either creates a new and valid state of data, or, if any failure occurs, returns all data to its state before the transaction was started.

    1. Isolation: A transaction in process and not yet committed must remain isolated from any other transaction.

    1. Durability: Committed data is saved by the system such that, even in the event of a failure and system restart, the data is available in its correct state.

        1. Implementing durability is a CS problem that combines understanding of hardware and operating systems with databases.
            It has few DS implications, so we will not discuss it in detail.

        1. The fact that Postgres (and MySQL/SQLite) has this durability properties ensures that even when hardware fails,
           the data in the database will not be corrupted.

1. NoSQL databases (e.g. MongoDB, CassandraDB, etc.) are typically not ACID compliant,
    and so the data can be corrupted.
    For some databases, this can happen even under normal operating conditions.

    MongoDB team infamously misrepresented reports about Jepsen Analysis (a standard test suite for checking ACID compliance),
    claiming that they pass tests when they do not: <https://www.infoq.com/news/2020/05/Jepsen-MongoDB-4-2-6/>

    How MongoDB corrupted the Diaspora social network's data: <http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb/>

    How/why *The Guardian* switched from MongoDB to Postgres: <https://www.theguardian.com/info/2018/nov/30/bye-bye-mongo-hello-postgres>

1. NoSQL databases can be faster than RDBMSs (e.g. Postgres/MySQL/SQLite) because they do not have ACID guarantees...
    but it's possible to selectively turn off these features in Postgres in order to speed it up.
    (You almost certainly shouldn't do this in a real world scenario... but it's possible.)

    Example is Postgres:

    1. Unlogged tables: https://www.compose.com/articles/faster-performance-with-unlogged-tables-in-postgresql/

    1. Disable fsync: https://www.2ndquadrant.com/en/blog/postgresql-fsync-off-warning-in-config-file/

    1. Impact of full page writes: https://www.2ndquadrant.com/en/blog/on-the-impact-of-full-page-writes/

<img src=nosql.jpeg width=300px />

<!--
**Life Pro Tips:**

1. Wrap all of your SQL scripts in a transaction.

    1. Postgres is the only database that allows DDL commands in transactions, not just DQL

        DDL: Data Definition Language (e.g. `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`)

        DQL: Data Query Language (e.g. `SELECT`, `INSERT`, `DELETE`, `UPDATE`)

1. Wrap all of your `DELETE` calls within a transaction, especially in psql.

    <img src=Strip-Bas-ed-eonnée-effacée-650-finalenglish.jpg width=500px/>

    1. The Junior Dev who deleted the production database:

       https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/


1. Avoid blocking/deadlocks in your `INSERT` code by avoiding `UNIQUE`/`FOREIGN KEY` constraints that aren't necessary

   <img src=deadlock.jpg width=300px>

   but don't remove the constraints that actually ARE necessary, or you'll corrupt your data

   <img src=you-cant-have-a-deadlock-if-you-remove-the-locks.jpg width=300px>

   Some data types like `UUID` are "probabilistically unique" and so don't need a constraint
-->

## Lab

<https://github.com/mikeizbicki/lab-transactions>

## Homework

None :)
