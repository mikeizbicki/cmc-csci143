# Topic 00: Course Overview

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src=img/dilbert.gif />
</a>
</center>

## Lecture Notes

**Expected Background Knowledge:**

General knowledge:
1. basic python
1. basic shell scripting
1. git version control system
1. continuous integration with github actions

SQL knowledge:
1. `SELECT`
1. `GROUP BY`
1. `WHERE`
1. `count()`
1. `count(distinct)`

If you're not confident in all of this material, that's okay.
We will spend the first 2 weeks reviewing.
We will also see how SQL relates to python/shell/git. 

<img src=img/map_of_cs.png width=600px>

**Working Environment:**

All of our work in this class will be done on the lambda server.
(You should have received an email with login credentials.)
The lambda server has:
1. 80 processors
1. 8 GPU
1. 256 GB RAM
1. 2 TB NVME
1. 50 TB RAID array of 16 HDDs

All text editing must be done in vim.

**Cheat sheets:**

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)
1. [github pull requests](pull_request.png)

**Quiz details:**

1. There will be a quiz (almost) every Thursday.
    1. No quiz this week.  Your first quiz is next week on Thursday 24 Jan.
1. All quizzes are open note.
1. The format follows the `practice_quiz_X.pdf` files.

## Background Work

## Lab

**Due Date:**

Labs are always due on midnight of the Sunday of the week that they are assigned (i.e. January 21 for this lab).

**Background Work:**

1. Log in to the lambda server and run the command
   ```
   $ vimtutor
   ```
   Complete all instructions in order to learn vim.
   This should take 30-60 minutes.

   Vim is famous for having a steep learning curve,
   and has inspired lots of memes/comics:

   <img src=img/vim-productivity.jpg width=500px>

   <img src=img/vim-comic2.webp width=500px>

   <img src=img/vim-comic.jpg width=500px>

1. Complete the [unix/git tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2023spring/topic_00_unix/git.md).

**Pre-lab work:**

You should be able to complete the following tasks without any problems.

1. Create a GitHub account if you do not already have one.

1. Press the "watch" button at the top of this page.
    This will ensure you get email notifications whenever a new issue is posted to github.
    All class related communications will happen through github,
    and not through email or sakai.

1. Create a [personal access token (PAT)](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for your github account, and save the PAT to a file for future use.
    The default level of permissions is okay.

1. Follow [these instructions](https://github.com/mikeizbicki/cmc-csci046/blob/2023spring/topic_00_unix/lambda-server.md) to update your lambda server account's settings.

1. Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci143/issues/226).

Depending on you background knowledge, you may not (yet) be able to complete the following task.

1. Complete the [github pull request assignment](https://github.com/mikeizbicki/cmc-csci046/blob/2023spring/topic_00_unix/github.md)

<!--
On Monday, we will go over how to complete the following task.
You're welcome to get started on it now if you're already familiar with github pull requests, but you don't have to.
-->

<!--
1. Read/watch the following articles/videos:

    1. [Ken Thompson and Dennis Ritchie Explain UNIX](https://www.youtube.com/watch?v=JoVQTPbD6UY)
    1. (optional) [Where GREP Came From - Computerphile](https://www.youtube.com/watch?v=NTfOnGZUZDk)
    1. (optional) [vim vs emacs: the oldest rivalry in computing](https://slate.com/technology/2014/05/oldest-software-rivalry-emacs-and-vi-two-text-editors-used-by-programmers.html)

    1. (optional) Corey Schafer's [Git Tutorial for Beginners: Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4).
       Corey is a really famous youtuber for programming tutorials, and you can watch his other videos too if you need more background.
       -->
       
**Instructions:**

If you don't yet have access to the lambda server,
let me know and we'll get that resolved.

1. Visit the [messages](https://github.com/mikeizbicki/messages) repo and complete the instructions in the README.

1. [Goodreads]

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

## Homework

Homeworks will generally be posted into the `homework` [git submodule](https://www.atlassian.com/git/tutorials/git-submodule) for each week.
Homeworks are always due on Tuesday of the week after they are assigned (i.e. Jan 24 for this homework).
