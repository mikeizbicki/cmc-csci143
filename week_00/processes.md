# Lab: shell scripting 

This lab will teach you the shell scripting and command line tools you will need to complete the twitter analysis homework.

<!--
Portions of this lab require you to work with a partner.
So you should pair up with another student.
Both of you should complete the lab on your own computers,
but you will have to run certain commands for your partner on your own computer at different steps.
-->

### Creating a shell script

Create a file in your home folder called `script.sh` with the following contents
```
#!/bin/sh

while true; do
    date
    sleep 1
done
```
This is a simple shell script that will print the current time in an infinite loop.
Run the command 
```
$ ls -l script.sh
```
to check the permissions of this file.
You should get output that looks similar to
```
-rw-r--r-- 1 user user 52 Jan 22 13:16 script.sh
```
The left-hand sequence of `-rw-r--r--` describes the permissions of the file.
This file has read/write permissions for the user (you), and read permissions for everyone else.
For more details on how to read these permission strings, see [this link](https://mason.gmu.edu/~montecin/UNIXpermiss.htm).

<!--
### Hacking your partner's account (pt 1)

By default, everyone has read access to everyone else's home folder.
Change your current working directory to be your partner's home folder by running the command
```
$ cd /home/username
```
but replace `username` with your partner's username.
Run
```
$ ls
```
to see all the files in their home folder.
One of those files should be the `script.sh` file they created in the previous step.

Run
```
$ vim script.sh
```
and try to edit the file.
You should get an error message saying that you don't have permissions to edit the file.

Now, have your partner run
```
$ chmod a+w /home/username/script.sh
```
again, where `username` is replaced by their real username.
Now you have write permission on the file,
and you can edit it in vim.

**TASK:**
Change the permissions of your home folder so that other users cannot read the contents of your files.
Note, you should change the permissions of the folder `/home/username` and not the permissions of each individual file.
This will ensure that any new files you create are also hidden.

**NOTE:**
Essentially all hacking boils down to understanding how a computer system is configured differently than the admin of the computer thinks.
Hackers exploit this misconfiguration to their advantage.
-->

### Running the shell file

<!--
Return to your home folder by running
```
$ cd
```
-->
Now, try to execute your script by running the command
```
$ ./script.sh
```
This should fail with the following error message:
```
bash: ./script.sh: Permission denied
```
That's because we haven't given the file execute permissions yet.

Run the following command to give yourself execute permissions
```
$ chmod u+x script.sh
```
Run the `ls -l` command to verify that your permissions have changed,
and then run the file
```
$ ./script.sh
```
This should print the current date/time every second.
You can end the program by pressing `^C`.
(The `^` symbol is the `CTRL` key on your keyboard.
For Mac users, ensure that you are pressing `CTRL` and not `Command`.)

Note that the `./` is required. 
If you ommit it, then you will get the following error:
```
$ script.sh
bash: script.sh: command not found
```

### Background processes

Now restart the program by running 
```
$ ./script.sh
```
again.
This time, however, press `^Z` to end the process.
This will return you to the command prompt,
but unlike `^C` it does not end the program.
`^Z` temporarily pauses the program,
and you can restart it by running
```
$ fg
``` 
(The `fg` stands for foreground.)
You can pause programs and restart them an arbitrary number of times.

Note that when the process has been paused with `^Z`,
it is not running anymore.
To run the program in the background, enter `bg` (stands for background) instead of `fg`.
Notice that you can still type on the command prompt,
but that `script.sh` is continuing to print out messages while you type.

Press `^C`.
Notice that this does not stop the background process.
To end the process,
first bring it back to the foreground with the command
```
$ fg
```
then press `^C` to terminate the process.

List all the processes running in your current shell with the command 
```
$ ps
```
You should get output that looks like
```
  PID TTY          TIME CMD
12906 pts/8    00:00:00 ps
31170 pts/8    00:00:00 bash
```
although the `PID` values will be different.
Each line corresponds to a process that has been started from your current session.
`bash` is the command interpreter that you are typing commands into,
and `ps` is the command that you just ran.

Later on we'll need more detailed information about the processes,
and you can get this more detailed output by adding the `-f` flag:
```
UID        PID  PPID  C STIME TTY          TIME CMD
user     14694 31170  0 13:52 pts/8    00:00:00 ps -f
user     31170 31166  0 10:24 pts/8    00:00:00 bash
```

Now run `./script.sh`, type `^Z` to pause it, then type `ps` again.
You should now see additional lines in your output, something like:
```
  PID TTY          TIME CMD
12900 pts/8    00:00:00 script.sh
12902 pts/8    00:00:00 sleep
12906 pts/8    00:00:00 ps
31170 pts/8    00:00:00 bash
```
The `script.sh` corresponds to the command you directly executed,
and the `sleep` corresponds to the command that is currently being executed by `script.sh`.
It is possible that instead of the `sleep` command, you will see the `date` command,
depending on where the program stopped.

The process id (pid) is how we communicate with processes.
Every time you start a program, a new process is created.
The `PID` column of `ps`'s output will always be unique,
but the other columns may not be.

### Output redirection

Run the following command in your terminal
```
$ ./script.sh > output
```
You should notice that the program is running, 
but no output is being printed to the screen.
You know the program is running because no prompt (`$`) is printed to the screen,
and you can't enter commands.
The `>` symbol is called output redirection,
and sends all of the output of your program into the `output` file.
(`output` can be replaced with any filename you'd like, and is just an example filename.)

After waiting a few seconds, press `^C` to end the program.
Now open the `output` file in vim
```
$ vim output
```
You should see several lines printed out that contain results of running your `./script.sh` file.

You can run this program in the background by running
```
$ ./script.sh > output
```
and then pressing `^Z` to pause the program and then entering
```
$ bg
```
to run it in the background.
Now, the `output` file is being continually written to.
To verify this:
open the file in vim;
check how many lines have been written;
close the file;
reopen the file in vim;
now there should be more lines in the file.

Alternatively, the command `wc -l` shows how many lines are in a file.
Run the command
```
$ wc -l output
```
then wait a few seconds and run the command again.
You should get different numbers both times.

### Killing processes

We've already seen that we can stop the `./script.sh` command by running the `fg` command and then typing `^C`.
`^C` sends a special signal to a process called `SIGINT`,
and the default response to this signal is to terminate.
Another way to stop the program is by directly killing it with the `kill` command.
`kill` takes a pid as a command line argument,
and you should run 
```
$ kill <PID>
```
where `<PID>` is the pid displayed by the `ps` command of your `./script.sh` process.
Go ahead and kill the process that you currently have running in the background from the previous section.

The `kill` command has many uses for manipulating process.
The most common other variation that you will need to know is `kill -9 <PID>`.
Without the `-9`, `kill` asks the process to "politely" kill itself,
performing a clean shutdown by (for example) saving any open files.
When a program breaks, however, these polite killings sometimes may not happen or may take too long.
Adding the `-9` flag forces the operating system to kill the process immediately without performing a clean shutdown.
This should be done if you tried an ordinary `kill` and it didn't work.

### Multiple connections

Create a second connection to the lambda-server. 
Run the command
```
$ ps
```
in both windows and notice that you get different outputs.
The `ps` command by default outputs only the processes that were created from your current connection.

To list all processes, run the command
```
$ ps -e
```
The `-e` flag causes `ps` to list "every" process on the system.
You should see a very long list that is multiple pages long.

In UNIX systems, we create these more complicated commands by combining simpler commands.
We will combine the `ps` command with the pipe `|` and `grep` command to get the features that we want.
Run the command:
```
$ ps -ef | grep username
```
where `username` is your username.
You should see all the processes created from both of your connected sessions.

The vertical bar `|` is called a pipe.
Pipes connect the output (`stdout`) of the program on the left to the input (`stdin`) of the program on the right.
The `grep` program reads one line at a time from its input and outputs only those lines containing `username`.
To see how this works, run the command
```
$ grep username
```
and start typing some lines.
Notice that if a line does not contain `username` then grep does nothing;
but if the line does contain `username`, then `grep` prints that line.

Thus, when we run the command
```
$ ps -ef | grep username
```
the `ps -ef` prints detailed information about all processes
(the `-e` is every process, and the `-f` prints the usernames and many other aspects of the processes).
Then the `|` passes those results into the `grep` command,
which removes all lines that do not contain your `username` string.

Any program can be combined with any other program using pipes.
The `find` program, for example, lists all files in the current directory and subdirectory.
Run it and you'll see one file per line, with LOTS of lines.
You can find only python files by filtering the output of `find` using `grep` like so:
```
$ find | grep 'py$'
```
(The `$` symbol is a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) matching the end of a line;
grep supports arbitrary regular expressions as input.)

The [UNIX Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) is that programs should "Do one thing and do it well."
Then, programs can be combined together using pipes to generate complex behavior.
For example, the `ps` command lists processes running on a system but doesn't provide any filtering.
We combine `ps` with `grep` to filter the output.
In general, whenever we want to filter a program's output, we always combine the previous program with `grep`;
this simplifies all the programs in unix because they do not need to contain code for filtering within them.
[Chapter 1](http://catb.org/~esr/writings/taoup/html/ch01s06.html) of ESR's famous The Art of Unix Programming goes into details.

Back to our `script.sh` command.
Go ahead and run it in one terminal session:
```
$ ./script.sh
```
then in the other, run our command for listing all of your processes:
```
$ ps -ef | grep username
```
You can see what processes other users are running with the same command.
Just replace `username` with their username instead.


### The `HUP` signal

Another way to kill processes is by sending the `HUP` signal.
The `HUP` signal is automatically sent to all "children" processes of your shell when the connection is closed.
This ensures that you don't accidentally leave thousands of processes running on machines that you're not actively using.

To see how this works,
run the command
```
$ ./script.sh > output2
```
then type `^Z` and run
```
$ bg
```
to send your shell script to the background.
Verify that this program is running in the background by executing the command
```
$ ps -ef | grep username
```
in the OTHER TERMINAL YOU HAVE OPEN.

Next, close the ssh session that you used to run `script.sh` by running the command
```
$ exit
```
In your second ssh session (that is still connected),
again run the command
```
$ ps -ef | grep username
```
and notice that your `script.sh` process is no longer running.
This is because when you closed your ssh connection,
the `HUP` signal was sent to the `script.sh` process,
ending the process.

### Blocking the `HUP` signal

Sometimes, however, we actually do want to have long running processes that last longer than our current sessions.
To do this, we use the `nohup` command to block the `HUP` signal.
(UNIX programmers like simple names :)

Reconnect a second terminal to the lambda server,
and in this terminal run the command
```
$ nohup ./script.sh > output2
```
Notice that the only difference between this command and the previous section is the use of the `nohup` command.
Then type `^Z` and run
```
$ bg
```
to send your shell script to the background.
Verify that this program is running in the background by executing the command
```
$ ps -ef | grep username
```
in the OTHER TERMINAL YOU HAVE OPEN.

Next, close the ssh session that you used to run `script.sh` by running the command
```
$ exit
```
In your second ssh session (that is still connected),
again run the command
```
$ ps -ef | grep username
```
and notice that your `script.sh` process is still running.
Use the `kill` command to end your `script.sh` process.

When you launch long-running processes on the lambda-server,
you will have to use the `nohup` command to ensure that they continue to run after you have disconnected.

<!--
### Hacking your partner (2)

Run
```
$ finger
```
to list all the ssh sessions currently logged in.
Because there is likely to be a lot of users logged into the lambda server right now,
it may be useful to use piping and grep to display only the lines that contain your partner's information:
```
$ finger | grep username
```
This command lists lots of information about each session,
but the important thing for right now is the `Tty` column.

**Historical Note:** `Tty` stands for "teletypewriter", 
which was the original name for a terminal way back in the day when monitors didn't exist and terminal sessions were input on typewriters and output on a printer.
Today, each terminal session has a unique `tty` file.
These are special files located in the `/dev/pts` folder on Linux machines.
By writing to these files, we can write to the different terminals open on the computer;
and by reading from these files, we can read from the different terminals.

Under the `Tty` column of finger's output is a line that looks something like `pts/23`,
(the number `23` will be different for every terminal session).
There is a file in the `/dev/pts` folder that corresponds to your partner's terminal session;
if the finger command shows that their tty is `pts/23`, for example, then the file is `/dev/pts/23`.
Run the following command to write to their terminal:
```
$ write username pts/23
```
Now, whatever you type as input to the write program will be displayed on their terminal.
You have permission to write to their screen because the `/dev/pts/23` file by default gives write permission to everyone in the same group.

In order to prevent someone from writing to your screen,
you need to change the group permissions so that writing is not allowed.
Do this by running
```
$ chmod g-w /dev/pts/23
```
Now, when other people try to write to your screen,
they will get permission denied errors.
-->
