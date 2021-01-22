## CSCI143: Big Data

<center>
<img width='100%' src=bigdata-knows-everything.jpg />
</center>

## About the Instructor

|||
|-|-|
| Name | Mike Izbicki (call me Mike) |
| Email | mizbicki@cmc.edu |
| Office | Adams 216 |
| Office Hours | MW 2pm-3pm, or by appointment |
| Webpage | [izbicki.me](https://izbicki.me) |
| Research | Machine Learning (see [izbicki.me/research.html](https://izbicki.me/research.html) for some past projects) |

Fun facts:
1. grew up in San Clemente
1. 7 years in the navy
1. phd/postdoc at UC Riverside
1. taught in [DPRK](https://pust.co)
1. My wife is pregnant and due to have a baby early April.
   This may result in a class session being rescheduled,
   depending on when the baby decides to come.

## About the Course

<center>
<img width='100%' src=map_of_cs.png />
</center>

**What is big data?**

1. Depends entirely on the person who is talking
    1. Most non-computer scientists think anything bigger than 1G is big data
    1. Facebook considers ["tens of petabytes" to be a "SMALL data problem"](https://research.fb.com/blog/2014/10/facebook-s-top-open-data-problems/)
1. For us, "big data" means:
    1. managing a cluster of computers to solve a computational problem; if it can be solved on a single computer, it's SMALL data
    1. all the interesting/applied parts of upper division computer science compressed into a single course

We will work with the following three datasets:

1. All geolocated tweets sent from 2017-today, 4 terabytes
1. The [common crawl](https://commoncrawl.org/) of the web since 2008, >1 petabyte
1. The [internet archive](https://archive.org/web/petabox.php), >50 petabytes as of 2014

By the end of this course, you will build your own "google" search engine.
You will manage a cluster of machines that work together to:
1. download all the data from the internet
1. analyzing it
1. store it in a format suitable for [sub 200ms queries](https://developers.google.com/speed/docs/insights/Server)
1. and serve the data in a webpage

In order to make your search engine scalable, we will use the following technologies:

1. Docker containers
    1. used to easily deploy code to thousands of computers
    1. requires concepts from operating systems, networks, architecture
    1. widely used in industry, see https://stackshare.io/docker

1. Postgresql / sqlite3 databases
    1. stores and accesses the data efficiently
        1. on 1 computer
        1. on >1 computers in the same data center
        1. on >1 data centers spread throughout the world
    1. SQL to manipulate data, Python to build applications
    1. implements full text search in 70+ languages using custom libraries I've written
    1. widely used in industry, see https://stackshare.io/postgresql

1. With these technologies, you can create a fully functioning, highly scalable web business
    1. former CMC student Biniyam Asnake created the business [NextDorm](https://www.nextdorm.college/cmc/browse?search=politics) as his senior thesis

<!--
Example search engines:
1. Camas reddit search: https://camas.github.io/reddit-search/
1. Have I Been Pwned? https://haveibeenpwned.com/
-->

**Who should take this course?**

This course is designed for **data science majors**, not computer science majors.
I'm happy to have CS majors in this course (and I think you'll find this course fun), but know that:

1. you probably have not fully met the prereqs for this course
1. some material in this course will duplicate material in your other CS courses
    1. you should not take both this course and CSCI133 Databases
    1. the course number CSCI143 comes from the fact that all CMC upper division CS courses start with CSCI14, and the 3 is for databases

**Prerequisites:**

1. Discrete math: CSCI055 or MATH055

    1. Basic probability / counting
    1. Basic graph theory

1. Foundations of data science: CSCI 036, ECON 122, or ECON 160

    1. Basic machine learning
    1. Basic SQL (also covered in  CSCI040 Computing for the Web; not covered in any computer science class except CSCI133 Databases, which you should not take if you take this course)
    1. Regular expressions (for CS majors, typically covered in a theory of computing or compilers class)

1. Data structures: CSCI046 or CSCI70 (Mudd) or CSCI62 (Pomona)

    1. All courses cover:
        1. Big-oh notation
        1. Balanced binary search trees
    1. CSCI046 covers:
        1. Basic Unix shell commands
        1. Advanced git
        1. Vim text editor
        1. Analyzing multi-gigabyte Twitter datasets
    1. Data structures pre-req CSCI040:
        1. Markdown
        1. HTML / CSS
        1. Basic SQL
        1. Programming web servers with the `flask` library
        1. Web scraping with the `requests` and `bs4` libraries

**Relation to other CS courses:**

One purpose of this course is to provide DS majors with an overview of CS concepts.
Therefore, there is a lot of material in this course that is covered in other upper division CS courses required for CS majors.

1. Overlapping concepts
    1. CSCI105 Computer Systems (10% overlap)
        1. types of storage: tape vs HDD vs SDD vs NVME vs RAM
        1. RAID
        1. parallel vs distributed architectures
    1. CSCI135 Operating Systems (10% overlap)
        1. permissions systems
        1. processes vs threads
        1. virtual machines vs containers
    1. CSCI125 Networking (10% overlap)
        1. private vs public networks
        1. IP addresses
        1. TCP ports
        1. virtual networks
    1. CSCI121 Software Development (10% overlap)
        1. version control systems (i.e. git)
        1. test driven development / continuous integration
        1. microservices vs monolithic architectures
        1. 12 factor applications
    1. CSCI133 Databases (50% overlap)
        1. SQL
        1. ACID/MVCC/transactions
        1. indexing techniques

1. Concepts we don't cover from CSCI133 Databases
    1. relational algebra
    1. technical implementation details / C programming
    1. relationship between the database and operating system

**Textbook:**

Big data is a rapidly changing field,
and all currently printed textbooks are both incomplete and already out of date.
Therefore, we won't be using a textbook.
Instead, we will be using online documentation.
The main references we will use are given below,
but I will provide more specific links each week.

1. [Docker documentation](https://docs.docker.com/)

1. [Postgresql documentation](https://www.postgresql.org/docs/)

1. [SQLite documentation](https://sqlite.org/docs.html)

1. [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/13/)

1. [12 Factor Web Apps](https://12factor.net/)

**Grades:**

You will have:

1. Occasional labs (worth 2pts each)
1. Weekly homeworks (worth 10-25 points each)
1. Twitter MapReduce project (worth 20 points)
1. One open notes midterm (20 points, week after spring break)
1. One open notes final (30 points, during finals week)
1. In total, there will be about 250 points in the class.

Your final grade will be computed according to the following table,
with one caveat.

| If your grade satisfies          | then you earn |
| -------------------------------- | ------------- |
| 95 &le; grade                    | A             |
| 90 &le; grade < 95               | A-            |
| 87 &le; grade < 90               | B+            |
| 83 &le; grade < 87               | B             |
| 80 &le; grade < 83               | B-            |
| 77 &le; grade < 80               | C+            |
| 73 &le; grade < 77               | C             |
| 70 &le; grade < 73               | C-            |
| 67 &le; grade < 70               | D+            |
| 63 &le; grade < 67               | D             |
| 60 &le; grade < 63               | D-            |
| 60 > grade                       | F             |

*CAVEAT:*
In order to get an A/A- in this course,
you must also complete one of the following two tasks to learn about the history of unix programming:

1. watch the following documentaries:

    1. [RevolutionOS](https://www.youtube.com/watch?v=4vW62KqKJ5A) (from 2001)

    1. [The Internet's Own Boy: The Story of Aaron Swartz](https://www.youtube.com/watch?v=9vz06QO3UkQ) (from 2014)

1. read chapters 1-3 of [The Art of Unix Programming](http://catb.org/~esr/writings/taoup/html/context.html) by ESR

**Late Work Policy:**

You lose 10% on labs/projects for each day late.
If you have extenuating circumstances, contact me in advance of the due date and I may extend the due date for you.

## Schedule

<!--
https://en.wikipedia.org/wiki/Amdahl%27s_law

Scan methods: https://severalnines.com/database-blog/overview-various-scan-methods-postgresql

Join methods: https://severalnines.com/database-blog/overview-join-methods-postgresql

Linux - 2 weeks
SQL - 2 weeks
Python+SQL - 1 week
Docker - 1 week

Postgres functions - 1 week
Postgres vaccuum / table overhead - 1 week
Triggers - 1 week

Indexes - 2 weeks
-->

| Week | Date        | Topic                                                |
| ---- | ----------- | ---------------------------------------------------- |
| 0    | M, 25 Jan   | DevOps: Unix Shell                                   |
| 0    | W, 27 Jan   | DevOps: Unix Shell                                   |
| 1    | M, 01 Feb   | DevOps: Docker                                       |
| 1    | W, 03 Feb   | DevOps: Docker                                       | <!-- Fri, 5 Feb is last day to add/drop -->
| 2    | M, 08 Feb   | DevOps: CRUD Apps                                    | 
| 2    | W, 10 Feb   | DevOps: CRUD Apps                                    | 
| 3    | M, 15 Feb   | SQL: Basics                                          |
| 3    | W, 17 Feb   | SQL: Basics                                          |
| 4    | M, 22 Feb   | SQL: Intermediate Data Types                         |
| 4    | W, 24 Feb   | SQL: Intermediate Data Types                         | 
| 5    | M, 01 Mar   | SQL: ACID/MVCC/Transactions                          | <!-- unlogged tables -->
| 5    | W, 03 Mar   | SQL: ACID/MVCC/Transactions                          |
| 6    | M, 08 Mar   | **Spring Break**                                     |
| 6    | W, 10 Mar   | **Spring Break**                                     |
| 7    | M, 15 Mar   | SQL: ACID/MVCC/Transactions                          |
| 7    | W, 17 Mar   | SQL: ACID/MVCC/Transactions                          |
| 8    | M, 22 Mar   | Search: b-tree                                       |
| 8    | W, 24 Mar   | Search: b-tree                                       |
| 9    | M, 29 Mar   | Search: Multilingual Full Text Search                |
| 9    | W, 31 Mar   | Search: Multilingual Full Text Search                | <!-- Cesar chavez day, observed on Friday -->
| 10   | M, 05 Apr   | Search: Multilingual Full Text Search                |
| 10   | W, 07 Apr   | Search: Multilingual Full Text Search                |
| 11   | M, 12 Apr   | Counting: Triggers                                   |
| 11   | W, 14 Apr   | Counting: Triggers                                   |
| 12   | M, 19 Apr   | Counting: Probabilistic Data Structures              |
| 12   | W, 21 Apr   | Counting: Probabilistic Data Structures              |
| 13   | M, 26 Apr   | Counting: Probabilistic Data Structures              |
| 13   | W, 28 Apr   | Counting: Probabilistic Data Structures              |
| 14   | M, 03 May   | DBA (DataBase Admin)                                 |
| 14   | W, 05 May   | DBA (DataBase Admin)                                 |

## Technology Policy

1. You must complete all programming assignments on the lambda server.

1. You must use either vim or emacs to complete all programming assignments.
   In particular, you may not use VSCode, IDLE, or PyCharm for any reason.

1. You must not share your lambda-server password with anyone else.

Violations of any of these policies will be treated as academic integrity violations.

## Collaboration Policy

You are encouraged to discuss all labs and projects with other students,
subject to the following constraints:

1. you must be the person typing in all code for your assignments, and
1. you must not copy another student's code.

You may use any online resources you like as references.

**WARNING:**
All material in this class is cumulative.
If you work "too closely" with another student on an assignment,
you won't understand how to complete subsequent assignments,
and you will quickly fall behind.
You should view collaboration as a way to improve your understanding,
not as a way to do less work.

**You are ultimately responsible for ensuring you learn the material!**

## Accommodations for Disabilities

I've tried to design the course to be as accessible as possible for people with disabilities.
(We'll talk a bit about how to design accessible software in class too!)
If you need any further accommodations, please ask.

I want you to succeed and I'll make every effort to ensure that you can.

<!--

diabolical queries:

select count(*) tablename     vs     select count(*) from tablename

-->
