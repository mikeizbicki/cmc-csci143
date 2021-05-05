# Wrapup

## Main ideas

1. DevOps
    1. Use linux:
        1. Even Microsoft uses more Linux than Windows

           https://www.zdnet.com/article/microsoft-developer-reveals-linux-is-now-more-used-on-azure-than-windows-server/

        1. <img src=y9nmw0smgxd61.png width=400px/>
    1. Use containers:
        1. Why?
            1. Infrastructure in a config file
            1. Simplify/automate the deployment of other techs
            1. Use locally or on the cloud with the same techniques
            1. A generic interface to cloud providers, so no vender lock in

               <img src=images.jpeg />
        1. We used: docker + docker-compose
        1. Other technologies
            1. Kubernetes:
                1. automatically start/stop services based on current system load
                1. even easier deployment to cloud providers
            1. not many other options
    1. Use:
        1. a good text editor (e.g. vim)
        1. version control (e.g. git)
        1. good test cases, continuous integration whenever possible (e.g. github actions)
           1. big datasets make it harder
           1. create smaller datasets and test on those

           <img src=Strips-Test-audimetre-600-finalenglish.jpg width=500px />
    1. Takeaway: devops is a hard, thankless task

       <img src=r_387549_W7fYM.jpg width=500px>

1. MapReduce

    1. Used for 1-off tasks
        1. easier to setup than a database
        1. slower for repeating similar work
    1. We used: plain old bash scripts
        1. easy to implement: no need to setup many servers/docker containers
        1. suitable for >1 TB datasets
        1. basic ideas the same no matter the underlying tech
    1. Other technologies:
        1. Twitter SummingBird
        1. Apache Hadoop
        1. Apache Hive
        1. Apache Spark (a little more general than just MapReduce)
    1. Don't use the other techs until you're into the >100s of TB range
        1. bash scripts have LOTs of applications
           1. so getting good at scripting will make you good at lots of tasks
           1. getting good at Hadoop will only make you good at MapReduce tasks

        1. too much setup overhead
        
           <img src=hadoop_meme.jpg />

1. Database

    1. Used for repeated tasks

       Basically, use for everything

       <img src=database-overloads.jpg />
    1. We used: PostgreSQL
        1. Correctness matters, and postgresql's #1 priority is correctness.

           If you insert data, it will be there.

           Speed matters too, and postgres is *nearly* as fast as other systems.
        1. World's "most advanced open source database"
            1. New features constantly being added
            1. More compliance with SQL standard than all other RDBMs
            1. Scales to multipetabyte datasets
        1. Extremely popular in industry: https://news.ycombinator.com/item?id=27025922
            1. Good enough for Instagram... and you're (probably) not going to have "bigger data" than Instagram
            1. Even Microsoft uses Postgres when they need to processes multi-petabyte datasets

               https://techcommunity.microsoft.com/t5/azure-database-for-postgresql/architecting-petabyte-scale-analytics-by-scaling-out-postgres-on/ba-p/969685
        1. | Normalized data | Denormalized data |
           | --------------- | ----------------- |
           | hard to insert  | easy to insert    |
           | less disk space | more disk space   |
           | easy to select  | hard to select    |

           Normalization is a spectrum

        1. Use indexes
            1. Make SELECT much faster

               Lack of indexes brought down Auth0: https://www.reddit.com/r/SQL/comments/n1z3o7/a_hardwon_lesson_in_indexing/
            1. Make INSERT slightly slower
            1. Many types of indexes
                1. We covered: BTree, Hash, GIN, RUM
                    1. Takeaways:
                        1. Full text search: use GIN/RUM
                        1. Everything else: BTree
                        1. Don't use Hash
                1. Did not cover: BRIN, GIST, SP-GIST
                1. Other DBs have different names for these indexes,

                   and minor implementation details change,

                   there's really no other major categories of indexes
            1. General procedure:
                1. First design your SELECT statements to be correct
                1. Then, create indexes that make them fast
    1. Other technologies
        1. Other RDBMS: MySQL, Microsoft SQL Server, Oracle, etc.
        1. NoSQL
            1. JSON/denormalized representations: MongoDB, Cassandra
                1. more scalable
                1. but data inserted into db not guaranteed to actually be inserted (not ACID)
            1. Full text search: Elastic, Lucene, Solr, Groonga
            1. Cache: Memcache, Redis
        1. Many other types of database technologies too

        <img src=junior-dev-postgres-intermediate-de-postgres-redis-mongodb-senior-dev-36100154.png />

    1. Don't do these things:
        1. Use MapReduce when a database is more appropriate
           (almost always)

        1. Run `DELETE`/`UPDATE`/`DROP` SQL commands outside of a transaction

           <img src=ri96s0xu1ryz.jpg width=400px/>

1. Notice:
    1. all these techs are open source
    1. the technology is not what differentiates companies
    1. it's the data / how the tech is deployed

Academic vs. Industry big data
1. We focused on industry in this class
1. Academic big data is much more math heavy, less implementation
    1. "monoid homomorphisms" needed for MapReduce
    1. probabilistic data structures like HyperLogLog
1. Open research problems:
    1. Non-English FTS
    1. Better web scraping for dynamic pages
    1. Efficiently updating materialized views

Where to go from here?
1. Learn more technologies?
    1. No.
    1. At least, don't learn them just for the sake of putting them on a resume
    1. There's too many
    1. Big data or pokemon? https://pixelastic.github.io/pokemonorbigdata/
1. Just build something
    1. You can build 99% of webpages/data analysis tools with docker/nginx/gunicorn/flask/pgbouncer/postgres tech stack
    1. If there's something else you need, learn it as you need it
    1. Much better to be an expert in a small number of techs than a novice in lots of tech

       (especially for a junior dev)

    1. Also much better to actually build a product that people can use/see

       <img src=r_538889_6FyHg.jpg />

1. If you insist on learning without projects,

   do things that will make you more productive on future projects
    1. try kubernetes
    1. more bash
    1. more SQL
    1. more vim ;)

**If there's ever anything I can do to help you in the future, please reach out.**

1. advice on how to implement a project
1. get involved with research
1. etc.

## Final

1. 40 points

   (currently about 200 points in the class => 20% of grade)

1. Problems will be very similar to the (written) homeworks, especially week09+10
   
   probably going to be hard (based on the scores for these homeworks)

1. Extra credit

   Watch a video below, write a 5 things that you learned

    1. [Scaling Instagram Infrastructure](https://www.youtube.com/watch?v=hnpzNAPiC0E)

    1. [The Evolution of Reddit.com's Architecture](The Evolution of Reddit.com's Architecture)

    1. [PostgreSQL at 20TB and Beyond: Analytics at a Massive Scale (AdTech use of postgres)](https://www.youtube.com/watch?v=BgcJnurVFag&t=1650s)

    1. [Large Databases, Lots of Servers, on Premises, in the Cloud - Get Them All! (AdTech use of postgres)](https://www.youtube.com/watch?v=4GB7EDxGr_c)

    1. [Breaking Postgres at Scale (how to configure postgres for scaling from 1GB up to many TB)](https://www.youtube.com/watch?v=eZhSUXxfEu0)
