# Docker

<center>
<a href=https://www.commitstrip.com/en/2016/06/24/how-to-host-a-coder-dinner-party/>
<img src=Strip-Discussion-Docker-english650final-1.jpg />
</a>
</center>

## Lecture

1. MapReduce

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
