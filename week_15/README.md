# Coroutines and Async Programming in Python

<img src=blocking-calls.jpg width=400px />

### Background

The problem:

1. IO (Input/Output) is slow

    Examples:

    1. Reading a file

    1. Network access

1. Traditional IO operations "block" the CPU from doing work

    <img src=IOBound.webp height=200px />

Solution:

1. Asynchronous programming

    <img src=Asyncio.webp height=200px />

Techniques:

1. Threads

1. Callbacks

1. Promises

1. ... many more ...

We will use: Coroutines (i.e. `async` / `await` syntax)

1. Recall that "routine" is a synonym for "function"

    The "co" stands for "cooperative", and so "coroutines" are functions that cooperate with each other

1. Currently most popular technique

1. Computationally efficient

1. "Easy" to use compared to other techniques

    <img src=yoda.jpeg width=400px />

History:

1. Syntax has changed considerably since first introduced in python,
    and only "stabalized" in Python 3.5 (2015)

    - Every python version since then has still introduced minor changes

1. [History of Coroutine PEPs](https://en.wikipedia.org/wiki/Coroutine#Python)

1. [Async/await history](https://en.wikipedia.org/wiki/Async/await#History)

<!--
[PEP 342 - Coroutines via Enhanced Generators](https://peps.python.org/pep-0342/)

[PEP 492 – Coroutines with async and await syntax](https://peps.python.org/pep-0492/)
-->

<!--
Python keywords:

1. `async`

1. `async with`

1. `async for`

1. `await`
-->

Applications:

1. Web frameworks:

    1. WSGI - Web Server Gateway Interface (pronounced like Whiskey)

        [PEP333 - Python Web Server Gateway Interface v1.0](https://peps.python.org/pep-0333/) (2003)

        1. Django

        1. Flask

    1. ASGI - Asynchronous Server Gateway Interface

        [No PEP](https://mail.python.org/pipermail/python-ideas/2018-October/054341.html), just a [github repo](https://asgi.readthedocs.io/en/latest/) - [first commit](https://github.com/django/asgiref/commit/8d186763a67c4a1a9a4eb14a7e5917facaa1be5f) Dec 2015
        
        1. [FastAPI](https://fastapi.tiangolo.com/) - [first commit](https://github.com/tiangolo/fastapi/commit/406c092a3bf65bbd4405ce87611a7e0b9c0ae706) - Dec 2018

    1. [Performance comparison](https://www.techempower.com/benchmarks/#section=test&runid=a979de55-980d-4721-a46f-77298b3f3923&hw=ph&test=plaintext&l=v2qiv3-e7&a=2&f=zik0zj-qmx0qn-zhxjwf-zik0zi-zik0zj-zik0zj-zik0zj-zik0zj-zik0zj-zik0zj-zik0zj-1kv)

    <!-- <img src=wsgi-asgi.jpeg width=400px /> -->

1. Database access:

    1. SqlAlechemy 1.4 (latest version) introduced [Beta support for async operations](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)

    1. Psycopg3 [introduces async support](https://www.psycopg.org/psycopg3/docs/advanced/async.html#async)

        First stable release was this year

        By default, sqlalchemy still uses psycopg2 as the backend

        History of the name, [from the postgres mailing list](https://www.postgresql.org/message-id/flat/CA%2BRjkXFL6Jy7actUy%2BS%3DdGfjpuD_jpUYYofGpON%2B1Nq9S2Y75w%40mail.gmail.com#f9771ec89bf350e0594cf9640a1f912c):

        > I wanted to call it psychopg but I typed the name wrong.  And the name just stuck.

**Takeaway:**

1. Async makes io code faster

1. Not everything is async yet, but everything will be async in the future

### The Syntax

References:

1. <https://mleue.com/posts/yield-to-async-await/>

    "Under the hood" details

1. <https://realpython.com/async-io-python/>

    More "applied"

<!--
1. <https://hynek.me/articles/waiting-in-asyncio/>

    How to make things concurrent vs sequential

1. <https://www.roguelynn.com/words/asyncio-we-did-it-wrong/>

    `asyncio` use at spotify, with lots of examples/pycon videos
-->

### Concurrent Web Requests

1. aiohttp library: 

    1. <https://docs.aiohttp.org/en/stable/>

    1. Examples all use docker/postgres or (mongo or redis)

        <https://aiohttp-demos.readthedocs.io/en/latest/index.html#aiohttp-demos-polls-beginning>

## Homework

Part 1: generator syntax practice (10pts)

1. Fork/fix the [containers repo](https://github.com/mikeizbicki/containers) so that all test cases pass

    Submit the completed repo to sakai

1. This is an assignment from CS46 (data structures), and so only students who didn't take that with me need to complete it

Part 2: wardial (20pts)

Both assignments will be due Wednesday, May 11.
