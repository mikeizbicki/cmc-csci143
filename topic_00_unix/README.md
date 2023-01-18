# Topic 00: Unix and the open source workflow

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src=dilbert.gif />
</a>
</center>

## Lecture

We will cover how to

1. work on a remote unix server
1. use the git version control system
1. use continuous integration to "prove" that your code works

Cheat sheets:

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)
1. [github pull requests](pull_request.png)

All of our work in this class will be done on the "lambda server."
(You should have received an email with login credentials.)
The lambda server has:
1. 80 processors
1. 8 GPU
1. 256 GB RAM
1. 2 TB NVME
1. 50 TB RAID array of 16 HDDs

Your accounts have:
1. 10GB storage in the NVME (home folder)

## Lab

**Due Date:**

Labs are always due on midnight of the Sunday of the week that they are assigned (i.e. January 22 for this lab).

*For this lab only:*
There will be no late penalty if you miss the due date,
but please be reasonable.
This is all important background material,
and I want to ensure that everyone has sufficient time to complete it based on their background experience.

**Pre-lab work:**

<!--
1. Read/watch the following articles/videos:

    1. [Ken Thompson and Dennis Ritchie Explain UNIX](https://www.youtube.com/watch?v=JoVQTPbD6UY)
    1. (optional) [Where GREP Came From - Computerphile](https://www.youtube.com/watch?v=NTfOnGZUZDk)
    1. (optional) [vim vs emacs: the oldest rivalry in computing](https://slate.com/technology/2014/05/oldest-software-rivalry-emacs-and-vi-two-text-editors-used-by-programmers.html)

    1. (optional) Corey Schafer's [Git Tutorial for Beginners: Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4).
       Corey is a really famous youtuber for programming tutorials, and you can watch his other videos too if you need more background.
       -->
       
1. Create a GitHub account if you do not already have one.
   Log in, and press the "watch" button at the top of this page.
   This will ensure you get email notifications whenever I post new issues to github.

1. Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci143/issues/226).

1. Log in to the lambda server.
   Run the command
   ```
   $ vimtutor
   ```
   Complete all instructions in order to learn vim.
   This should take 30-60 minutes.

   Vim is famous for having a steep learning curve,
   and has inspired lots of memes/comics:

   <img src=vim-productivity.jpg width=500px>

   <img src=vim-comic2.webp width=500px>

   <img src=vim-comic.jpg width=500px>

1. (Optional)
   Play the <https://vim-adventures.com> game to learn vim while playing a game.
   The first 3 levels are free, but you have to pay to continue playing the game.
   Anyone who completes the entire game before the end of the semester gets +1 point extra credit.

**Instructions:**

1. Complete the following "review tasks" from CS46.

    1. Update your lambda server account settings to match mine,
       which are a bit more user friendly than the defaults.
       Follow [these instructions](https://github.com/mikeizbicki/cmc-csci046/blob/2023spring/topic_00_unix/lambda-server.md) to make the changes.

    1. Work through the following tutorials that review important unix shell concepts:

        1. the [unix/git tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2023spring/topic_00_unix/git.md)
        3. the [github tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/topic_00_unix/github.md)
        3. the [unix processes tutorial](processes.md)

<!--
    1. Finally, you will begin the `typespeed` "caveat task.
       
       Log in to the lambda server, and run the command
       ```
       $ typespeed
       ```
       Follow the command prompts to test your typing speed on the "Unix commands" task.
       (Press `1` then `Enter` in the menu to enter the task.)

       Programmers spend lots of time at the keyboard,
       and so it pays to actually be able to type well.
       Anyone who beats my high score will have my undying admiration :)

       Performing well at `typespeed` is one of the "caveat tasks" in this class.
       You should [work through the task instructions](../caveat_tasks/typespeed.md),
       which will also help you review basic terminal commands.
-->

<!--
1. Each of the following problems asks you to write a bash command to complete some task.
   You should submit the commands (not the output of the commands, but the actual commands) to sakai.
   The commands must work no matter what the current working directory is (i.e., do not rely on the user having run a `cd` command previously).
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

       > **NOTE:**
       > The directory with the data is named `/data/Twitter dataset`,
       > but you cannot directly type this as an argument to an executable program due to the space.
       > Instead, you must "escape" the space using a backslash or quotation marks to pass it as an argument.
       > For example, 
       > ```
       > $ ls /data/Twitter dataset
       > ```
       > will not work, but
       > ```
       > $ ls '/data/Twitter dataset'
       > ```
       > will work.

    1. Count the number of geolocated tweets sent on 2020-12-25 that contain the word "coronavirus".
       The file `/data/Twitter dataset/geoTwitter20-12-25.zip` contains all geolocated tweets sent on that day.

       My command took 51 seconds to run, and I got 3143 tweets.
       
       > **HINT:**
       > Use the `unzip` command to extract the contents of the zip archive;
       > you will have to read the man page in order to figure out the correct option to get the output printed on stdout.
       > (Use the command `man unzip` to open the manpage, then type the forward slash key `/` to search; `/` is also used the hotkey for searching in vim, firefox, and other open source programs.)
       > Use the `tr 'A-Z' 'a-z'` command to translate all characters into lowercase.
       > Use `grep` to extract only the lines containing `coronavirus`.
       > Use `wc` to count the number of lines.
-->

## Homework

Homeworks will generally be posted into the `homework` [git submodule](https://www.atlassian.com/git/tutorials/git-submodule) for each week.
Homeworks are always due on Tuesday of the week after they are assigned (i.e. Jan 24 for this homework).
