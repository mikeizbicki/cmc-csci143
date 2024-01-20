# Caveat Task: typespeed

**Background:**
[Touch typing](https://en.wikipedia.org/wiki/Touch_typing) is the ability to type on a computer without looking at the keys.
[It is an important, but under-practiced skill for programmers](https://dev.to/davidsanwald/touch-typing-the-most-important-skill-for-developers-nobody-talks-about-3352).

This task gives you practice touch typing using the `typespeed` game,
which is specifically designed for improving your ability to touch type programming idioms.
Programming idioms are often much harder to type than standard English words because they involve weird character combinations (e.g. `fsck` and `tcpdchk`).
The `typespeed` game will train your eyes to read these idioms faster and your fingers to type them correctly.

**Summary:**
You must get a score of at least 400 on the `typespeed` game.

**Extra Credit:**
You can earn extra credit by getting a score of at least 9999.
This will almost certainly require "hacking" the typespeed program somehow,
and the amount of extra credit awarded will depend on the ingenuity of your hack.

## Grading

Scores for the `typespeed` game are stored in the file `/var/games/typespeed.score`.

> **NOTE:**
>
> In general, the contents of the `/var` directory is for information that must be "shared" between multiple users, but "varies" over time.
> Information that is shared but doesn't "vary" over time is commonly stored in the `/usr/share` directory.
> Thus, the wordlists that typespeed uses are stored in the `/usr/share/typespeed/` folder.

You can display the contents of the scores file using the `cat` command like
```
$ cat /var/games/typespeed.score
502 539 92  Mike Izbicki    words.unix  default 12386   1642543157
521 573 92  Mike Izbicki    words.unix  default 13608   1642543526
480 516 91  Mike Izbicki    words.unix  default 13813   1642543677
```
Details of the file format are available in the [README](https://github.com/mikeizbicki/typespeed),
but basically it is a TSV (tab separated value, a common alternative to CSV) file where the 1st column is the score and the 4th column is the name of the person who earned that score.

We can get all the scores for a particular user by filtering the output of `cat` with the `grep` command
```
$ cat /var/games/typespeed.score | grep 'Mike Izbicki'
502 539 92  Mike Izbicki    words.unix  default 12386   1642543157
521 573 92  Mike Izbicki    words.unix  default 13608   1642543526
480 516 91  Mike Izbicki    words.unix  default 13813   1642543677
```
Then we can use the `cut` command to extract only the leftmost column;
the `sort` command to order these columns with the largest score at the top;
and the `head` command to extract the first line of the output.
This results in the following command:
```
$ cat /var/games/typespeed.score | grep 'Mike Izbicki' | cut -f1 | sort -nr | head -n1
521
```

## Hacking

An enterprising student might observe that the grade on this assignment is determined only by the contents of the `/var/games/typespeed.score` file,
and try to edit this file directly with a score of `9999`.
Either of the following two commands would accomplish this task:
```
> vim /var/games/typespeed.score
> echo "9999\t0\t0\tMike Izbicki\twords.unix\tdefault\t0\t0" >> /var/games/typespeed.score
```
If you try these commands, however, you'll notice that you don't have permissions to edit this file.
We can verify this by checking the permissions of the file:
```
$ ls -l /var/games/typespeed.score
-rw-rw-r-- 1 root games 237 Jan 18 14:47 /var/games/typespeed.score
```
Here, you can see that the `root` user and `games` group have write permissions,
and everyone else has only read permissions.
You can run the `groups` command to verify that you are not in fact a member of the `games` group,
and so you do not have write permission to this file.

This raises a critical question:
If you don't have write access to the `/var/games/typespeed.score` file,
then how does the `typespeed` command write to this file?

To answer this question,
let's look at the permissions of the `typespeed` executable:
```
$ which typespeed
/usr/games/typespeed

$ ls -l /usr/games/typespeed
-rwxr-sr-x 1 root games 63968 Apr  3  2018 /usr/games/typespeed
```
Notice that the `typespeed` executable has an `s` (instead of an `x` or `-`) in the execute bit for the groups slot.
This `s` stands for [setgid (set group id) bit](https://www.geeksforgeeks.org/setuid-setgid-and-sticky-bits-in-linux-file-permissions/).
Programs with the setgid bit set will be run with the permissions of the corresponding group.
Therefore, this program will run with the permissions of group `games` for all users, and so will be able to write to the `/var/games/typespeed.score` file.

> **NOTE:**
>
> The effect above could also be achieved by setting the setuid bit instead of the setgid bit.
> This would cause the program to run with `root` permissions for all users,
> since the file is owned by `root`.
> But this would be a VERY BAD IDEA.
> If there are any bugs in your program, then a malicious user could exploit those bugs to run arbitrary commands as the `root` user, taking over your whole computer.
> This is a classic exploit that has resulted in [many security breaches](https://attack.mitre.org/techniques/T1548/001/) in the wild.
> In general, we want our programs to run with as few permissions as possible to limit the scope of these attacks.

In order to get the extra credit for this assignment, you'll have to figure out a way to exploit the `typespeed` executable (or some other executable with group `games`) to make the necessary changes to the scores file.
I know of at least one way to do this, but I suspect there are probably more.

## Submission

Modify the command below to output your best score instead of mine.
```
$ cat /var/games/typespeed.score | grep 'Mike Izbicki' | cut -f1 | sort -nr | head -n1
```
Upload the resulting command and its output to sakai.
If the output is at least `400`, then you will pass this task.
