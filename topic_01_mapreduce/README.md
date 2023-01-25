# shell scripting (and parallel programming)

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
    1. Ken Thompson wrote the first Unix shell called the "Thompson Shell" (`sh` for short) in 1971
    1. `sh` was inspired by the RUNCOM shell (`rc`), which was written in 1963
        1. `.*rc` config files were originally designed for the RUNCOM shell
        1. `.vimrc` and `.bashrc` are examples
    1. Many shells replaced the Thompson shell in the original Unix
        1. the most famous is Stephen Bourne wrote the Bourne shell in 1979
           
           the Bourne shell was the default for UNIX version 7+
    1. Open Source shells:
        1. Almquist shell (`ash`) written by Kenneth Almquist in 1980; BSD-licensed
        1. The Bourne-Again shell (`bash`) written by Brian Fox in 1989; GPL-licensed

           Bash is the GNU project's shell and by far the most popular (interactive) shell

           and therefore people often (incorrectly) say they are writing a "bash" script when they are writing a generic "POSIX" script

           <img src=gnu+linux.jpg width=600px />

           See the [GNU+Linux copypasta](https://itsfoss.com/gnu-linux-copypasta/)
        1. The Debian-Almquist shell (`dash`) written by Herbert Xu ini 1997; GPL-licensed

            Dash is used on all Debian-based systems (including the lambda server) for system-wide scripts.
            it has fewer features than bash but is much faster.
        1. Z shell (`zsh`) is the default on Mac; BSD-licensed

    1. POSIX
        1. All the shells above have slightly different behaviors
        1. POSIX defines the a universal standard of minimal features that all shells must have

           POSIX = Portable Operating System Interface
        1. It's best to try to write POSIX-compliant scripts to ensure portability (and speed, since you can use `dash` to run the script)
        1. Lots of weird behaviors that result from needing backwards compatibilty
            1. These make programming seem easy, but actually super #?*!ing hard
               <img src=bash-meme.jpg width=600px />
            1. Your quiz will scratch the surface of these hard edge cases
            <!--
            1. (optional) for detailed examples, see https://dwheeler.com/essays/fixing-unix-linux-filenames.html
            -->
    1. Non-POSIX shells 
        1. Fix POSIX problems, but not backwards compatible, so not popular
        1. The [friendly interactive shell](https://github.com/fish-shell/fish-shell) (`fish`)
        1. The [OIL Shell](https://www.oilshell.org/)


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

## Lab

In-class lab Friday 27 Jan cancelled due to data science capstone kickoff.

No late penalty for this lab, and you may collaborate however you'd like.

**Pre-lab work:**

1. Ensure that you have completed the entire lab for `topic_00` before completing this lab.

    1. If you don't feel 100% confident in the git terminal commands,
        then re-do the git+unix tutorial from last week.

        (It's okay if you don't feel confident in these commands at this point.
        I expect most of the class would benefit from redoing the tutorial.)

1. Spend at least 20 minutes reviewing how to use vim effectively.
    You can either:
    
    1. re-do the vimtutor tutorial from last pre-lab, or
    2. try the more interactive tutorial at <https://www.openvim.com/>.

**Instructions:**

1. Complete the [shell scripting and parallel programming tutorial](processes.md)

<!--
1. In the previous lab, you forked the class repository.
    Since then, however, I have made updates to the class repo,
    and those updates won't be reflected in your forked repo.
    In this first task,
    you must update your forked repo so that it has all the content of my upstream repo.

    Use the following flowchart to help you get the commands correct:

    <img width='100%' src=update_downstream.png />

    Note that the steps with "negative numbers" are events that have already happened,
    steps with "zero numbers" are events that you only have to run once to setup your local repo.
    Every time you need to update your repo,
    you will start with step 1.
-->

1. For each of the tasks below, write a POSIX-compliant one line shell command that completes the task.
    Upload both the command and your result to sakai.
    The command should be able to run from any directory,
    and so should use absolute and not relative paths.

    1. Count the total number of days in the geolocated tweets dataset.
       The dataset is located in the folder `/data/Twitter dataset` and has

    1. Count the number of geolocated tweets sent on 2020-12-25 that contain the word "coronavirus".
       The file `/data/Twitter dataset/geoTwitter20-12-25.zip` contains all geolocated tweets sent on that day,
       and you should be able to count tweets that write the word "coronavirus" with any capitalization.
       (For example, you should include both `coronavirus` and `cOrOnAvIrUs`.)

       My command took 51 seconds to run, and I got 3143 tweets.
       
       > **HINT:**
       > Use the `unzip` command to extract the contents of the zip archive;
       > you will have to read the man page in order to figure out the correct option to get the output printed on stdout.
       > (Use the command `man unzip` to open the manpage, then type the forward slash key `/` to search; `/` is also used the hotkey for searching in vim, firefox, and other open source programs.)
       > Use the `tr 'A-Z' 'a-z'` command to translate all characters into lowercase.
       > Use `grep` to extract only the lines containing `coronavirus`.
       > Use `wc` to count the number of lines.

## Homework

You should start the [twitter MapReduce](../hw_twitter) homework.
Because this homework can potentially take a very long time to run,
this homework has a modified due date schedule.
