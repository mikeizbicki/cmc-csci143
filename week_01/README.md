# More Unix + Docker Intro

<img src=automate.jpeg width=400px />

## More Unix

**Monday Announcements:**

1. 10 students have completed last weeks lab
    1. you're not behind if you haven't done it yet
    1. if you don't finish it this week, you will be behind
    1. **Friday update:**
        1. only 18/29 students have completed last week's lab
           
           6 students missed points; check comments and resubmit
        1. 11/18 students have completed the homework
        1. you are now behind if you have not, and should be *slightly* worried

1. Great use of github issues to ask questions!
    1. All questions should go through github issues
        1. Faster response from me than email
        1. Other people (TAs/students) can respond if I'm slow
        1. Recruiters will run stats on your github profile, and this will improve your stats
        1. Everyone has access to the answers
    1. Email only for grade related questions
    1. Make sure to "watch" the repo!
        1. Otherwise, you won't get class announcements

1. Quiz next Wednesday
    1. You will have the first 10 minutes of class to complete the quiz
    1. I will arrive to class >20 minutes before the start of class; if you arrive early, you may start the quiz early

       (so basically, you can have up to 30 minutes on the quiz if you'd like; time shouldn't be an issue for anyone)

    1. the `quiz` folder contains a sample

**Lecture:**

<img src=LinuxAdmin.jpg width=600px />

1. Definitions:
    1. **Terminal** the graphical program that you type in
        1. technically, this is a **terminal emulator**
        1. handles things like copy/paste, colorscheme, etc.
        1. runs on your computer, not the lambda server
    1. **Shell** the non-graphical program that actually runs the commands
        1. it is a "thin wrapper" over the operating system
        1. runs on the lambda server, not your computer

1. [Types of unix shells](https://www.multicians.org/shell.html)
    1. Ken Thompson wrote the first Unix shell called `sh` in 1971
    1. `sh` was inspired by the RUNCOM shell (`rc`), which was written in 1963
        1. `.*rc` config files were originally designed for the RUNCOM shell
        1. `.vimrc` and `.bashrc` are examples
    1. Many shells replaced the Thompson shell in the original Unix
        1. the most famous is Stephen Bourne wrote the Bourne shell in 1979
    1. Open Source shells:
        1. Almquist shell (`ash`) written by Kenneth Almquist in 1980; BSD-licensed
        1. The Bourne-Again shell (`bash`) written by Brian Fox in 1989; GPL-licensed

           Bash is the GNU project's shell

           It is by far the most popular (interactive) shell,
           and therefore people often (incorrectly) say they are writing a "bash" script when they are writing a generic "POSIX" script

           <img src=gnu+linux.jpg width=600px />

           See the [GNU+Linux copypasta](https://itsfoss.com/gnu-linux-copypasta/)
        1. The Debian-Almquist shell (`dash`) written by Herbert Xu ini 1997; GPL-licensed
        1. Z shell (`zsh`) is the default on Mac; BSD-licensed
    1. POSIX
        1. All the shells above have slightly different behaviors
        1. POSIX defines the a universal standard of minimal features that all shells must have
        1. It's best to try to write POSIX-compliant scripts to ensure portability (and speed, since you can use `dash` to run the script)
        1. Lots of weird behaviors that result from needing backwards compatibilty
            1. These make programming seem easy, but actually super #?*!ing hard
               <img src=bash-meme.jpg width=600px />
            1. Your quiz will scratch the surface of these hard edge cases
            1. (optional) for detailed examples, see https://dwheeler.com/essays/fixing-unix-linux-filenames.html
    1. Non-POSIX shells 
        1. Fix POSIX problems, but not backwards compatible, so not popular
        1. The [friendly interactive shell](https://github.com/fish-shell/fish-shell) (`fish`)


## Docker

**Pre-lecture work:** (Complete before class on Wednesday)

1. Watch the following videos:

    1. [What is GNU+Linux](https://www.youtube.com/watch?v=kb2T8hWRu8g) by RMS

    1. [Virtual Machines vs Docker Containers](https://www.youtube.com/watch?v=TvnZTi_gaNc)

    1. (optional) [Docker vs Kubernetes vs Docker Swarm](https://www.youtube.com/watch?v=9_s3h_GVzZc)

    <!--
    1. (optional) [MapReduce - Computerphile](https://www.youtube.com/watch?v=cvhKoniK5Uo)

    1. (optional) [Apache Spark - Computerphile](https://www.youtube.com/watch?v=cvhKoniK5Uo)
    -->

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

        1. you have to use it to full understand it... so labs/hws will be super important

1. References:
    1. https://www.docker.com/resources/what-container

       Helps you understand the following jokes:

       <img src=docker-vm.png width=600px />

       <a href=https://www.commitstrip.com/en/2016/06/24/how-to-host-a-coder-dinner-party/>
       <img src=Strip-Discussion-Docker-english650final-1.jpg width=600px />
       </a>

    1. https://docs.docker.com/get-started/overview/

       Helps you actually understand the commands below

1. Basic Commands

    1. `docker pull`: download a docker image

        important images include:
        1. `ubuntu`: a basic install of the ubuntu distro
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
1. More unix shell
    1. for loops
    1. glob (`*`)
    1. file permissions ([optional reference](https://linuxhandbook.com/linux-file-permissions/))
    1. `PATH` environment variable
-->

## Friday: some loose ends

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
        1. easy to create [memory leaks](https://en.wikipedia.org/wiki/Memory_leak), [race conditions](https://en.wikipedia.org/wiki/Race_condition), and other hard-to-debug problems
        1. easy to accidentally create [fork bombs](https://en.wikipedia.org/wiki/Fork_bomb), which were the original form of [cracking](http://www.catb.org/jargon/html/C/cracker.html)
        1. code is non-deterministic (everytime you run it, you get different results), resulting in lots of [heisenbugs](https://en.wikipedia.org/wiki/Heisenbug)
            1. simple example: [I can't login standing up](https://www.reddit.com/r/talesfromtechsupport/comments/3v52pw/i_cant_log_in_when_i_stand_up/)
            1. complicated example: [I can't send email more than 500 miles](http://www.ibiblio.org/harris/500milemail.html)
            1. (links in the lecture notes are never required... but the "most cultured" programmers will want to read them... these two in particular)
        1. python is not great for manipulating processes (it's very easy to create very bad bugs); bash is much better; so I always do the parallel programming parts in bash
        1. MapReduce paradigm simplifies parallel data analysis

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
      <https://localhost:8080>
      in your web browser.
      You should now have access to the search engine.

      > **NOTE:**
      > Only muggles use chrome/edge/safari.
      > Proper hackers use firefox with the uBlock origin extension.
      > Almost all other add block extensions either sell your browsing history or let advertisers pay to not have their ads blocked.

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
