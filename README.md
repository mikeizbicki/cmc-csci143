# CSCI143: Big Data

<center>
<img width='100%' src=img/bigdata-knows-everything.jpg />
</center>

## About the Instructor

|||
|-|-|
| Name | Mike Izbicki (please call me Mike---[titles are lowkey insults to hackers](http://www.catb.org/jargon/html/appendixb.html)) |
| Office | Adams 216 |
| Office Hours | [see #712](https://github.com/mikeizbicki/cmc-csci143/issues/712) |
| Zoom | TBA |
| Email | mizbicki@cmc.edu (you should probably [post a github issue](https://github.com/mikeizbicki/cmc-csci040/issues) instead of email) |
| Webpage | <https://izbicki.me> |
| Research | Machine Learning (see <https://izbicki.me/research.html> for some past projects) |

Fun facts:
1. grew up in San Clemente (~1hr south of Claremont, on the beach)
1. 7 years in the navy
    1. nuclear submarine officer, personally converted >10g of uranium into pure energy
    1. worked at National Security Agency (NSA)
    1. left Navy as a [conscientious objector](https://www.nytimes.com/2011/02/23/nyregion/23objector.html)
1. phd/postdoc at UC Riverside
1. taught in [DPRK (i.e. North Korea)](https://pust.co)

Other links:

1. [My CS/DS career prospects page](https://github.com/mikeizbicki/cmc-csci143/tree/2026spring/career)

## About the Course

<!--
<center>
<img width='100%' src=map_of_cs.png />
</center>
-->

**What is big data?**

Depends entirely on the person who is talking.

1. Most non-computer scientists (muggles) think "too big for excel"
    1. $>1000$ rows
    1. $>10$ MB
1. Facebook considered ["tens of petabytes" to be a "SMALL data problem" in 2014](https://research.fb.com/blog/2014/10/facebook-s-top-open-data-problems/)
    1. a major problem in industry is people apply tools for "Facebook big data" to "muggle big data"
    1. a major goal of this course is to teach you why this is bad and how to avoid it
1. For us, "big data" means:
    1. datasets in the 10GB-10TB range
        1. too big to fit in memory
        1. need $O(1)$ memory and $O(n)$ time algorithms
        1. no pandas
    1. all the interesting/applied parts of upper division computer science compressed into a single course
        1. shell scripting
        1. mapreduce
        1. git
        1. continuous integration / test driven development
        1. docker / docker-compose
        1. (**50% of course**) SQL using sqlite3 / postgres
        1. Instagram tech stack
        1. large language models (LLMs)

**Who should take this course?**

This course is designed for **data science majors**,
not computer science majors.
I'm happy to have CS majors in this course (and I think you'll find this course fun), but know that:

1. you probably have not fully met the prereqs for this course
1. some material in this course will duplicate material in your other CS courses
    1. this is especially true of CSCI133 Databases
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
    1. A lot of the concepts we'll be covering "should" be covered in other CS courses,
       but because CS professors are often more theory minded than practice minded,
       they don't get covered.
       In that sense, this course is similar to the [Missing Semester of Your CS Education](https://missing.csail.mit.edu/) course taught at MIT.

1. Concepts we don't cover from CSCI133 Databases
    1. relational algebra
    1. technical implementation details / C programming
    1. relationship between the database and operating system

1. BigData concepts from a CS perspective that we will not talk about:
    1. Frameworks for distributed computation (e.g. Apache Hadoop, Apache Spark)
    1. Distributed Filesystems (e.g. HDFS, IPFS, S3)
    1. Geo-distributed databases

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

## Grades

**Assignments:**

1. Weekly labs (worth `2**1` or `2**2` or `2**3` points)
1. Weekly quizzes (worth `2**2` or `2**3` or `2**4` points)
1. Weekly homeworks (worth `2**3` or `2**4` or `2**5` points)
1. No exams!
1. Non-graduating students will have a final project.

All assignments are designed to help you get a good job.  (See [/career/README.md](/career/README.md).)
1. All code, no math.
1. You will build your github portfolio.
1. You will do cool stuff to talk about in interviews (analyze ALL tweets about covid, build an Instagram clone).
1. The assignments will help you with SQL technical interview questions.

See <https://github.com/mikeizbicki/cmc-csci143/issues/577> for extra credit opportunities.

**Late Work Policy:**

You lose `2**(i-1)` points on every assignment,
where `i` is the number of days late.

Do not expect partial credit for incomplete assignments.
It is much better to submit a correct assignment late than an incorrect one on time.

**Caveats:**

There are 2 "caveat tasks" in this course.
These tasks should be easy, and everyone will get full credit on the task just for completing the task.
If you don't complete one of the tasks, however, your grade will be docked 10%.
(For example, an A- grade would become a B- grade.) 
You have the entire semester (until I submit grades) to complete these tasks.

You can find the details about the caveat tasks at:
1. [caveat_tasks/typespeed.md](caveat_tasks/typespeed.md)
1. [caveat_tasks/culture.md](caveat_tasks/culture.md)

## Academic Integrity

**Technology Policy:**

1. You MAY use any AI tool without restriction.

1. You MUST complete all programming assignments on the lambda server.

1. You MUST use either Vim or Emacs for all text editing.

   In particular, you MAY NOT use the GitHub text editor, VSCode, IDLE, or PyCharm for any reason.

1. You MAY NOT share your lambda server credentials with anyone else.

**Collaboration Policy**

See <https://github.com/mikeizbicki/cmc-csci143/issues/592>.

## Accommodations

I've tried to design the course to be as accessible as possible for people with disabilities.
(We'll talk a bit about how to design accessible software in class too!)
If you need any further accommodations, please ask.

I want you to succeed and I'll make every effort to ensure that you can.

<!--
# topic change
Need to cover TTY vs non-TTY stdin/stdout in the first 2 weeks of class on bash.

In particular, docker exec defaults to non-TTY and must add -it to get TTY, but docker-compose defaults to TTY and must add -T to get non-tty

Properly escape the \x00 in the twitter_postgres assignment

Add functions to the first pagila assignments
-->

<!--

diabolical queries:

select count(*) tablename     vs     select count(*) from tablename


NOTES:

Next midterm should include a COUNT (DISTINCT customer_id) trick question.

JOIN keys to join on; (customer_id can link customer to both payment and rentals)

INDEX PROBLEM:

Find all the coupons that are expired (90 day expiration):

    SELECT * FROM coupon
    WHERE created_at + INTERVAL '90 DAY' < now()

This will not use the index on the "created_at" column and will be slow.

You should rewrite the inequality to:

    SELECT * FROM coupon
    WHERE created_at < now() - INTERVAL '90 DAY'

and now the query will be much faster. There are a lot of cases in postgres where simple equivalent algebraic manipulations can completely change the query plan

 They are not equivalent since `created_at + INTERVAL '90 DAY'` can overflow for every single row whereas `now() - INTERVAL '90 DAY'` is a constant for the purpose of the query execution.

 reply
    
        
        CWuestefeld 2 hours ago | root | parent | next [–]

        Yes - this is a common restriction in any DB I've used, certainly in MS SQL Server. The idea is that your queries need to be "SARGable": https://en.wikipedia.org/wiki/Sargable
-->
