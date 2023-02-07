# Docker Intro

<img src=containers_2x.png width=400px />

## Docker

**Pre-lecture work:**

1. (optional) Watch the following videos:

    1. [What is GNU+Linux](https://www.youtube.com/watch?v=kb2T8hWRu8g) by RMS

    1. [Virtual Machines vs Docker Containers](https://www.youtube.com/watch?v=TvnZTi_gaNc)

    1. [Docker vs Kubernetes vs Docker Swarm](https://www.youtube.com/watch?v=9_s3h_GVzZc)

    1. [MapReduce - Computerphile](https://www.youtube.com/watch?v=cvhKoniK5Uo)

    <!--
    1. (optional) [Apache Spark - Computerphile](https://www.youtube.com/watch?v=cvhKoniK5Uo)
    -->

**Lecture:**

1. Overview

    1. Docker used basically everywhere

       <https://stackshare.io/docker>

       <img src=docker-docker-everywhere.jpg width=400px />

    1. Why?
       
       1. Different computers have different versions of libraries
       1. So code that works on 1 computer won't necessarily work on another computer
       1. Docker containers let you deploy your code along with all the dependencies
       1. So if it works on any machine, it works on every machine

           <br/>
           <br/>
           <img src=works-on-my-machine2.jpeg width=400px />
           <br/>
           <br/>

           <img src=works-on-my-machine.jpeg width=400px />

    1. Hard to learn
        1. Lots of different concepts that all work together

        1. You can't fully understand any concept until you understand all the concepts

           In this way it's like git/github... but on steroids

        1. It's okay if you don't 100% understand all of today's lecture;
           
           the next few lectures will build on this material, reviewing it and filling in gaps

        1. you have to use it to fully understand it... so labs/hws will be super important

1. References:
    1. https://www.docker.com/resources/what-container

       Helps you understand the following jokes:

       <img src=docker-vm.png width=400px />

       <br/>
       <a href=https://www.commitstrip.com/en/2016/06/24/how-to-host-a-coder-dinner-party/>
       <img src=Strip-Discussion-Docker-english650final-1.jpg width=400px />
       </a>

    1. https://docs.docker.com/get-started/overview/

       Helps you actually understand the commands below

1. Installing "rootless docker"

    1. Instructions: <https://docs.docker.com/engine/security/rootless/#install>

    <!--
    1. Ensure that you:
        1. move the contents of the `bin` folder into `.local/bin`
        1. add the `DOCKER_HOST` environment variable to your `.bashrc` file
    
    1. Whenever the lambda server restarts, you must run the command
       ```
       $ systemctl --user start docker
       ```
       to restart the docker daemon.
    -->

1. Basic Commands

    1. `docker pull`: download a docker image

        important images include:

        1. `ubuntu`: a basic install of the ubuntu distro
        1. `debian`: a basic install of the debian distro
        1. `alpine`: a basic install of the alpine distro (most popular distro for containers due to extremely small size)
        1. `python`: an alpine container with latest python pre-installed

    1. `docker run`: creates and runs a new container

       automatically calls `docker pull` if needed

        1. `-it`: use this flag whenever you are running an interactive command (such as `bash`); the `i` stands for interactive and the `t` stands for tty

           (pronounced "eye-tee" not "it")
        1. `--name`: provide a name for the container that will be displayed with the `docker ps` command
        1. `--rm`: delete the container after running, useful for preserving disk space
        1. `-d` run as a daemon
        <!--
        1. `-p X:Y`: expose port `Y` in the docker image to lambda server port `X`
        -->
    1. `docker ps`: lists currently running containers
        1. `-a`: list all containers (even those not running)
        1. `-q`: only print container ids
    1. `docker stop`: stop a container started with the `-d` flag
    1. `docker rm`: delete a stopped container that was not created with the `--rm` flag
        1. commonly called with the pattern
           ```
           $ docker rm $(docker ps -qa)
           ```
           to delete all containers
    1. `docker exec`: runs a command in a container without creating a new container
        1. `-it`: same as for `run`

1. Customization commands
    1. `docker build`: creates a new "container image"
        1. `-t`: name the image
    1. `Dockerfile`: a file describing the instructions for creating a new image

1. Debug/admin commands
    1. `docker image`:
        1. `rm`: remove a single image
        1. `prune`: remove ALL images
    1. `docker system`:
        1. `df`: report disk usage of docker
            
            all docker data stored in `~/.local/share/docker`
            1. a bit "hidden"
            1. counts towards your diskspace quota
    1. `docker logs`: shows `stdout` and `stderr` of all commands run without the `-it` flags; most commonly used on containers started with the `-d` flag
        1. `-f`: follow mode

<!--
1. Parallel programming
    1. All of the hardest parts of an OS course compressed down into 5 minutes

       > **NOTE:**
       > We will revisit this material in more detail after the final in the non-seniors-only portion of the class.

    1. "Trivial" to do in POSIX-compliant shells

        (mod the weird #?*!ing edge cases)

    1. Two techniques: Threads vs Processes
        1. Threads are "lightweight"
            1. minimal overhead
            1. each thread shares the same memory, so communication is easy
            1. slightly less safe because a bug in one thread will cause bad behavior in every program
            1. Python's [global interpretter lock (GIL)](https://realpython.com/python-gil/) means you cannot use threads in python for parallel programming
        1. Processes are "heavyweight"
            1. about 10MB of unavoidable overhead per process in the system kernel
                1. technically, this number is application dependent
                1. 10MB is for postgres (and other "big" programs are same order of magnitude)
            1. additionally, each child process duplicates the memory of its parent process
            1. processes can communicate only by reading/writing to files
            1. processes are the only way to do parallel programming in python
            1. processes created by "forking"
                1. `os.fork()`
                1. [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) built-in library
    1. Programming with threads/processes is HARD
        1. easy to create [memory leaks](https://en.wikipedia.org/wiki/Memory_leak), [race conditions](https://en.wikipedia.org/wiki/Race_condition), and other hard-to-debug problems
        1. easy to accidentally create [fork bombs](https://en.wikipedia.org/wiki/Fork_bomb), which were the original form of [cracking](http://www.catb.org/jargon/html/C/cracker.html)
        1. code is non-deterministic (everytime you run it, you get different results), resulting in lots of [heisenbugs](https://en.wikipedia.org/wiki/Heisenbug)
            1. simple example: [I can't login standing up](https://www.reddit.com/r/talesfromtechsupport/comments/3v52pw/i_cant_log_in_when_i_stand_up/)
            1. complicated example: [I can't send email more than 500 miles](http://www.ibiblio.org/harris/500milemail.html)
            1. (links in the lecture notes are never required... but the "most cultured" programmers will want to read them... these two in particular)
        1. python is not great for manipulating processes (it's very easy to create very bad bugs); bash is much better; so I always do the parallel programming parts in bash
        1. MapReduce paradigm simplifies parallel data analysis
-->

1. Basic networking
    1. Internet Protocol (IP) addresses
        1. (Almost) every device on the internet has a unique IPv4 address.
           IPv4 uses 32bit addresses (looks like 134.173.191.241), which supports up to 4 billion unique addresses.
        1. The internet is slowly moving to the IPv6 standard.
           IPv6 uses 64bit addresses (looks like `fe80::3efd:feff:fedd:feec`).
        1. The IPv4 address `127.0.0.1` is called a "loopback" address because it always refers to the computer you are working on.
    1. TCP port numbers
        1. ports are numbers between 1 and 2^16-1 (65535)
        1. different services listen on different ports
        1. some standard ports are:
            1. ssh is 22
            1. http is port 80
            1. https is port 443
        1. notice that the lambda server is running ssh on a non-standard port,
           and that is why you must specify the `-p` flag when connecting
        1. only root can listen on ports < 1024;
           therefore, you cannot use the standard ports for your web services running on the lambda server
    1. port forwarding lets you redirect connections from one computer to another ([optional reference](https://www.ssh.com/ssh/tunneling/example))

## Lab

This is a "hello world" assignment for flask/docker that just ensures you have a sane working environment.

**Part 0: terminal-based web client**

Any task that you can do without the terminal can be done with the terminal,
including browsing the web.
The most popular command line web browser is called `links`.
Login to the lambda server, and run the command
```
$ links http://www.phrack.org
```
to browse to the phrack magazine.
Phrack is an old-school hacker zine.
Issue 7, article 3 has the famous "hacker manifesto",
and you should try to browse to it and open it in links.

> **HINT:**
> The up/down arrows take you to the next link,
> but there's a lot of links on a page,
> so moving to the correct link can take a long time.
> Use the `/` key to search for text to navigate the webpage faster.

Browsing the web this way is unfortunately rather inconvenient,
and so you may be tempted to ask why would anyone do it?
The simplest answer is that many people must use command line web browsers due to physical disability.
For example, the famous physicist Stephen Hawking

<img src=hawking.webp width=400px />

could not use a mouse,
and so could not use a traditional web browser.
In order to make your webpages accessible to people like Hawking,
it is good practice to test your webpages in the links browser.
And the Americans with Disabilities Act (ADA) actually requires that large companies and government agencies do this.

Another reason to use the links browser is that we can run it on remote machines and access web servers that our laptop doesn't have direct access to.
For example, run the command
```
$ links http://localhost:5000/
```
You should see a simple hello world webpage get displayed in the links browser.
But if you try to access this url from firefox on your laptop,
you will get an error message.
This webpage is running on port 5000 of the lambda server,
but you can't connect to this webpage directly due to various firewalls that the CMC IT folks have installed.
The links program is the easiest way to bypass these firewalls.

**Part 1: port forwarding**

For most of, however, browsing the web with links would be very inconvenient,
and so we would rather be able to use firefox to access the webpage.
(But definitely not chrome/safari... bleh... that spyware crap is gross.)
[Port forwarding](https://en.wikipedia.org/wiki/Port_forwarding) is a way for ssh to make web applications that are only available on remote servers available locally on your computer.

<!--
In order to see the webpage that you'll create in the docker tutorial (Part 2),
you'll need to use port forwarding.
Port forwarding can be tricky to setup,
so this first part of the lab focuses just on understanding port forwarding without docker.
-->

Port forwarding gets enabled when you login to the lambda server.
Depending on how you login, the instructions will be slightly different.
1. **Mac/Linux/Windows (with power shell)**: log on to the lambda server with the following command
    (changing `username` to your username):
    ```
    $ ssh username@134.173.191.241 -p 5055 -L 8080:localhost:5000
    ```
    This tells ssh to forward all requests to port 8080 on your computer (`localhost`) to port 5000 on the lambda server.

1. **Windows (with Putty)**:
    You will have to select the appropriate checkboxes in putty to get local port forwarding enabled.
    You can follow [these instructions](https://web.archive.org/web/20180508204631/https://blog.devolutions.net/2017/4/how-to-configure-an-ssh-tunnel-on-putty) to get pictures of where the checkboxes are located.
    You want port 8080 for the local side and port 5000 for the remote side of the connection.

Once you're logged into the lambda server, visit the url
<http://localhost:8080>
in your web browser.
You should see a page showing the date.

**Part 2: a terminal-based web server**

Now we will create a simple web server using shell commands.
You will need a partner to complete this part of the lab.

> **RECALL:**
> It is an academic integrity violation to work with a partner on these assignments if you are not either in class or in the QCL.

On the lambda server, run the following command:
```
$ while true ; do echo "$MESSAGE" | nc -lq1 -p $PORT ; done
```
where `$MESSAGE` is a message you want to send to your partner and `$PORT` is a number number between `2**10` and `2**16`.

> **NOTE:**
> `nc` is short for "net cat" and is like the familiar `cat` command but outputs to the network instead of the terminal.
> So in the command above, we're using the pipe to send the results of `echo` to the network.
> When a web browser connects to `lambda-server:$PORT`
> By piping in more complicated commands into `nc`,
> we can easily create simple web services in one line of shell that would take hundreds of lines of python.

Now, your partner should try to connect to your webserver using port forwarding.
(And you should try to connect to theirs.)
Don't move onto the last step until you get this working.

**Part 3: docker**

Follow these instructions to create a simple flask app running in a docker container: <https://runnable.com/docker/python/dockerize-your-flask-application>.

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

Finally, there's a handful of errors that you'll get when you build the project.
You'll find that fixing these errors only takes a very small change to the project files,
but figuring out exactly what this change is will be quite difficult.
The fundamental problem is that various libraries/packages have introduced breaking changes since the author of the tutorial wrote the tutorial.
The easiest way to figure out how to get the right versions is to open up a working container with the `docker run` command,
then manually try installing all the different versions of the libraries until you get something that successfully creates the webpage.
Once you've figured out the correct sequence of commands,
then you should modify the `Dockerfile` to reflect these new commands.

**Submission:**

Put all your files from Part 3 into a github repo,
and upload the url to sakai.

## Homework

No homework this week :)

Just work on the twitter/MapReduce homework.

<!--
You should start the [twitter MapReduce](../hw_twitter) homework.
Because this homework can potentially take a very long time to run,
this homework has a modified due date schedule.
-->
