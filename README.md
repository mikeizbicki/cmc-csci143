## CSCI143: Big Data

<center>
<img width='100%' src=bigdata-knows-everything.jpg />
</center>

[Career information](career.md)

## About the Instructor

|||
|-|-|
| Name | Mike Izbicki (call me Mike) |
| Email | mizbicki@cmc.edu |
| Office | Adams 216 |
| Office Hours | See [Issue #243](https://github.com/mikeizbicki/cmc-csci143/issues/243) |
| Zoom Link | See [Issue #227](https://github.com/mikeizbicki/cmc-csci143/issues/227) |
| Webpage | [izbicki.me](https://izbicki.me) |
| Research | Machine Learning (see [izbicki.me/research.html](https://izbicki.me/research.html) for some past projects) |

Fun facts:
1. grew up in San Clemente (~1hr south of Claremont, on the beach)
1. 7 years in the navy
    1. nuclear submarine officer, personally converted >10g of uranium into pure energy
    1. worked at National Security Agency (NSA)
    1. left Navy as a [conscientious objector](https://www.nytimes.com/2011/02/23/nyregion/23objector.html)
1. phd/postdoc at UC Riverside
1. taught in [DPRK (i.e. North Korea)](https://pust.co)
1. my wife is pregnant and due to have a baby April 18th
    1. I'll be taking 2 weeks paternity leave when the baby comes

## About the Course

<center>
<img width='100%' src=map_of_cs.png />
</center>

**What is big data?**

Depends entirely on the person who is talking
1. Most non-computer scientists (muggles) think anything bigger than 1G is big data
1. Facebook considers ["tens of petabytes" to be a "SMALL data problem"](https://research.fb.com/blog/2014/10/facebook-s-top-open-data-problems/)
1. One of the biggest problems in industry is people apply tools for "Facebook big data" to "muggle big data",
   and a major goal of this course is to teach you why this is bad and how to avoid it
1. For us, "big data" means:
    1. managing a cluster of computers to solve a computational problem; if it can be solved on a single computer, it's SMALL data
    1. all the interesting/applied parts of upper division computer science compressed into a single course

We will work with the following three datasets:

1. All geolocated tweets sent from 2017-today, 4 terabytes
1. ~~The [common crawl](https://commoncrawl.org/) of the web since 2008, >1 petabyte~~
1. ~~The [internet archive](https://archive.org/web/petabox.php), >50 petabytes as of 2014~~

By the end of this course, you will build your own "google" search engine.
You will manage a cluster of machines that work together to:
1. download all the data from the internet
1. extract key information from the HTML
1. store it in a format suitable for [sub 200ms queries](https://developers.google.com/speed/docs/insights/Server)
1. and serve the data in a webpage

In order to make your search engine scalable, we will use the following technologies:

1. Docker containers
    1. used to easily deploy code to thousands of computers
    1. requires concepts from operating systems, networks, architecture; closely related to "virtual machines"
    1. widely used in industry, see https://stackshare.io/docker

1. Databases
    1. stores and accesses the data efficiently
        1. application and database on same computer (SQLite, covered in CS40)
        1. application and database on different computers (Postgres), **our focus**
        1. database on a cluster of computers in the same datacenter (Postgres + extensions like Citus)
        1. database on a cluster of computers spread throughout the world ([YugabyteDB](https://docs.yugabyte.com/), [CocroachDB](https://www.cockroachlabs.com/docs/stable/))
    1. SQL to manipulate data, python to build applications
    1. NoSQL (e.g. MongoDB, CouchDB) sucks and you should probably never use it (strongly held personal opinion)
    1. Postgres implements full text search in 70+ languages using custom libraries I've written
    1. Postgres widely used in industry, see https://stackshare.io/postgresql

1. With these technologies, you can create a fully functioning, highly scalable web business
    1. former CMC student Biniyam Asnake created the business [NextDorm](https://www.nextdorm.college/cmc/browse?search=politics) as his senior thesis (slightly different tech stack, but same ideas)

<!--
Example search engines:
1. Camas reddit search: https://camas.github.io/reddit-search/
1. Have I Been Pwned? https://haveibeenpwned.com/
-->

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

1. Takeaway:
    1. I am expecting that you have basic familiarity with the Linux terminal, git, and SQL joins.
    1. If you haven't seen those concepts before, expect to spend extra time those weeks catching up.
    1. There are also extra assignments that certain people will have to complete depending on your background.

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
    1. Distributed Filesystems (e.g. HDFS, IPFS); we will talk about S3
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

<!--
1. Occasional labs (worth 1-5 points each)
1. Occasional quizzes (worth 10-30 points each)
1. Weekly homeworks (worth 10-30 points each)
    1. First 2 homeworks only for students who did not take CS46 with me
1. One open notes midterm (80 points)
1. One open notes final (120 points)
1. Non-seniors will have a final project (50 points)
1. Extra credit, as posted in [#85](https://github.com/mikeizbicki/cmc-csci143/issues/85)
1. In total, there will be between 400-500 points in the class.
-->

1. Weekly labs (worth `2**1` points)
1. Weekly quizzes (worth `2**2` or `2**3` or `2**4` points)
1. Weekly projects (worth `2**3` or `2**4` or `2**5` points)
1. 2 exams (worth `2**6` points each)
    1. Non-graduating students will complete a final project due during finals week.
1. [Occasional extra credit assignments](extra_credit/README.md)


<!--
> **NOTE:**
> All of my assignments are explicitly designed to help you get a good job after graduation.
> They will help build your github "portfolio" and give you cool things to talk about during interviews.
> These assignments are all very practical, and not "leetcode".
> For mastering leetcode-style questions, you'll want to take CSCI148: Graph Algorithms with Prof Cannon.
-->

**Late Work Policy:**

You lose `2**i` points on every assignment,
where `i` is the number of days late.
It is usually better to submit a correct assignment late than an incorrect one on time.

**Grade Schedule:**

Your final grade will be computed according to the following standard table,
with the caveats described below.

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

**Caveats:**

There are 2 "caveat tasks" in this course.
These tasks should be easy, and everyone will get full credit on the task just for completing the task.
If you don't complete one of the tasks, however, your grade (from the table above) will be docked 10%.
(For example, an A- grade would become a B- grade.) 
You have the entire semester (until I submit grades) to complete these tasks.

You can find the details about the caveat tasks at:
1. [caveat_tasks/typespeed.md](caveat_tasks/typespeed.md)
1. [caveat_tasks/culture.md](caveat_tasks/culture.md)


<!--
**Weekly Schedule:**

| Day                   | Time              |
| --------------------- | ----------------- |
| Monday / Wednesday    | 08:10AM - 09:25AM |
| Friday                | 11:00AM - 12:05PM |

Friday meetings are "mandatory" in the same sense that Monday/Wednesday meetings are.
That is, you won't lose points for missing class, but we will cover new material.

We have Friday class meetings so that I can take a paternity leave and still cover all the material in the course.

**Paternity Leave:**

Class will be canceled (and I will be unavailable) for approximately 2 weeks after my new baby comes.
The baby is due Feb 25th, but will likely come early.

Therefore, we won't be exactly following the schedule above.
We'll be ahead of schedule before the baby comes,
and behind schedule after the baby comes,
but we should be able to cover everything by the end of the semester.

> **WARNING:**
> We will be running this course about 25% faster than a normal course during the non-paternity leave weeks.
> Therefore, you should anticipate putting in about 25% more work during most weeks.

**Quiz/Midterm/Finals Schedule:**

Unfortunately, I cannot give exact dates yet for quiz/midterm/finals because I do not know exactly when the baby will come.
We will have a midterm "approximately" before spring break,
and a final "approximately" on the second to last week of class.

I promise to be reasonable with giving you sufficient advance notice to prepare for these exams.
-->

<!-- senior grades due May 6 -->
<!-- https://medium.com/analytics-vidhya/python-generators-coroutines-async-io-with-examples-28771b586578 -->

## Academic Integrity

**Technology Policy:**

1. You MUST complete all programming assignments on the lambda server.

1. You MUST use either vim or emacs to complete all programming assignments.
   In particular, you may not use the GitHub text editor, VSCode, IDLE, or PyCharm for any reason.

   In particular: You MAY NOT use the GitHub interface to edit files for a pull request.

1. You MAY NOT share your lambda server credentials with anyone else.

Violations of any of these policies will be treated as academic integrity violations.

**Collaboration Policy**

1. There are no restrictions on what you can post to GitHub Issues.
    In particular, you are highly encouraged to post detailed questions/answers/comments with lots of code.

1. You are highly encouraged to collaborate with students

    1. in class/lab,

    1. in the QCL,

    1. in office hours,
    
    1. and  in computer labs.

1. You MAY NOT look at another student's code (or have another human look at your code) in any other context.

1. You MAY NOT look at another student's code on github.

    All projects are developed as open source projects,
    and so the code is published openly online.
    The benefits of this model include:
    (1) you actually learn how to develop/contribute to open source projects;
    (2) future employers see you have github activity.
    Please do not abuse this privilege.

## Accommodations

I've tried to design the course to be as accessible as possible for people with disabilities.
(We'll talk a bit about how to design accessible software in class too!)
If you need any further accommodations, please ask.

I want you to succeed and I'll make every effort to ensure that you can.

<!--
## Meta

1. CMC's intro programming sequence 

1. This course is designed to get you a good job

1. Second time this course is being offered

    1. I want to add about 50% new material

    1. I'm adding about 25% new material

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
