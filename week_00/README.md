# Week 00: The Unix Shell

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src=dilbert.gif />
</a>
</center>

## Lecture

We will cover the basics of using the unix command line shell effectively.
This includes:

1. basic shell scripting
1. piping / output redirection
1. file permissions
1. environment variables
1. signals
1. processes

Pre-lecture reading/videos:

1. [Ken Thompson and Dennis Ritchie Explain UNIX](https://www.youtube.com/watch?v=JoVQTPbD6UY)

1. (optional) [Where GREP Came From - Computerphile](https://www.youtube.com/watch?v=NTfOnGZUZDk)

1. (optional) [vim vs emacs: the oldest rivalry in computing](https://slate.com/technology/2014/05/oldest-software-rivalry-emacs-and-vi-two-text-editors-used-by-programmers.html)

**References:**

1. https://www.tutorialspoint.com/unix/shell_scripting.htm

## Lab

Pre-lab work:

1. Create a GitHub account if you do not already have one.
   Log in, and press the "watch" button at the top of this page.
   Read and follow the instructions in Issue #1: the meet and greet thread.

1. Log in to the lambda server.
   Run the command
   ```
   $ vimtutor
   ```
   Complete all instructions in order to learn vim.
   This should take 30-60 minutes.

1. (Optional)
   Play the https://vim-adventures.com game to learn vim while playing a game.
   The first 3 levels are free, but you have to pay to continue playing the game.

1. (Optional)
   Run the command
   ```
   $ typespeed
   ```
   to test your unix typing skills.
   Programmers spend lots of time at the keyboard,
   and so it pays to actually be able to type well.

Instructions:

1. Follow [these instructions](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/lambda-server.md) to update your lambda server account's settings

1. If you did not take CS46 with me:
    1. Complete the [unix/git tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/git.md)
    1. Complete the [unix processes tutorial](processes.md)

1. Complete each of the following exercises.
   Enter your completed answers into sakai.
   (Enter the commands, not the output of the commands.)

    1. Write a 1-line command that counts the number of times the user `mizbicki` is logged in.
       The command should print only a single number and nothing else.

       Hint:
       Use the `finger`, `grep`, and `wc` commands piped together.
       Use the command `man wc` to figure out how to limit `wc`'s output to only the number of lines.

    1. Count the number of zip files contained in the directory `/data/Twitter dataset`.
       Note that not every file in the directory is a zip file.

    1. Count the number of tweets sent on 2020-11-01 that contain the word "coronavirus".

       HINT:
       Use the `unzip` command to extract the contents of the zip archive;
       you will have to read the man page in order to figure out the correct option to get the output printed on stdout.
       Use the `tr 'A-Z' 'a-z'` command to translate all characters into lowercase.
       Use `grep` to extract only the lines containing `coronavirus`.
       Use `wc` to count the number of lines.
