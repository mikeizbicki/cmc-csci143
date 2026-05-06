# Last day of class!

Announcements:

1. Quizzes will be graded in canvas by end of day

1. I will be in my office most of the day Thurs/Fri this week
    1. if you want to guarantee my availability, post a github issue

1. Graduating students: everything must be submitted before Friday morning 9AM

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>


## Class Takeaways

**Good habits make good programmers.**

1. Use tools effectively

    <img src=img/vim.jpg width=300px />

    1. This class highly opinionated:
        1. vim
        1. command line / shell

    1. Other tools okay, but only if you **master** them

    1. You WILL BE JUDGED by how you use your tools

        > **Corollary:**
        > If you compliment people's tool use, they will like you :)

    <img src=img/gates.jpg width=400px />
    <br/>
    <img src=img/the-three-chief-virtues-of-a-programmer-are-laziness-impatience-and-hubris-larry-wall.jpg width=400px />

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

1. Use git in *everything*

    <img src=img/git.jpg width=300px />

    1. always run `git init` before you start a project

        always run `git add` and `git commit` before leaving your computer

    1. setup continuous integration

    1. don't upload credentials though

    1. **MORE EXTRACREDIT:**
        
        For each game below you complete, I will give +2 points of extra credit.

        1. <https://github.com/git-game/git-game>
        1. <https://github.com/git-game/git-game-v2>

1. Use docker in *almost* everything.
    1. reproducibility! reproducibility! reproducibility!

        <img src=img/works-on-my-machine.jpeg width=300px />

    1. "real" programmers mess up docker

        <img src=img/headache.jpg width=300px />

        1. (2025) Deepseek: [Internal database exposed due to bad port management](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak)
        1. (2018) Tesla: [Hackers hijack Tesla’s cloud system to mine cryptocurrency](https://www.cnbc.com/2018/02/21/hackers-hijack-teslas-cloud-system-to-mine-cryptocurrency-redlock.html)
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

1. Use lindy software

    <img src=img/lindy.png width=300px />

    Examples: shell (POSIX/bash/zsh/dash), SQL

    Goal for sqlite3: Remain relavent past 2050.

    Why?

    1. Whatever you learn will still be valuable throughout your whole career.
    1. AI will have good answers for you.
    1. These tools much more powerful than 1-off custom big data tools.

        (And they're free!)

        <img src=img/bash-meme.jpg width=300px />

        <br/>

        <img src=img/sql-meme.png width=300px />

    **BIG TAKEAWAY:**

    If you are ever tempted to store something in a file,
    you should probably store it in a sqlite3 database instead.

    <img src=img/sqlite-meme.jpg width=300px />

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

1. Don't break backwards compatibility

    <img src=img/lego.jpg width=300px />

    1. intentional breaking changes are a sign of evil:

        `docker-compose` vs `docker compose`

        `master` vs `main` <https://github.com/mikeizbicki/cmc-csci143/issues/750>

    1. unintentional breaking changes are a sign of incompentence:

        1. version control your versions

            ```
            $ pip3 freeze > requirements.txt
            $ git add requirements
            $ git commit
            ```

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

Please fill out course surveys :)

Specifics about the following particularly useful:
- the most interesting/fun/boring/hard/etc assignments
- the best sources of help you found (AI/QCL/classmates/office hours/etc)
- ways to adapt the course for AI
