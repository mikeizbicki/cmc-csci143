# CSCI143: Big Data

<center>
<img width='100%' src=img/bigdata-knows-everything.jpg />
</center>

## About the Instructor

See <https://github.com/mikeizbicki/about-me>

You should contact me through the [class github issues](https://github.com/mikeizbicki/cmc-csci143/issues).

You may send questions about grades to my email at <mizbicki@cmc.edu>.

View my office hours at this link https://github.com/mikeizbicki/about-me/issues/1 

## About the Course

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

            <img width=400px src=img/pandas1.jpg />

            <br/>

            <img width=400px src=img/anakin-padme-pandas-large-dataframe-meme.jpg />

    1. all the interesting/applied parts of upper division computer science compressed into a single course
        1. shell scripting
        1. mapreduce
        1. git
        1. continuous integration / test driven development
        1. docker / docker-compose
        1. (**50% of course**) SQL using sqlite3 / postgres
        1. Instagram tech stack
        1. large language models (LLMs)

<hr>

<img src=https://raw.githubusercontent.com/mikeizbicki/cmc-advising/master/courses-map.png width=100% />

<br/>

We will do all our work on the lambda server.

<center>
<img width='500px' src=img/big-data-map.png />
</center>

The lambda server has:
1. 80 processors
1. 8 GPU
1. 256 GB RAM
1. 2 TB NVME
1. 50 TB RAID array of 16 HDDs

<br/>

<img src=https://raw.githubusercontent.com/mikeizbicki/cmc-advising/master/iceberg/iceberg.png width=100% />

**Out of scope:**

1. concepts from CSCI133 databases
    1. relational algebra
    1. technical implementation details / C programming

1. other programming concepts
    1. frameworks for distributed computation (e.g. Apache Hadoop, Apache Spark)
    1. distributed Filesystems (e.g. HDFS, IPFS, S3)
    1. geo-distributed databases

**Textbook:**

<img src=img/free.jpg width=400px />

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

| Assignment Type | Points | Approximate Percentage |
| --------------- | ------ | ---------------------- |
| weekly labs     | `2**1` or `2**2` or `2**3` | 20% |
| weekly projects | `2**2` or `2**3` or `2**4` | 30% |
| weekly quizzes  | `2**2` or `2**3` or `2**4` | 30% |
| oral final exam | `2**6`                     | 20% |

All assignments are designed to help you get a good job:
1. All code, no math.
1. You will build your github portfolio.
1. You will do cool stuff to talk about in interviews (analyze ALL tweets about covid, build an Instagram clone).
1. The assignments will help you with SQL technical interview questions.

See <https://github.com/mikeizbicki/cmc-csci143/issues/577> for extra credit opportunities.

**Late Work Policy:**

You lose `2**(i-1)` points on every assignment,
where `i` is the number of days late.

> **Example:**
> Homeworks will be due on Tuesdays, so if you submit on Wednesday then `i=1` and you receive a `2**(1-1)` (i.e. `1`) point penalty.
> If you submit on Friday, you receive a `2**(3-1)` (i.e. 4) point penalty.

Do not expect partial credit for incomplete assignments.

It is much better to submit a correct assignment late than an incorrect one on time.

I expect that most students will submit late assignments at some point.

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

**Technology Policy**

The purpose of this policy is to encourage you to learn how to use AI and other technology effectively.

1. You MAY ONLY use AI tools that we discuss in class using APIs.

    In particular, you MAY NOT use:
    1. web interfaces (e.g. <https://chatgpt.com>, <https://claude.ai>)
    2. subscription-based services (e.g. Claude Code, Codex, CoPilot)

    We will build similarly powerful tools in class from the ground up.

1. You MUST complete all programming assignments on the lambda server.

1. You MUST edit all text in the command line (for example, using vim).

    In particular, you MAY NOT use the GitHub text editor, VSCode, or jupyter notebooks.

1. You MAY NOT share any account credentials with anyone else.

**Collaboration Policy**

The purpose of this policy is to encourage you all to work together like professional programmers work together.

1. You MAY post anything at all to github issues without restriction.

    In particular, you are encouraged to post detailed questions/answers/comments with lots of code. Particularly good posts will be awarded extra credit.

1. You MAY ONLY collaborate with other humans:

    1. in class/lab/office hours,

    1. in the QCL.

    You MAY NOT collaborate with humans in any other context.

1. When collaborating:

    1. You MAY look at another student's code to help them or get high level guidance.

    1. You MAY NOT copy another student's code.

    1. You MUST be the only human to type in code for your assignments.

1. You MAY NOT look at another student's code on github.

    All projects are developed as open source projects, and so the code is published openly online.  The benefits of this model include: (1) you actually learn how to develop/contribute to open source projects; (2) future employers see you have github activity. Please do not abuse this privilege.

## Accommodations

I've tried to design the course to be as accessible as possible for people with disabilities.
(We'll talk a bit about how to design accessible software in class too!)

If you need any further accommodations, please ask.

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
