# MVCC Implementation

## Announcements

**Monday, 28 March:**

1. I've regraded problem 4 from the midterm

    1. I made a mistake with my initial grading (my sincere apologies)

    1. Many people got the full 10 points back, many other people got 5/10 points

    1. Some people "should" have lost points, but I didn't take them away

1. Quiz on transactions/locks will be Monday 4 April

1. Homework posted due Sunday 3 April

1. Several people have emailed me about extra credit... these discussions must happen in person and not over email

1. We will finish up week 9 notes today before starting on the material below

## Lecture Notes

**Reading:**

1. You are responsible for everything in chapters 1,2,5,6 in the book <http://www.interdb.jp/pg>

    This covers the implementation details of MVCC.
    These details will help you understand:
    
    1. why locks work the way they do
    1. the "table overhead" (we previously talked about "row overhead" only)
    1. how to make SQL `SELECT` queries fast
        1. next section of class covers the algorithms used for these queries,
            and you'll need to know the MVCC details

**Important Highlights From the Reading:**

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

1. Deleting a row does not actually delete data from the harddrive.
   Instead, it simply sets the `xmax` variable for the row to the current `xid`.
   This is necessary so that other transactions can still see the row.

   Similarly, updating a row does not actually update the information on the harddrive.
   Instead, it deletes the old row and inserts a new one.

1. Determining whether a row is "visible" or "invisible" is a complex formula involving the `xmin` and `xmax` system columns (and several other pieces of information).
   See http://www.interdb.jp/pg/pgsql05.html for a detailed description.

   If a row is not visible to any currently running transactions,
   then the row is called "dead".
   Dead tuples waste disk space.

1. `xid` numbers are 4-byte unsigned integers => "only" 4.2 billion transactions possible.

    It's actually very common to exceed this number in practice => transaction wraparound problem.

1. The `VACUUM` procedure scans a table and actually deletes the dead tuples from a page file.
   You can call it manually via
   ```
   VACUUM tablename;
   ```
   A background process called `autovacuum` runs regularly on each table, automatically vacuuming the table for you. 

    1. Vacuuming a table is an expensive procedure.
        For large tables (>1gb),
        vacuuming can easily take days.

    1. The **visibility map (VM)** is used to determine which pages need to be vacuumed (i.e. have dead tuples), and greatly speeds up this process.

    1. Regular vacuuming ensures that most pages do not have dead tuples, so that vacuuming remains fast.
        The autovacuum process does this vacuuming for you automatically.

        Tuning autovacuum is important for database loads with lots of deletes/updates,
        and is a relatively difficult task that requires a fairly deep understanding of db implementation details.
        For most workloads, however, the defaults work well enough.

        <img src=autovacuum.jpeg />

    1. `VACCUM` acuires a `SHARE UPDATE EXCLUSIVE` lock.
        While a table is being vacuumed,
        most SQL operations can be performed (e.g. `SELECT`/`UPDATE`/`DELETE` are okay),
        but certain operations like creating an index are blocked.

        If the `CREATE INDEX` command blocks due to autovacuum, it's tempting to disable autovacuum.

        **First Rule of Postgres Admin:** Never disable autovacuum.

    1. Many database designers try to avoid creating a database that will require `UPDATE`/`DELETE` commands in order to avoid the difficulties associated with vacuuming,
        although it's not always possible to completely avoid these commands.

    1. Because of vacuuming,
       there is often free space in the table file that is not at the end of the table.
       New tuples will get inserted into this free space.
       The physical order of rows in the database therefore has no semantic meaning,
       it is 100% arbitrary.

       The **free space map (FSM)** is used to determine which page to insert a tuple into.

    1. Even though vacuuming a table deletes dead tuples,
       it does not "defragment" the tuples or delete "pages".
       Therefore, it cannot actually remove any disk space.
       The "full vacuum" is required to actually free up the disk space,
       and it can be run via
       ```
       VACUUM FULL tablename;
       ```
       The downside of this command is that it requires an `ACCESS EXCLUSIVE` lock,
       so no other process can modify the table during a full vacuum.

1. For workloads that involve updates/deletes,
   it is essentially impossible to predict how much disk space the database will use.
   This will depend on a complex interaction between the amount of data, and the orders of updates/deletes.
   Typical overhead factors are between 2-4x,
   but could easily be more.

<!--
1. Other oddities:
   The values in a `SERIAL` column need not be sequential.

   If you add a row to a table within a transaction,
   new numbers will be generated for any serial columns.
   If the transaction is aborted,
   these numbers will remain unused,
   and future inserts will continue as if the transaction occurred.
-->
