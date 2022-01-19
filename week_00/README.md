# Week 00: The Unix Shell

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src=dilbert.gif />
</a>
</center>

## Lecture

We will cover the basics of the unix shell.
This includes:

1. basic shell scripting
1. piping / output redirection
1. file permissions
1. environment variables
1. signals
1. processes
1. git
1. github

The lambda server has:
1. 80 processors
1. 8 GPU
1. 256 GB RAM
1. 2 TB NVME
1. 50 TB RAID array of 16 HDDs

Your accounts have:
1. 10GB storage in the NVME (home folder)
1. 250GB storage in the RAID array (`~/bigdata` folder)

**Pre-lecture work:**

Read/watch the following articles/videos:

1. [Ken Thompson and Dennis Ritchie Explain UNIX](https://www.youtube.com/watch?v=JoVQTPbD6UY)
1. (optional) [Where GREP Came From - Computerphile](https://www.youtube.com/watch?v=NTfOnGZUZDk)
1. (optional) [vim vs emacs: the oldest rivalry in computing](https://slate.com/technology/2014/05/oldest-software-rivalry-emacs-and-vi-two-text-editors-used-by-programmers.html)

Print each of these cheatsheets, and have them handy for lecture:

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)
1. [github pull requests](pull_request.png)

**References:**

1. <https://www.tutorialspoint.com/unix/shell_scripting.htm>

## Lab

**Due Date:**

Labs are always due on midnight of the Sunday of the week that they are assigned (i.e. January 23 for this lab).
If you collaborate with either a student or TA,
then you get a 48 hour extension until the following Tuesday at midnight (i.e. January 25 for this lab).

Weekly homeworks have the same due dates and extension policies.

**Instructions:**

1. Create a GitHub account if you do not already have one.
   Log in, and press the "watch" button at the top of this page.
   This will ensure you get email notifications whenever I post new issues to github.
   Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci143/issues/83).

1. Complete the following "review tasks" from CS46.

    1. Log in to the lambda server.
       Run the command
       ```
       $ vimtutor
       ```
       Complete all instructions in order to learn vim.
       This should take 30-60 minutes.

       > **NOTE:**
       > If you've previously completed the `vimtutor` command,
       > then you do not have to redo the tutorial.
       > Instead, you should spend at least 30 minutes reviewing other vim tips that you will find helpful.
       > I recommend working through the tutorials at <https://thevaluable.dev/vim-commands-beginner/>,
       > but you can use whatever resource you'd like.

       > **NOTE:**
       > There are a number of games designed to help you get better at using vim.
       > The most polished is <https://vim-adventures.com>, which is a vim RPG. 
       > The first 3 levels are free, but you have to pay to continue playing the game.
       > One of my former students also created the [PacVim](https://github.com/jmoon018/PacVim) game,
       > which is an open source pacman clone using vim controls.
       > You're not required to play any of these games,
       > but many people find them more fun than working through standard tutorials.

    1. Follow [these instructions](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/lambda-server.md) to update your lambda server account's settings with a nicer looking prompt.

    1. Work through the following tutorials:
        1. the [unix/git tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/git.md)
        1. the [github tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/github.md)
        1. the [unix processes tutorial](processes.md)

        There is nothing to turn in for these tutorials,
        but subsequent lectures will assume you are 100% comfortable with all of the material.
        So it would behoove you to spend a few hours working through the material to ensure that you fully understand it all.

    1. Log in to the lambda server, and run the command
       ```
       $ typespeed
       ```
       to test your unix typing skills.
       Programmers spend lots of time at the keyboard,
       and so it pays to actually be able to type well.
       Anyone who beats my high score will have my undying admiration :)

       Performing well at `typespeed` is one of the "caveat tasks" in this class.
       You should [work through the task instructions](https://github.com/mikeizbicki/cmc-csci143/blob/2022spring/caveat_tasks/typespeed.md),
       which will also help you review basic terminal commands.

1. Each of the following problems asks you to write a bash command to complete some task.
   You should submit the commands (not the output of the commands, but the actual commands) to sakai.
   **This is the only lab task that requires that you turn anything in.**

    1. Write a 1-line command that counts the number of times the user `mizbicki` is logged in.
       The command should print only a single number and nothing else.

       > **HINT:**
       > Use the `finger`, `grep`, and `wc` commands piped together.
       > Use the command `man wc` to figure out how to limit `wc`'s output to only the number of lines.

    1. Write a 1-line command that counts the number of zip files contained in the directory `/data/Twitter dataset`.

       > **HINT:**
       > Not every file in the directory is a zip file.
       > Use the `ls` command to list all the files,
       > `grep` to select only the zip files,
       > and `wc` to count them.

    1. Count the number of geolocated tweets sent on 2020-12-25 that contain the word "coronavirus".
       The file `/data/Twitter dataset/geoTwitter20-12-25.zip` contains all geolocated tweets sent on that day.

       My command took 51 seconds to run, and I got 3143 tweets.
       
       > **HINT:**
       > Use the `unzip` command to extract the contents of the zip archive;
       > you will have to read the man page in order to figure out the correct option to get the output printed on stdout.
       > Use the `tr 'A-Z' 'a-z'` command to translate all characters into lowercase.
       > Use `grep` to extract only the lines containing `coronavirus`.
       > Use `wc` to count the number of lines.

## Homework

Homeworks will generally be posted into the `homework` [git submodule](https://www.atlassian.com/git/tutorials/git-submodule) for each week.
Like labs, homeworks are always due on midnight of the Sunday of the week that they are assigned (i.e. Jan 23 for this homework, or Jan 25 with the 2 day collaboration extension).

This week's homework assignment is a review assignment from CS46.
Therefore:

1. Only those students who did not take CS46 with me should complete this assignment.
   If you took CS46 with me, you are welcome to complete the assignment as review, but it will not count towards your grade.

1. **There will be no late penalty for this assignment if you miss the due date.**
   This is an important assignment, and I want to ensure that everyone has sufficient time to master it.
