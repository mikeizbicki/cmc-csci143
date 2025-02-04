# MapReduce (via shell scripting)

<img src=img/LinuxAdmin.jpg width=600px />

**Announcements (Tuesday 2025-01-28)**

Issues:
1. Overall great use of github issues :)
1. Do not post issues to submodules (i.e. repos that are not the main class repo)

Labs:
1. "Due" last night.
1. 28/38 submitted.
1. 10 non-submitted students:
    1. No late penalty, but be reasonable.
    1. Reach out if you need help.

Homework:
1. Due tonight (but no late penalty)
1. I won't be covering in class how to submit pull requests.
1. If you'd like a review, see the Spring 2023 CS46 class recording: <https://www.youtube.com/watch?v=M9qT9fOBuIA&t=1460s>.

    (Video starts with a short conversation about grades, then uses a pull request to change how grading is done.)

Quiz:
1. This Thursday
1. 4 problems from Shell Topics 00-02.
1. 10 minutes during class
1. I will be in the classroom 10-20 minutes before class
<!--
1. For more quiz review:
    1. CS46 POSIX 1 Lecture: <https://www.youtube.com/watch?v=5LmyskP7j7Y&t=897s>
    1. CS46 POSIX 2 Lecture (part 1): <https://www.youtube.com/watch?v=4BkIoN_8-cE&t=2420s>
    1. CS46 POSIX 2 Lecture (part 2): <https://www.youtube.com/watch?v=zjCJU5CrvZs&t=3m40s>
-->

**Announcements (Thursday 2025-01-30)**

Grades:
1. All grades updated in sakai.
1. I have entered 0 for unsubmitted hw/labs.

    Once you submit, I will regrade without a penalty.

This week assignments:
1. Lab no penalty for late submission this week.
    But to qualify, you must email me before the due date explaining why you didn't finish in time and what you'll do differently in the future.
1. Homework not yet posted.  (We will continue working on this topic next week.)

Quiz:
1. Next week covers Shell topics 03, 04, ~~05~~
1. Will have 4 review problems + 4 new problems
1. Option to retake this week's quiz (new problems) with no penalty.  You will keep whatever grade you get on the retake.
1. Future notes packets will not have as much material

**Announcements (Tuesday 2025-02-04)**

1. Everything updated in sakai.

    Overall grades:

    <img src=img/grades.png width=300px />

    Quiz grades:

    <img src=img/grades-quiz.png width=300px />

1. Many people received zeros on submitted assignments.
    1. You may fix the mistake and resubmit for full credit.
    1. Check sakai to see if this applies to you.

1. Too many people taking advantage of the no late penalty policy.

    | Assignment                            | Submissions Received |
    | ------------------------------------- | ----- |
    | topic01 lab: posix-mapreduce          | 24/37 |
    | topic01 prelab: processes             | 31/37 |
    | topic01 prelab: pipes-twitter         | 31/37 |
    | topic00 lab: goodreads2               | 34/37 |
    | topic00 lab: goodreads1               | 35/37 |
    | topic00 hw: continuous-integration    | 33/37 |

    1. It's bad to fall behind in this course.

    1. Later portions of this course assume perfect understanding of the topic00/topic01 review material.

    1. Grace period ends this Sunday (9 Feb).
        Any submissions received after this time period will receive late penalties.

1. As a cohort, you all are behind previous iterations of this class.

   Course modifications:
    1. We'll be spending another week on review material.
        (A new lab will be posted below later this week.)
    1. Quiz Thursday will cover Shell Topics 03 and 04 only (not 05).

        Recall that you can retake the first quiz during this same time period.
    1. I've hired a TA for this class (Ainslee Archibald).
        Expect an announcement about her availability soon.

## Lecture Notes

1. Definitions:
    1. **Terminal** the graphical program that you type in
        1. technically, this is a **terminal emulator**
        1. handles things like copy/paste, colorscheme, etc.
        1. runs on your computer, not the lambda server
    1. **Shell** the non-graphical program that actually runs the commands
        1. it is a "thin wrapper" over the operating system "kernel"
        1. runs on the lambda server, not your computer

1. [Types of unix shells](https://www.multicians.org/shell.html)
    1. [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson) wrote the first Unix shell, called the "Thompson Shell" (`sh` for short), in 1971

        <img src=img/Ken_Thompson_and_Dennis_Ritchie--1973.jpg width=400px />

    1. `sh` was inspired by RUNCOM (short for *run commands*, also abbreviated as `rc`), which was written in 1963
        1. `.*rc` config files were originally designed for the RUNCOM shell
        1. `.vimrc` and `.bashrc` are examples
    1. Many newer shells
        1. The Bourne shell (named after author Stephen Bourne) became the standard in UNIX in 1979
        1. Open Source shells:
            1. Almquist shell (`ash`), which was written by Kenneth Almquist in 1980; BSD-licensed
            1. The Bourne-Again shell (`bash`), which was written by [Brian Fox](https://en.wikipedia.org/wiki/Brian_Fox_(programmer)) in 1989; GPL-licensed

                <img src=img/330px-BrianJFox.png width=240px />

                Bash is the GNU project's shell and by far the most popular (interactive) shell

                <img src=img/gnu+linux.jpg width=600px />

                See the [GNU+Linux copypasta](https://itsfoss.com/gnu-linux-copypasta/)

            1. The Debian-Almquist shell (`dash`), written by Herbert Xu in 1997; GPL-licensed

                Dash is used on all Debian-based systems (including the lambda server, which runs Ubuntu) for system-wide scripts.
                It has fewer features than bash but is much faster.
            1. Z shell (`zsh`) is the default on Mac; BSD-licensed

    1. POSIX (= Portible Operating System Interface)
        1. All the shells above have slightly different behaviors
        1. POSIX defines the universal standard of minimal features that all shells must have
        1. It's best to try to write POSIX-compliant scripts to ensure portability (and speed, since you can use `dash` to run the script)
        1. Lots of weird behaviors that result from needing backwards compatibilty
            1. These make programming hard tasks easy, but easy tasks super &?*!ing hard

               <img src=img/bash-meme.jpg width=600px />
            <!--
            1. Your quiz will scratch the surface of these hard edge cases
            1. (optional) for detailed examples, see https://dwheeler.com/essays/fixing-unix-linux-filenames.html
            -->
    1. Non-POSIX shells 
        1. Fix POSIX problems, but not backwards compatible, so not popular
        1. The [friendly interactive shell](https://github.com/fish-shell/fish-shell) (`fish`)
        1. The [OIL Shell](https://www.oilshell.org/)

        1. Non-POSIX shells are not [Lindy](https://en.wikipedia.org/wiki/Lindy_effect)

            > The Lindy effect proposes the longer a period something has survived to exist or be used in the present, the longer its remaining life expectancy.


1. Parallel programming
    1. All of the hardest parts of an OS course compressed down into 5 minutes

    1. "Trivial" to do in POSIX-compliant shells with `&` + `nohup`

        (mod the weird `fsck`ing edge cases)

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

<!--
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
-->

## Lab (31 Jan)

**Prelab Tasks:**

1. Spend at least 20 minutes reviewing how to use Vim effectively.
    You can either:
    
    1. redo the `vimtutor` tutorial from last pre-lab, or
    2. try the more interactive tutorial at <https://www.openvim.com/>.

    > **Warning:**
    > It will be tempting to skip this task.
    > But recall that you will be using Vim throughout the semester.
    > That's 10 hours/week times 15 weeks = 150 hours.
    > If you actually learn how to use the tool,
    > then the rest of the semester will be much more pleasant for you.

1. If you don't feel 100% confident in the git terminal commands,
    then redo [CSCSI046's git+unix tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2023spring/topic_00_unix/git.md) that was assigned for last week's homework.

    (It's okay if you don't feel confident in these commands at this point.
    I expect most of the class would benefit from redoing the tutorial.)

1. Complete the following two lab assignments from CSCI046.
    Both labs have tasks you will have to submit on sakai.

    1. [lab-pipes-twitter](https://github.com/mikeizbicki/lab-pipes-twitter)
    1. [lab-processes](https://github.com/mikeizbicki/lab-processes).

    > **Note:**
    > If you took CSCI046 with me, then you've already completed these labs.
    > You are still required to complete them again.

**Instructions:**

The lab is posted in the [lab-posix-mapreduce submodule](https://github.com/mikeizbicki/lab-posix-mapreduce).

## Lab (7 Feb)

TBA

## Homework

TBA
<!--
The homework is posted in the [hw-twitter-mapreduce](https://github.com/mikeizbicki/twitter_coronavirus) git submodule.

**Modified Due Date:**
Tuesday, 18 February.

You have 3 weeks to complete the assignment due to potentially long computation times.
You should get started early.
There will be no extensions if your code does not finish in time.
-->
