# Topic 00: Unix Background

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src=img/dilbert.gif />
</a>
</center>

## Lecture Notes

**Expected Background Knowledge:**

General knowledge:
1. python
1. regular expressions
1. shell scripting
1. git version control system
1. github actions

SQL knowledge:
1. `SELECT`
1. `GROUP BY`
1. `WHERE`
1. `count()`
1. `count(distinct)`

If you're not confident in all of this material, that's okay.
We will spend the first 2 weeks reviewing.
We will also see how SQL relates to python/shell/git.

<!--
**Working Environment:**

All of our work in this class will be done on the lambda server.
(You should have received an email with login credentials.)
The lambda server has:
1. 80 processors
1. 8 GPU
1. 256 GB RAM
1. 2 TB NVME mounted on `/` (you have 10GB of space)
1. 50 TB RAID array of 16 HDDs mounted on `/data` (you have 250GB of space)

<center>
<img width='500px' src=../img/big-data-map.png />
</center>

We will use docker and docker-compose to manage our own "virtual cloud infrastructure" from the lambda server.

<img src=img/map_of_cs.png width=600px>
-->

**Vim**

All text editing must be done in Vim.
We will encounter many instances in this class where more familiar tools like VSCode and Jupyter Notebooks will not work.

<img src=img/vim-productivity.jpg width=500px>

<!--
<img src=img/vim-comic2.webp width=500px>

<img src=img/vim-comic.jpg width=500px>
-->


**Cheat sheets:**

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [Vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)

<!--
1. [github pull requests](img/pull_request.png)
1. [sql](img/SQL_Basics_For_Data_Science.pdf)
-->

**Quiz details:**

1. There will be a quiz every Wednesday.
1. Your first quiz is next week on Wednesday 9 Sep.
1. The quiz will cover:
    1. <https://github.com/mikeizbicki/quiz/blob/master/quiz_shell/topic00_intro.pdf>
    1. <https://github.com/mikeizbicki/quiz/blob/master/quiz_shell.old/topic01_variables.pdf>
    1. <https://github.com/mikeizbicki/quiz/blob/master/quiz_shell.old/topic02_environment_variables.pdf>
1. All quizzes are open note.
    I strongly encourage you to complete all of the practice quiz problems and take notes on the practice sheets of paper.

## Lab

**Due Date:**

Motivated students should be able to complete them within the allocated time on Friday.

Labs are always due on midnight of the Sunday of the week that they are assigned (e.g. Sep 6 for this lab).

*For this lab only: There will be no late penalty if you miss the due date, but please be reasonable.

**Pre-lab work:**

1. Create a GitHub account if you do not already have one.

1. Press the watch button on both this repo and <https://github.com/mikeizbicki/about-me>.
    This will ensure you get email notifications whenever a new issue is posted to github.
    All class related communications will happen through github,
    and not through email or canvas.

1. Create a [personal access token (PAT)](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for your github account, and save the PAT to a file for future use.

1. Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci143/issues/573).

1. Log in to the lambda server and run the command
   ```
   $ vimtutor
   ```
   Complete all instructions in order to learn Vim.
   This should take 30-60 minutes.

1. Complete the [github pull request tutorial](https://github.com/mikeizbicki/pullrequest-tutorial)

1. Follow [these instructions](https://github.com/mikeizbicki/cmc-csci046/blob/2023spring/topic_00_unix/lambda-server.md) to update your lambda server account's settings.

1. Follow [these instructions](https://github.com/mikeizbicki/lab-llm) to get a nice terminal interface to LLMs on the lambda server.

1. (Optional) Watch a short video where the creators of UNIX Ken Thompson and Dennis Ritchie explain the UNIX philosophy.

**Instructions:**

TBA
<!--
1. First, visit the [lab-messages](https://github.com/mikeizbicki/messages) repo and complete the instructions in the README.

1. Then complete [lab-goodreads](https://github.com/mikeizbicki/lab-goodreads) and [lab-goodreads-part2](https://github.com/mikeizbicki/lab-goodreads2).
    (It's really just 1 lab split into two submodules for organization.)
-->

## Homework

**Due Date:**

Homeworks are always due at 11:59pm on the Tuesday of the week after they are assigned (i.e. 8 Sep at 11:59pm for this homework).

*For this hw only:*
I will not apply a late penalty, but please be reasonable.

**Instructions:**

<!--
This week's homework will teach you how to use continuous integration,
and prepare you to submit all future assignments.
You can find the homework at <https://github.com/mikeizbicki/continuous-integration>.
-->
