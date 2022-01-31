# Docker, docker-compose, the Instagram tech stack

## Announcements

1. In person notes:
    1. you may login over zoom and watch live, but I probably won't be able to interact with you
    1. lectures still recorded/posted to youtube; watching these asynchronously is probably the best way to keep up with class if you miss a lecture for some reason

1. Quiz Wednesday!
    
    Recall:
    1. I will be in RN12 by at least 7:50.
       Quiz is 10 minutes, but you may come early and have extra time.
       I don't want anyone to feel "time pressure."

    1. Open notes, closed computer.

1. As of Monday:
    1. 20/29 students have submitted last week's lab
       
       you still have until Tuesday@midnight with the collaboration extension

    1. 5 students still need to submit the week0 lab, 4 people need to submit the hw

       (people who took data structures with me are excused from the hw but not the lab)

    1. I'll try to give more time for future assignments, but the shortened timeline was needed for this assignment to keep us on track

1. lab update

   lots of problems with the tutorial?
   
   (it was intentional... muahaha...)

   <img src='Strip-Le-déploiement-english650-final.jpg' width=600px />

   good use of github issues to resolve problems!

   the fundamental problem was dependencies improperly specified in the `requirements.txt` file

   fixed version posted in the `flask_web` folder of this repo

1. lab/hw for this week is already posted below
    1. you'll build an instagram clone
    1. this week's assignment is still a "copy+paste" assignment
    1. but it has a lot more sharp edges where things can go wrong
    1. expect to spend ~10x the amount of time on this assignment as last assignment

1. Our goal for the week:
    1. finish docker/everything needed for the lab by Wed
    1. start postgres/sql by Friday (maybe Wed)

## Lecture

1. We're still setting up our "working environment" this week

   <a href=https://dilbert.com/strip/2017-01-02><img width=600px src=dt170102.gif /></a>

    1. the "boring" / "old" technologies are the most useful
        1. [choose boring technology](https://news.ycombinator.com/item?id=20323246)

        1. bash has been with us for 50 years...

            1. that's why the language has all the weird warts
            1. but it's also only getting more popular

        1. other newer technologies come and go
            1. [Pokemon or bigdata?](https://pixelastic.github.io/pokemonorbigdata/)

    1. [types of scaling](http://pudgylogic.blogspot.com/2016/01/horizontal-vs-vertical-scaling.html)

       <img src=horizontal-vs-vertical-scaling-vertical-and-horizontal-scaling-explained-diagram.png width=400px />

       1. horizontal = more computers
       1. vertical = better computers

       1. my hot take:
          1. vertical scaling is almost always what you want... easily solve problems quickly with bash scripts (e.g. Twitter MapReduce)

          1. horizontal scaling can scale almost without limits, but it imposes a 10x factor overhead; so go with vertical if your problem can possibly fit on 1 computer

          1. horizontal scaling often results from "resume driven development" as people try to add more "pokemon technologies" to their resumes that aren't really needed for solving business applications

1. The elements of a standard web service deployment
    1. [12 factor webapp](https://12factor.net/)
        1. one of the most influential guides for high scalability
        1. written at a fairly high level, so sometimes a bit too vague for beginners
    1. [LAMP tech stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29)
        1. services
            1. Linux
            1. Apache
            1. MySQL
                1. MySQL and PostgreSQL are the 2 main databases
                1. MySQL uses threads; Postgres uses processes
                1. MySQL has less overhead, more bugs, lots of data integrity issues, less standards compliant
                1. For most "weby" websites (e.g. Facebook), speed >> data integrity
                1. Postgres has become the "standard" database now because faster machines mean the increased overhead is minimal
            1. PHP
        1. popular in the 1990s, early 2000s
        1. Facebook (used to) run this
            1. [2009 article and slashdot discussion](https://linux.slashdot.org/story/09/04/11/1142246/how-facebook-runs-its-lamp-stack)
            1. still use LAP, but much more complicated database system than MySQL
    1. WIMP tech stack
        1. services
            1. Windows
            1. IIS <- name of Microsoft's web server
            1. MySQL
            1. PHP
        1. No one uses Windows anymore
            1. [Even on Microsoft Azure, over 50% of all servers run Linux](https://www.zdnet.com/article/microsoft-developer-reveals-linux-is-now-more-used-on-azure-than-windows-server/)
            1. The "only" major website that uses Windows is https://stackoverflow.com
            1. Even [bing has dependencies on Linux](https://www.neowin.net/forum/topic/867244-bing-running-on-linux/) and [outlook.com has dependencies on a unix called FreeBSD](https://en.wikipedia.org/wiki/Outlook.com#MSN_Hotmail)
        1. Security vulnerabilities responsible for the entire internet shutting down multiple times in 2001
            1. [Code Red](https://en.wikipedia.org/wiki/Code_Red_(computer_worm))
            1. [Code Red II](https://en.wikipedia.org/wiki/Code_Red_II)
            1. [Nimda](https://en.wikipedia.org/wiki/Nimda)
    1. Instagram's tech stack 
        1. We will closely follow instagram's tech stack
        1. detailed writeup from 2011: https://instagram-engineering.com/what-powers-instagram-hundreds-of-instances-dozens-of-technologies-adf2e22da2ad
            1. 3 nginx ("cute" pronunciation "engine-x")
            1. 25 django
            1. 1 pg\_bouncer
            1. 12 postgres
        1. <img width=100% src=webapp.png />
        1. services
            1. nginx
                1. technically a "reverse proxy" https://www.nginx.com/resources/glossary/reverse-proxy-server/
                    1. load balancer
                    1. manage TCP/IP state
                    1. encrypt/decrypt HTTPS requests
                1. social
                    1. world's #1 web server: https://news.netcraft.com/archives/category/web-server-survey/
                    1. rare Russian company to beat American companies both technically and socially
                    1. recently (2019) raided by Russian police https://news.ycombinator.com/item?id=21771144
            1. The web development framework defines the web page's "application logic"
                1. django
                    1. this is what instagram uses
                    1. the "first" python web framework
                    1. "heavyweight" and "highly opinionated"
                1. flask
                    1. this is what we'll be using
                    1. currently the most popular python web framework
                    1. "lightweight" and "unopinionated"
                        1. easier to get started
                        1. less boilerplate code
                        1. usually faster
                    1. didn't exist when instagram first started
                1. WSGI (pronounced like "whiskey") = Web Server Gateway Interface
                    1. [PEP-3333](https://www.python.org/dev/peps/pep-3333/)
                    1. A standard interfance for python web frameworks
                    1. Ensures that the rest of the tech stack doesn't care which framework you use for you application logic
                    1. Internal to the framework libraries -> doesn't affect application developers
                    1. [ASGI](https://asgi.readthedocs.io/en/latest/introduction.html) = Asynchronous Server Gateway Interface
                        1. replacing WSGI
                        1. Django is both WSGI/ASGI compatible
                        1. Flask is only WSGI
                        1. FastAPI is the "spritual successor" of flask and ASGI compatible
                        1. We'll talk about how ASGI relates to multiprocessing in the non-seniors only portion of the class
            1. [gunicorn webserver](https://gunicorn.org/)
                1. Converts a WSGI application into an actual web service that people can connect to
                1. Handles multiple requests simultaneously and in parallel (using the `fork` syscall)
                1. Much more efficient than flask's built-in webserver
            1. pg_bouncer + postgresql database
                1. Extremely complicated
                1. Most of this class will be focused on the database
                1. Instagram also uses other databases for parts of their website (memcached, redis, solr)
                    1. We'll talk about the differences between postgresql and each of these throughout the course
                1. sqlalchemy python library for interacting with the database from the webapp
        1. more users => consume more resources => slower responses ; increase the numbers of each service above for faster responses
        1. hosted on AWS => "easy" to add more services
        1. does not use docker (it didn't exist)
            1. docker => even easier to add more services
            1. docker makes it easy to transfer from one hosting provider to another
                1. ensures that you can use the cheapest provider
                1. cloud providers can cancel your business contracts for any reason
                    1. parler https://www.nbcnews.com/tech/tech-news/amazon-suspends-hosting-parler-its-servers-citing-violent-content-n1253648
                    1. pirate bay https://www.vice.com/en/article/3an7pn/pirate-bay-founder-thinks-parlers-inability-to-stay-online-is-embarrassing
                    1. sci-hub https://www.reddit.com/r/scihub/comments/fzpjjk/so_why_can_i_still_access_scihub/
            1. without docker, it's difficult to ensure that all instances are running the same code
            1. docker usage is seeing huge adoption right now: https://www.datadoghq.com/docker-adoption/
            1. major companies like netflix use docker: https://netflixtechblog.com/the-evolution-of-container-usage-at-netflix-3abfc096781b
            1. fundamental sys-admin principles you learn working with docker will transfer to whatever deployment solution your future employers use

1. More docker containers

    <a href=https://xkcd.com/1988/><img width=600px src=containers_2x.png /></a>

    1. docker-compose

        1. a convenient "declarative" interface for managing docker commands

           sh/bash/posix-shell is an "imperative" interface


           imperative => specify HOW

           1. adv: more "fine grained" control
           1. adv: universal system
           1. dis: more manual work

           declarative => specify WHAT, the computer figures out HOW

           1. adv: easier to use (fewer sharp edges)
           1. adv: automatically figure out different HOWs depending on the environment (deploying to laptop? lambda server? AWS? Azure?  docker-compose will figure out the details for you)
           1. dis: less control
           1. dis: works only for docker

           other tools (docker swarm/kubernetes) are more powerful declarative systems

           <img src=galaxy-brain.jpg width=400px />

        1. It's a python program.
           First, you need to make sure that your `PATH` is setup to allow `pip` to install programs.
           Run the following commands:
           ```
           $ which pip3
           $ pip3 install pip --upgrade
           $ which pip3
           /home/user/.local/bin/pip3
           ```
           Assuming you get output similar to the above, you can now install the program:
           ```
           $ pip3 install docker-compose
           $ which docker-compose
           /home/user/.local/bin/docker-compose
           ```

        1. important commands
            1. `docker-compose build`: builds the container
            1. `docker-compose up`: start all the services
                1. `-d` in deamon mode
            1. `docker-compose down`: stop all the services (equivalent to `docker stop` and `docker rm`
            1. `docker-compose exec`: run a command on an already running docker container
            1. `docker-compose run`: (probably don't want to use this for this class) brings up a container and runs a 1-off command; useful for admin tasks
            1. `docker-compose logs [container]`: view the logs of `[container]` or all containers if not specified
                1. `-f` follow mode
    1. docker volumes
        1. allow "persistant state" in a docker container
        1. will be critical for databases; for everything else, main use is for debugging
        1. docker-compose will handle all of the (rather complicated) underlying docker commands for us automatically
        1. references:
            1. docker's official docs: https://docs.docker.com/storage/volumes/
            1. good tutorial that also references docker-compose: https://devopsheaven.com/docker/docker-compose/volumes/2018/01/16/volumes-in-docker-compose.html
    1. differences between docker image and docker container
        1. image:
            1. defined by a docker file
            1. blueprint for starting a container
            1. changes to a container never affect the image
        1. container:
            1. defined by the `docker run IMAGE` command, where `IMAGE` is the base image
            1. an actual running "virtual machine"
            1. changes to the container are "locally persistent"
                1. you can stop and restart the container and changes will stay
                1. changes do not affect the base image, or any other containers created from the image
        1. remove stopped containers with the command
           ```
           $ docker-compose rm
           ```
           1. the command
              ```
              $ docker-compose down
              ```
              is a shortcut for the following two commands
              ```
              $ docker-compose stop
              $ docker-compose rm
              ```
           1. if you choose to just run the `stop` command, then you can restart the non-deleted content by running
              ```
              $ docker-compose start
              ```
    1. More Dockerfile 
        1. [overlay filesystems](https://jvns.ca/blog/2019/11/18/how-containers-work--overlayfs/)
        1. [Dockerfile best practices](https://github.com/docker/docker.github.io/blob/master/develop/develop-images/dockerfile_best-practices.md)
        1. [Best simple docker reference](https://towardsdatascience.com/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5)
    1. security issues with docker
        1. credentials and git (see [this post for examples](https://news.ycombinator.com/item?id=25013756).)
        1. [51% of docker images have critical security flaws](https://news.ycombinator.com/item?id=25454207)
        1. [Dependency Confusion: How I hacked Apple, Microsoft, and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
        1. [Typosquatting programming language package managers](https://incolumitas.com/2016/06/08/typosquatting-package-managers/)
        1. [Threat actors targetting docker via container escape feature](https://news.ycombinator.com/item?id=26121877)

1. More networking
    1. We often work with hostnames instead of IP addresses
        1. Hostnames can be defined locally in the file `/etc/hosts`
            1. My hosts file is set to https://github.com/StevenBlack/hosts/blob/master/data/StevenBlack/hosts to block requests to ad/malware servers.
               (This blocks more requests than just an adblock extension for your browser.)
        1. Hostnames can be defined globally using DNS servers
        1. The hostname `localhost` always resolves to the IPv4 address `127.0.0.1`.
    1. Load balancing
    1. [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
        1. 200: success
        1. 404: file not found
        1. 503: internal server error (problem in your python code)
            1. syntax errors cause the server to shutdown and it needs to be restarted

<!--
1. More unix shell
    1. exit codes and the `$?` variable ([optional reference](https://shapeshed.com/unix-exit-codes/))
        1. 0 = success
        1. 1-127 = failure
    1. the commands `true`, `false`, `test`, `[`
    1. if statements
    1. connecting programs with `|`, `&`, `||`, `&&`, `;` ([optional reference](https://unix.stackexchange.com/questions/24684/confusing-use-of-and-operators))
-->

## Lab / Homework

Your lab and homework assignment this week are combined together.
The goal is for you to get a fully working web service using our modified instagram tech stack.
This is a slightly more complicated "hello world" than you did last week that includes (almost) all of the services we'll be using in this class.

1. Create a new github repo called `flask-on-docker`

1. Follow this tutorial to create the necessary files for a simple web app: https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

1. Add all of your tutorial files to the `flask-on-docker` repo except your database credentials.

   > **IMPORTANT:**
   > Many security breaches are caused by developers uploading credentials into public git repositories.
   > See [this post for examples](https://news.ycombinator.com/item?id=25013756).
   > If any of your production credentials are uploaded to github,
   > you will receive a -2 on the assignment.
   > This is not -2 points off your grade, this is a NEGATIVE TWO POINTS TOTAL...
   > committing private credentials to a public repo would cause your company to lose potentially millions of dollars, and so is worse than doing nothing at all.
   > I strongly recommend creating a `.gitignore` file to prevent this from happening on accident.

1. Upload the url of your repo to sakai.

   There are no specific test cases that you need to pass,
   just by uploading the files, you'll get full credit.
   Next week we'll be introducing test cases that combine docker with the github actions continuous integration.

<!--
1. how to change your code:
    1. dev (default) environment:
        1. just change it
        1. docker volumes ensure that the change is instant
    1. production:
        1. to update the contents of your image, run the commands
           ```
           $ docker-compose -f docker-compose.prod.yml down
           $ docker-compose -f docker-compose.prod.yml build
           $ docker-compose -f docker-compose.prod.yml up 
           ```
           takes a little while, but generates a much faster/more secure image
-->

<!--
1. Since we're working on a remote server, you need to enable port forwarding in ssh, and everyone can't be using the same lambda server port

    python3 flask run -p 3400

    ssh -L 8080:localhost:3400

    see: https://www.ssh.com/ssh/tunneling/example

    docker-compose.yml ports needs to change to 3400:5000 instead of 5000:5000

    nginx ports should be 3400:80 NOT 1337:80

1. there are bugs in the `Dockerfile.prod` file; specifically, change the following lines:

    `RUN addgroup -S app && adduser -S app -G app` to `RUN adduser app`
    `RUN chown -R app $APP_HOME` to `RUN chown -R app:app $APP_HOME`

1. Students need to understand the `venv` library: activating, deactivating, deleting

1. What do these files mean in python projects: `requirements.txt`, `__init__.py`; 

    1. why do we specify the version numbers in `requirements.txt`?
    1. the `Dockerfile` for flask contains the command `RUN pip install --upgrade pip`.
       why is this bad?

1. vim copy/paste doesn't work because your clipboard is different from the server's clipboard;
   need to use the terminal's pasting features;
   in vim `:set paste`
   (linux systems have 2 clipboards, the `*` and `+`)

1. docker compose version numbers are wrong in the tutorial; change 3.7 -> 3.3

    EDIT: instead, pip3 install docker-compose

1. sqlalchemy managed vs raw mode

1. for debugging, run `docker-compose up` without the `-d` flag or `docker-compose logs`

1. psql commands `\l`, `\c`, `\dt`, `\q`

1. `docker volume inspect flask-on-docker_postgres_data` command shouldn't have the `-`s

1. must understand: `netcat -z` = `nc -z`

1. instructions never use the `docker-compose down` command

1. the volumes in the docker-compose.yml file lets us modify the source code locally without rebuilding the docker images

1. postgres docker container must have usernames/passwords specified

1. docker multistage builds
-->
