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

**Famous Programmers:**

Linus Torvalds is the 1337est programmer ever.

<img width=100% src=https://zdnet1.cbsistatic.com/hub/i/2020/07/13/7c4051fb-df54-4d6e-8bb6-35b9b48ee872/linustorvaldstedyoutubed.jpg />

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

1. https://www.tutorialspoint.com/unix/shell_scripting.htm

## Lab

**Due Date:**

Labs are always due on midnight of the Sunday of the week that they are assigned (i.e. January 31 for this lab).
If you either attend the class lab session or collaborate with another student by completing the lab together over zoom, then you get a 48 hour extension until the following Tuesday at midnight (i.e. February 2 for this lab).

Weekly homeworks have the same due dates and extension policies.

**Pre-lab work:**

1. Create a GitHub account if you do not already have one.
   Log in, and press the "watch" button at the top of this page.
   Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci143/issues/1).

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

**Instructions:**

1. Log in to the lambda server, and run the command
   ```
   $ typespeed
   ```
   to test your unix typing skills.
   Programmers spend lots of time at the keyboard,
   and so it pays to actually be able to type well.
   Anyone who beats my high score will have my undying admiration :)

1. Follow [these instructions](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/lambda-server.md) to update your lambda server account's settings

1. If you did not take CS46 with me:
    1. Complete the [unix/git tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/git.md)
    1. Complete the [github tutorial](https://github.com/mikeizbicki/cmc-csci046/blob/2021spring/week_00/github.md)
    1. Complete the [unix processes tutorial](processes.md)
    1. Neither of these require you to turn anything in.
       They are simply for you to practice the commands.
       If you're confident that you already know the concepts, then feel free to skim/skip.

1. Complete each of the following exercises.
   Enter your completed answers into sakai.
   (Enter the commands, not the output of the commands.)

    1. Write a 1-line command that counts the number of times the user `mizbicki` is logged in.
       The command should print only a single number and nothing else.

       HINT:
       Use the `finger`, `grep`, and `wc` commands piped together.
       Use the command `man wc` to figure out how to limit `wc`'s output to only the number of lines.

    1. Write a 1-line command that counts the number of zip files contained in the directory `/data/Twitter dataset`.

       HINT:
       Not every file in the directory is a zip file.
       Use the `ls` command to list all the files,
       `grep` to select only the zip files,
       and `wc` to count them.

    1. Count the number of geolocated tweets sent on 2020-12-25 that contain the word "coronavirus".
       The file `/data-fast/twitter2020/geoTwitter20-12-25.zip` contains all geolocated tweets sent on that day.

       My command took 51 seconds to run, and I got 3143 tweets.
       
       HINT:
       Use the `unzip` command to extract the contents of the zip archive;
       you will have to read the man page in order to figure out the correct option to get the output printed on stdout.
       Use the `tr 'A-Z' 'a-z'` command to translate all characters into lowercase.
       Use `grep` to extract only the lines containing `coronavirus`.
       Use `wc` to count the number of lines.

       NOTE:
       The only difference between the file `/data-fast/twitter2020/geoTwitter20-12-25.zip` and `/data/Twitter dataset/geoTwitter20-12-25.zip` is that the former is stored on an NVME drive, whereas the later is stored on an HDD.
