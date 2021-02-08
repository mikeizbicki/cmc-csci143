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

1. Basic networking
    1. Internet Protocol (IP) addresses
        1. (Almost) every device on the internet has a unique IPv4 address.  IPv4 uses 32bit addresses (looks like 134.173.191.241), which supports up to 4 billion unique addresses.
        1. The internet is slowly moving to the IPv6 standard.  IPv6 uses 64bit addresses (looks like `fe80::3efd:feff:fedd:feec`).
        1. The IPv4 address `127.0.0.1` is called a "loopback" address because it always refers to the computer you are working on.
    1. TCP port numbers
        1. ports are numbers between 1 and 2^16-1 (65535)
        1. different services listen on different ports
        1. the standard ports are:
            1. ssh is 22
            1. http is port 80
            1. https is port 443
        1. notice that the lambda server is running ssh on a non-standard port, and that is why you must specify the `-p` flag when connecting
        1. only root can listen on ports < 1024; therefore, you cannot use the standard ports for your web services running on the lambda server
    1. port forwarding lets you redirect connections from one computer to another ([optional reference](https://www.ssh.com/ssh/tunneling/example))

1. Docker containers
    1. `docker ps`: lists currently running containers
    1. `docker run`: creates and runs a new container
        1. `--name`: provide a name for the container that will be displayed with the `docker ps` command
        1. `-it`: use this flag whenever you are running an interactive command (such as `bash`); the `i` stands for interactive and the `t` stands for tty
        1. `--rm`: delete the container after running, useful for preserving disk space
        1. `-p X:Y`: expose port `Y` in the docker image to lambda server port `X`
        1. `-d` run as a daemon
    1. `docker logs`: shows the output of a container started with the `-d` flag
        1. `-f`: follow mode
    1. `docker stop`: stop a container started with the `-d` flag
    1. `docker rm`: delete a stopped container that was not created with the `--rm` flag
    1. `docker exec`: runs a command in a container without creating a new container
        1. `-it`: same as for `run`
    1. `docker build`: creates a new "container image"
        1. `-t`: name the image
    1. `Dockerfile`: the instructions for creating a new image

1. More unix shell
    1. for loops
    1. glob (`*`)
    1. file permissions ([optional reference](https://linuxhandbook.com/linux-file-permissions/))
    1. `PATH` environment variable

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

1. First, we'll practice using ssh port forwarding.
   A sample of the final search engine you'll be creating in this class is currently running on the lambda server's port 5000.
   For this task, you will log on to the lambda server with "local port forwarding" in order to get access to this webpage.

   1. **Mac/linux**: log on to the lambda server with the following command
      (changing `username` to your username):
      ```
      $ ssh username@134.173.191.241 -p 5055 -L 8080:localhost:5000
      ```
      This tells ssh to forward all requests to port 8080 on your computer (`localhost`) to port 5000 on the lambda server.

      **Windows**:
      You will have to select the appropriate checkboxes in putty to get local port forwarding enabled.
      You can follow [these instructions](https://blog.devolutions.net/2017/4/how-to-configure-an-ssh-tunnel-on-putty) to get pictures of where the checkboxes are located.

   1. After you've logged on to the lambda server, visit the url
      https://localhost:8080
      in your web browser (I use firefox with the uBlock origin extension for all my internet browsing).
      You should now have access to the search engine.

1. Install rootless docker

    1. The instructions are here: https://docs.docker.com/engine/security/rootless/#install

    1. Ensure that you:
        1. move the contents of the `bin` folder into `.local/bin`
        1. add the `DOCKER_HOST` environment variable to your `.bashrc` file
    
    1. Whenever the lambda server restarts, you must run the command
       ```
       $ systemctl --user start docker
       ```
       to restart the docker daemon.

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
    
    Finally, the python file in the webpage has a few python syntax errors that you'll have to fix.


1. After completing the steps above, upload the sentence `I've completed the lab` to sakai to get credit for the lab.

## Homework

You should start the [twitter MapReduce](../hw_twitter) homework.
Because this homework can potentially take a very long time to run,
this homework has a modified due date schedule.
