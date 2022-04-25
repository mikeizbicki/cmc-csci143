# Wrapup

Done with material for the final exam

Today: Review

Wednesday: Ask questions

Next week: last homework for non-seniors

## Main ideas

1. DevOps

    1. Use linux:
        1. Even Microsoft uses more Linux than Windows

           <https://www.zdnet.com/article/microsoft-developer-reveals-linux-is-now-more-used-on-azure-than-windows-server/>

        1. <img src=y9nmw0smgxd61.png width=400px/>

    1. Use containers:
        1. Why?
            1. Infrastructure in a config file
            1. Simplify/automate the deployment of other techs
            1. Use locally or on the cloud with the same techniques
            1. A generic interface to cloud providers, so no vender lock in

               <img src=images.jpeg />

               (most venders MUCH cheaper than AWS)
        1. We used: docker + docker-compose
        1. Other technologies
            1. Kubernetes (abbreviated K8s):
                1. automatically start/stop services based on current system load
                1. even easier deployment to cloud providers
                1. this is for real "google scale"
            1. not many other (popular) options
            1. containers are easy to do "from scratch": <https://www.redhat.com/sysadmin/building-container-namespaces>

    1. Use:
        1. a good text editor (e.g. vim)
        1. version control (e.g. git)
        1. good test cases, continuous integration (e.g. github actions)
           1. big datasets make it harder
           1. create smaller datasets and test on those

           <img src=Strips-Test-audimetre-600-finalenglish.jpg width=400px />

    1. Takeaway: devops is a hard, thankless, but necessary task

        See: [Issue #184](https://github.com/mikeizbicki/cmc-csci143/issues/184)

        <img src=r_387549_W7fYM.jpg width=400px>

1. MapReduce: the main workhorse of "big data" data analysis

    1. Used for 1-off tasks
        1. easier to setup than a database
        1. slower for repeating similar work

    1. We used: plain old bash scripts (vertical scaling)
        1. easy to implement: no need to setup many servers/docker containers
        1. suitable for >1 TB datasets
        1. basic ideas the same no matter the underlying tech

    1. Other technologies (horizontal scaling):
        1. Twitter SummingBird
        1. Apache Hadoop
        1. Apache Hive
        1. Apache Spark (a little more general than just MapReduce)

    1. Don't use the other techs until you're into the >1 PB range
        1. bash scripts have LOTs of applications
           1. so getting good at scripting will make you good at lots of tasks
           1. getting good at Hadoop/etc will only make you good at MapReduce tasks

        1. pain to set up
        
           <img src=hadoop_meme.jpg />

1. Database: the main workhorse of storing "bigish data"

    1. Unless you have a good reason not to, use a database

       <img src=database-overloads.jpg />

       Really big data (e.g. common crawl/internet archive) stored in custom formats

    1. We used: PostgreSQL

        1. Correctness matters, and postgresql's #1 priority is correctness.

           If you insert data, it will be there.

           [The Guardian newspaper switched from MongoDB to Postgres because Mongo randomly lost some archived news articles](https://www.theguardian.com/info/2018/nov/30/bye-bye-mongo-hello-postgres).

           Speed matters too, and postgres is *nearly* as fast as other systems.

        1. World's "most advanced open source database"
            1. New features constantly being added
            1. More compliance with SQL standard than all other RDBMs
            1. Scales to multipetabyte datasets

        1. Extremely popular in industry: 
            1. [Ask HN: Who's Hiring (March 2022)](https://news.ycombinator.com/item?id=30515750) - 31 ads mention postgres
            1. [stackshare.io/postgres](https://stackshare.io/postgresql)

                > **HINT:**
                > When interviewing at a company, visit their stackshare.io webpage to learn what technologies they use.
                > Then, you can have intelligent conversations with the interviewers about their tech.
                > See, for example, <https://stackshare.io/companies/instagram>.

            1. Postgres is good enough for Instagram... and you're (probably) not going to ever have "bigger data" than Instagram
            1. Even Microsoft uses Postgres (instead of SQL Server) when they need to processes multi-petabyte datasets

               <https://techcommunity.microsoft.com/t5/azure-database-for-postgresql/architecting-petabyte-scale-analytics-by-scaling-out-postgres-on/ba-p/969685>

        1. Normalization is a spectrum
        
           Exactly how normalized your database should be is a tricky technical decision with lots of tradeoffs

           | Normalized data | Denormalized data |
           | --------------- | ----------------- |
           | hard to insert  | easy to insert    |
           | less disk space | more disk space   |
           | easy to select  | hard to select    |
           | lots of joins   | few/no joins      |

           Heuristic:
           
           1. if you "own" the data, then prefer normalized

           1. if someone else "owns" the data, then prefer denormalized

        1. Use indexes
            1. Make SELECT much faster

               Lack of proper indexes brought down the company Auth0: <https://www.reddit.com/r/SQL/comments/n1z3o7/a_hardwon_lesson_in_indexing/>

            1. Make INSERT slightly slower

            1. Many types of indexes
                1. We covered: BTree, Hash, GIN, RUM
                    1. Takeaways:
                        1. Full text search, JSON, Arrays: use GIN/RUM
                        1. Everything else: BTree
                        1. Don't use Hash
                1. Did not cover: BRIN, GIST, SP-GIST
                1. Other DBs have different names for these indexes,

                   and minor implementation details change,

                   but there's really no other major categories of indexes

            1. General procedure:
                1. First design your SELECT statements to be correct
                1. Then, create indexes that make them fast
                1. (Rarely) re-write your SELECT statement to use indexes better
                    1. Remove set-returning functions
                    1. Adding LIMIT clauses
                    1. Lots of other tricks we didn't get into
                        1. <https://www.cybertec-postgresql.com/en/avoid-or-for-better-performance/>
                        1. <https://towardsdatascience.com/how-we-optimized-postgresql-queries-100x-ff52555eabe>

                        > **Note:**
                        > Our class didn't go over all of these tricks, and there's too many for any class to cover.
                        > What separates the good from the great devs is that the great devs actively study these tricks on their own.

    1. Other technologies
        1. Other RDBMS: MySQL, Microsoft SQL Server, Oracle, etc.
        1. NoSQL
            1. JSON/denormalized representations: MongoDB
                1. became popular around 2010 due to scalability and JSON ease-of-use
                1. but data inserted into db not guaranteed to actually be inserted (not ACID)
                1. postgres safety guarantees can be turned off to get this scalability (but don't do this!)
                1. today, postgres supports (basically) everything MongoDB does and more
            1. Full text search: Elastic, Lucene, Solr, Groonga
                1. there's a LOT more to FTS than what we covered...
                1. My prediction: Postgres will be state-of-the-art within 10 years
            1. Cache: Memcache, Redis
        1. Many other types of database technologies too

        <img src=junior-dev-postgres-intermediate-de-postgres-redis-mongodb-senior-dev-36100154.png />

1. Notice:
    1. all these techs are open source
    1. the technology is not what differentiates companies
    1. it's the data / how the tech is deployed

1. Don't do these things:
    1. Use MapReduce when a database is more appropriate, and vice-versa
        1. MapReduce: 1-off analysis tasks that can take a long time, no setup overhead
        1. Database: many related tasks with real time responses, lots of setup overhead

    1. Upload production credentials to github

    1. Run `DELETE`/`UPDATE`/`DROP` SQL commands outside of a transaction

       <img src=ri96s0xu1ryz.jpg width=400px/>

Academic vs. Industry big data

1. We focused on industry in this class

1. Academic big data is much more math heavy, less implementation
    1. "monoid homomorphisms" needed for MapReduce
    1. probabilistic data structures like [HyperLogLog](https://github.com/citusdata/postgresql-hll/)
    1. [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)

<!--
1. Open research problems:
    1. Non-English FTS
    1. Better web scraping for dynamic pages
    1. Efficiently updating materialized views
-->

Where to go from here?

1. Learn more technologies?
    1. No.
    1. At least, don't learn them just for the sake of putting them on a resume
    1. There's too many
    1. Big data or pokemon? <https://pixelastic.github.io/pokemonorbigdata/>

1. Just build something

    1. You can build 99% of webpages/data analysis tools with the docker/nginx/gunicorn/flask/pgbouncer/postgres tech stack
    1. If there's something else you need, learn it as you need it
    1. Much better to be an expert in a small number of techs than a novice in lots of tech

       (especially for a junior dev)

    1. Also much better to actually build a product that people can use/see

       <img src=r_538889_6FyHg.jpg />

1. Do things that will make you more productive on future projects

    1. more bash
    1. more postgres / sql
    1. more vim ;)

**If there's ever anything I can do to help you in the future, please reach out.**

## Grade Reminders

1. Your grades are up-to-date in sakai

1. 2 caveat tasks
    1. Failure to complete will result in the loss of a letter grade
    1. Graduating students must have these complete by Monday

1. State-of-the-industry videos ([Issue #170](https://github.com/mikeizbicki/cmc-csci143/issues/170))

## Final

1. I will post Friday morning, you will have until Monday midnight

1. 120 points

   (currently about 240 points in the class => 33% of grade)

1. Format:

    1. Take home, same rules as midterm:
        1. Open notes/internet/anything written before the begining of the exam
        1. Open postgres/lambda server
        1. No communication with another human

    1. Nothing on blocks/locks/deadlocks
   
    1. 60 points: True/False questions

        You have LOTS of sample questions from the handouts

        Half of questions will cover material we directly covered in lecture, half you'll have to look up in references

    1. 60 points: Free response 

        Similar to the take home indexes quiz

<!--
    1. Probably going to be hard (based on the scores for these homeworks)
-->

## Course evals

Please complete the course evals :)

<!--
1. google forms eval: https://docs.google.com/forms/d/1Fw-jDmq6B2eiSNGMqA6MGSFsWT4iOEuS4SyYpN-6agY

I read all the answers, and will use the feedback to help make future versions of this course better
-->
