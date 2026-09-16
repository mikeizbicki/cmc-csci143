# MapReduce (via shell scripting)

<img src=img/LinuxAdmin.jpg width=400px />

**Announcements (Monday 14 Sep)**:

1. everything graded
    1. you have 0 as "default grade" for unsubmitted work

        once you submit, I will update your grade

    1. still no late penalties have been applied

1. last week's quiz

    | grade | # students |
    | ----- | ---------- |
    | 4     | 2          |
    | 3     | 5          |
    | <=2   | 13         |

    retake this Wednesday

    1. complete during normal quiz time
    1. everyone may take a copy
    1. if you submit the copy, your grade on the copy will replace your existing grade

## Lecture Notes

1. Definitions:
    1. **Terminal** the graphical program that you type in
        1. runs on your computer, not the lambda server
        1. handles things like copy/paste, colors, font size

    1. **Shell** the non-graphical program that actually runs the commands
        1. runs on the lambda server, not your computer
        1. it is a "thin wrapper" over the operating system "kernel"

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

            1. The Debian-Almquist shell (`dash`), written by [Herbert Xu](https://www.linux.com/news/30-linux-kernel-developers-30-weeks-herbert-xu/) in 1997; GPL-licensed

                <img src=img/Herbert_Xu.jpg width=240px />

                Dash is used on all Debian-based systems (including the lambda server, which runs Ubuntu) for system-wide scripts.
                It has fewer features than bash but is much faster.
            1. Z shell (`zsh`) is the default on Mac (since 2019); BSD-licensed

                The name comes from [`z`hong `sh`ao](https://www.cs.yale.edu/homes/shao-zhong/) (currently a professor at Yale).

                But `zsh` was written by his student [Paul Falstad](https://www.falstad.com/) as an undergrad student project.

    1. POSIX (= Portable Operating System Interface)
        1. All the shells above have slightly different behaviors
        1. POSIX defines the universal standard of minimal features that all shells must have
        1. It's best to try to write POSIX-compliant scripts to ensure portability (and speed, since you can use `dash` to run the script)
        1. Lots of weird behaviors that result from needing backwards compatibility
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

            <img src=img/lindy.webp width=500px />

1. Famous bugs caused by bad shell use:
    1. (1998) Toy story: <https://thenextweb.com/news/how-pixars-toy-story-2-was-deleted-twice-once-by-technology-and-again-for-its-own-good>
    1. Modern:
        1. (2026-02-21) OpenClaw CVE-2026-27209: <https://github.com/openclaw/openclaw/security/advisories/GHSA-65rx-fvh6-r4h2>
        1. (2026-02-25) ClaudeCode command injection: <https://github.com/anthropics/claude-code/issues/28784>
        1. (2026-06-19) Network-AI: <https://github.com/advisories/GHSA-qw6v-5fcf-5666?utm_source=chatgpt.com>
        1. (2025-11-18) node.js: <https://github.com/advisories/GHSA-5j98-mcp5-4vw2>
        1. (2026-03-19) vim: <https://github.com/vim/vim/security/advisories/GHSA-w5jw-f54h-x46c>
    1. Common Weakness Enumeration (CWE):
        1. CWE-78: Command Injection <https://cwe.mitre.org/data/definitions/78.html>
        1. CWE-88: Argument Injection <https://cwe.mitre.org/data/definitions/88.html>
    1. These types of errors are common in AI agent output

        <img src=img/claude.jpg width=300px />

1. Parallel programming
    1. All of the hardest parts of an OS course compressed down into 5 minutes

    1. "Trivial" to do in POSIX-compliant shells with `&` + `nohup`

        (mod the weird `fsck`ing edge cases)

    1. Two techniques: Threads vs Processes
        1. Threads are "lightweight"
            1. minimal overhead
            1. each thread shares the same memory, so communication is easy
            1. slightly less safe because a bug in one thread will cause bad behavior in every program
            1. Python's [global interpreter lock (GIL)](https://realpython.com/python-gil/) means you cannot use threads in python for parallel programming

                <img src=img/gil.jpg width=300px />

        1. Processes are "heavyweight"
            1. about 10MB of unavoidable overhead per process in the system kernel
                1. technically, this number is application dependent
                1. 10MB is for postgres (and other "big" programs are of the same order of magnitude)
            1. additionally, each child process duplicates the memory of its parent process
            1. processes can communicate only by reading/writing to files
            1. processes are the only way to do parallel programming in python
            1. processes created by "forking"
                1. `os.fork()`
                1. [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) built-in library

    1. Programming with threads/processes is HARD
        1. easy to create [memory leaks](https://en.wikipedia.org/wiki/Memory_leak), [race conditions](https://en.wikipedia.org/wiki/Race_condition), and other hard-to-debug problems
        1. easy to accidentally create [fork bombs](https://en.wikipedia.org/wiki/Fork_bomb), which were the original form of [cracking](http://www.catb.org/jargon/html/C/cracker.html)
        1. code is non-deterministic (every time you run it, you get different results), resulting in lots of [heisenbugs](https://en.wikipedia.org/wiki/Heisenbug)

            <img src=img/heisenbug.jpg width=400px />

            1. simple example: [I can't login standing up](https://www.reddit.com/r/talesfromtechsupport/comments/3v52pw/i_cant_log_in_when_i_stand_up/)
            1. complicated example: [I can't send email more than 500 miles](http://www.ibiblio.org/harris/500milemail.html)
            1. (links in the lecture notes are never required... but the "most cultured" programmers will want to read them... these two in particular)

    1. MapReduce paradigm simplifies parallel data analysis
        1. trivial to do in bash with `&` and `nohup`
        1. cloud options expensive and require "specialized" knowledge

            <img src=img/yes-no.jpg width=400px />

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

**Prelab:**

> **Note:**
> If you took CSCI046 with me, then you've already completed this prelab work.
> You are not required to complete it again.

1. Complete the following two lab assignments from CSCI046.
    Both labs have tasks you will have to submit on canvas.

    1. [lab-pipes-twitter](https://github.com/mikeizbicki/lab-pipes-twitter)
    1. [lab-processes](https://github.com/mikeizbicki/lab-processes).

1. The next (short) task is designed to help you learn vim.

    <img src=img/vim.jpg width=400px />

    Using the [vim cheatsheet](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf):

    1. select 10 verbs and 10 motions
    1. write by each of these commands and what they do
    1. do your best to memorize these commands and incorporate them into your workflow

**Lab:**

TBA

<!--
The lab is posted in the [lab-posix-mapreduce submodule](https://github.com/mikeizbicki/lab-posix-mapreduce).
-->

## Homework

Homework repo is: <https://github.com/mikeizbicki/twitter_coronavirus>

**Modified Due Date:**
Tuesday, 6 October.

I recommend starting early and having everything complete by 29 September.

Why?

- Runtime on unloaded lambda server: 3-5 hours

- Runtime on heavily loaded lambda server: 5 hours * 20 students = 100 hours = 4 days 

There will be no extensions given for code not completing in time.
