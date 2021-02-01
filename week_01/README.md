# Docker

<center>
<a href=https://www.commitstrip.com/en/2016/06/24/how-to-host-a-coder-dinner-party/>
<img src=Strip-Discussion-Docker-english650final-1.jpg />
</a>
</center>

## Lecture

1. Parallel programming
    1. All of the hardest parts of an OS course compressed down into 5 minutes
    1. Two techniques: Threads vs Processes
        1. Threads are "lightweight"
            1. minimal overhead
            1. each thread shares the same memory, so communication is easy
            1. slighly less safe because a bug in one thread will cause bad behavior in every program
            1. Python's [global interpretter lock (GIL)](https://realpython.com/python-gil/) means you cannot use threads in python for parallel programming
        1. Processes are "heavyweight"
            1. about 10MB of unavoidable overhead per process in the system kernel
            1. additionally, each child process duplicates the memory of its parent process
            1. processes can communicate only by reading/writing to files
            1. processes are the only way to do parallel programming in python
            1. processes created by "forking"
                1. `os.fork()`
                1. [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) built-in library
    1. Programming with threads/processes is HARD
        1. easy to create "memory leaks"
        1. easy to accidentally create [fork bombs](https://en.wikipedia.org/wiki/Fork_bomb), which were the original form of [cracking](http://www.catb.org/jargon/html/C/cracker.html)
        1. code is non-deterministic (everytime you run it, you get different results), resulting in lots of [heisenbugs](https://en.wikipedia.org/wiki/Heisenbug)
            1. simple example: [I can't login standing up](https://www.reddit.com/r/talesfromtechsupport/comments/3v52pw/i_cant_log_in_when_i_stand_up/)
            1. complicated example: [I can't send email more than 500 miles](http://www.ibiblio.org/harris/500milemail.html)
        1. python is not great for manipulating processes (it's very easy to create very bad bugs); bash is much better; so I always do the parallel programming parts in bash
        1. MapReduce paradigm simplifies parallel data analysis

1. Docker containers

1. Basic networking
    1. IP addresses
    1. port numbers
    1. port forwarding ([optional reference](https://www.ssh.com/ssh/tunneling/example))

1. Flask webpages

**Pre-lecture work:**

Watch the following videos:

1. [Virtual Machines vs Docker Containers](https://www.youtube.com/watch?v=TvnZTi_gaNc)

1. (optional) [Docker vs Kubernetes vs Docker Swarm](https://www.youtube.com/watch?v=9_s3h_GVzZc)

1. (optional) [MapReduce - Computerphile](https://www.youtube.com/watch?v=cvhKoniK5Uo)

1. (optional) [Apache Spark - Computerphile](https://www.youtube.com/watch?v=cvhKoniK5Uo)

<!--
1. (optional) https://dwheeler.com/essays/fixing-unix-linux-filenames.html
-->

## Lab

This is a "hello world" assignment for flask/docker that just ensures you have a sane working environment.

<!--
1. Connect to the webpage
-->

1. Follow the instructions for installing rootless docker: https://docs.docker.com/engine/security/rootless/#install

1. Follow these instructions to create a simple flask app running in a docker container: https://runnable.com/docker/python/dockerize-your-flask-application

    These instructions were not designed specifically with this class in mind, and thus you will have to modify parts of the instructions in order to get them to work.
    This is intentional in order to get you more practice adapting tutorials into different computational environments.
    There are two main modifications you'll have to make:

    1. In the `docker run` command, you will have to change the port that docker exposes to a port other than 5000.
       (This is because you're all running this code at the same time, and you can't all use the same port.)
       I recommend using your user id as a port number, as this will guarantee that you don't run into conflicts with other students.
       Your userid is stored in the environment variable `$UID`.

    1. In order to view your webpage from your laptop,
       you will have to connect to the lambda server with local port forwarding enabled.
       The command will look something like
       ```
       $ ssh username@134.173.191.241 -p 5055 -L 8080:localhost:DOCKER_PORT
       ```
       where `DOCKER_PORT` is whatever port you specified.

## Homework

You should start the [twitter MapReduce](../hw_twitter) homework.
Because this homework can potentially take a very long time to run,
this homework has a modified due date schedule.
