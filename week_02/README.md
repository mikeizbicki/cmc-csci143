# Docker, docker-compose, the Instagram tech stack

<center>
<a href=https://dilbert.com/strip/2017-01-02><img width=80% src=dt170102.gif /></a>

<br/>
<br/>
<a href=https://xkcd.com/1988/><img width=70% src=containers_2x.png /></a>
</center>

## Lecture

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
            1. 3 nginx
            1. 25 django
            1. 1 pg\_bouncer
            1. 12 postgres
        1. <img width=100% src=webapp.png />
        1. services
            1. nginx
                1. load balancer
                1. manage TCP/IP state
                1. encrypt/decrypt HTTPS requests
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
                1. WSGI (pronounced like "whiskey")
                    1. A standard interfance for python web frameworks
                    1. Ensures that the rest of the tech stack doesn't care which framework you use for you application logic
                    1. Internal to the framework libraries -> doesn't affect application developers
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
            1. without docker, it's difficult to ensure that all instances are running the same code
            1. docker usage is seeing huge adoption right now: https://www.datadoghq.com/docker-adoption/
            1. major companies like netflix use docker: https://netflixtechblog.com/the-evolution-of-container-usage-at-netflix-3abfc096781b
            1. fundamental sys-admin principles you learn working with docker will transfer to whatever deployment solution your future employers use
            1. <img src=galaxy-brain.jpg width=50% />

1. More docker containers
    1. docker-compose
        1. get it by running
           ```
           $ which pip3
           $ pip3 install pip --upgrade
           $ which pip3
           $ pip3 install docker-compose
           ```
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
        1. to start the containers in daemon mode, but still view the logs, use
           ```
           $ docker-compose up -d
           $ docker-compose logs [-f] [container]
           ```
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
    1. More Dockerfile 
        1. [overlay filesystems](https://jvns.ca/blog/2019/11/18/how-containers-work--overlayfs/)
        1. [Dockerfile best practices](https://github.com/docker/docker.github.io/blob/master/develop/develop-images/dockerfile_best-practices.md)
        1. [Best simple docker reference](https://towardsdatascience.com/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5)
    1. security issues with docker
        1. credentials and git (see [this post for examples](https://news.ycombinator.com/item?id=25013756).)
        1. [51% of docker images have critical security flaws](https://news.ycombinator.com/item?id=25454207)
        1. [Dependency Confusion: How I hacked Apple, Microsoft, and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
        1. [Typosquatting programming language package managers](https://incolumitas.com/2016/06/08/typosquatting-package-managers/)

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

<img src='Strip-Le-déploiement-english650-final.jpg' width=60% />

Your lab and homework assignment this week are combined together.
The goal is for you to get a fully working web service using our modified instagram tech stack.
This is a slightly more complicated "hello world" than you did last week that includes (almost) all of the services we'll be using in this class.

1. Create a new git repo called `flask-on-docker`

1. Follow this tutorial to create the necessary files for a simple web app: https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

1. Add all of your tutorial files to the `flask-on-docker` repo except your database credentials.

   **IMPORTANT:**
   Many security breaches are caused by developers uploading credentials into public git repositories.
   See [this post for examples](https://news.ycombinator.com/item?id=25013756).
   If any of your production credentials are uploaded to github,
   you will receive a -2 on the assignment.
   This is not -2 points off your grade, this is a NEGATIVE TWO POINTS TOTAL...
   committing private credentials to a public repo would cause your company to lose potentially millions of dollars, and so is worse than doing nothing at all.
   I strongly recommend creating a `.gitignore` file to prevent this from happening on accident.

1. Upload the url of your repo to sakai.

   There are no specific test cases that you need to pass,
   just by uploading the files, you'll get full credit.
   Next week we'll be introducing test cases that combine docker with the github actions continuous integration.


