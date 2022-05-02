# Coroutines and Async Programming in Python

## Background

The problem:

1. IO (Input/Output) is slow

    Examples:

    1. Reading a file

    1. Network access

1. Traditional IO operations "block" the CPU from doing work

Solution:

1. Asynchronous programming

Techniques:

1. Threads

1. Callbacks

1. Promises

1. ... many more ...

We will use: Coroutines

1. Recall that "routine" is a synonym for "function"

    The "co" stands for "cooperative", and so "coroutines" are functions that cooperate with each other

1. Currently most popular technique

1. Most computationally efficient

1. "Easiest" to use

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

        1. Django

        1. Flask

    1. ASGI - Asynchronous Server Gateway Interface)
        
        1. [FastAPI](https://fastapi.tiangolo.com/)

    1. [Performance comparison](https://www.techempower.com/benchmarks/#section=test&runid=a979de55-980d-4721-a46f-77298b3f3923&hw=ph&test=plaintext&l=v2qiv3-e7&a=2&f=zik0zj-qmx0qn-zhxjwf-zik0zi-zik0zj-zik0zj-zik0zj-zik0zj-zik0zj-zik0zj-zik0zj-1kv)

1. Database access:

    1. SqlAlechemy 1.4 (latest version) introduced [Beta support for async operations](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)

    1. Psycopg3 [introduces async support](https://www.psycopg.org/psycopg3/docs/advanced/async.html#async)

        (By default, sqlalchemy still uses psycopg2 as the backend)

        History of the name: <https://www.postgresql.org/message-id/flat/CA%2BRjkXFL6Jy7actUy%2BS%3DdGfjpuD_jpUYYofGpON%2B1Nq9S2Y75w%40mail.gmail.com#f9771ec89bf350e0594cf9640a1f912c>

        > Like always, the name was a joke, and a badly worded one. At the time, all PostgreSQL Python drivers were pure s**t and my company gave to two interns the job to write a new driver. They produced s**t^2 by writing first a server that connected to PostgreSQL using libpq and then a Python client that was supposed to connect to the server and pass through it all the SQL for the backend. After a couple of month the a whole thing still didn't work: the worse bug was that for apparently no reason it opened connections to the backend like _crazy_.
        >
        > So, in about a weekend I wrote the core of psycopg 1, just to demonstrate that you can write something that works without over-engineering it. **I wanted to call it psychopg (a reference to their psychotic driver) but I typed the name wrong.**
        >
        > **And the name just stuck.**
        >
        > To be honest, we later decided that the name was ok, given that, at the time, psycopg was the only driver able to support multi-threaded Python applications without dying an horrible death. Something along the lines that the driver should be a bit "psycho" to manage all the threads. Or something like that.

## The Syntax

References:

1. <https://mleue.com/posts/yield-to-async-await/>

    "Under the hood" details

1. <https://realpython.com/async-io-python/>

    More "applied"

## Concurrent Web Requests

1. aiohttp library: 

    1. <https://docs.aiohttp.org/en/stable/>

    1. Examples all use docker/postgres or (mongo or redis)

        <https://aiohttp-demos.readthedocs.io/en/latest/index.html#aiohttp-demos-polls-beginning>
