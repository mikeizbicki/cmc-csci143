'''
Explanation of using coroutines for concurrency.
'''

import time
from collections import deque
import heapq

def get_page():
    print("Starting to download page")
    yield ("sleep", 1)
    print("Done downloading page")
    yield "<html>Hello</html>"

def read_db():
    print("Starting to retrieve data from db")
    yield ("sleep", 0.5)
    print("Connected to db")
    yield ("sleep", 1)
    print("Done retrieving data from db")
    yield "db-data"

def scheduler(coros):
    start = time.time()
    ready = deque(coros)
    sleeping = []
    while True:
        if not ready and not sleeping:
            break
            
        # wait for nearest sleeper,
        # if no coro can be executed immediately right now
        if not ready:
            deadline, coro = heapq.heappop(sleeping)
            if deadline > time.time():
                time.sleep(deadline - time.time())
            ready.append(coro)
            
        try:                
            coro = ready.popleft()
            result = coro.send(None)
            # the special case of a coro that wants to be put to sleep
            if len(result) == 2 and result[0] == "sleep":
                deadline = time.time() + result[1]
                heapq.heappush(sleeping, (deadline, coro))
            else:
                print("Got: ", result)
                ready.append(coro)
        except StopIteration:
            pass
	#print(f"Time elapsed: {time.time()-start:.3}s")

'''
Explanation of [PEP 380 - Syntax for Delegating to a Subgenerator](https://peps.python.org/pep-0380/)
(2009)
'''

def worker():
    '''
    This is a natural function to want to write,
    but it won't work with our scheduler.
    '''
    get_page()
    read_db()


def worker():
    '''
    We need to yield the results that were yielded by the function calls.
    '''
    for step in get_page():
        yield step
    for step in read_db():
        yield step


def worker():
    '''
    The "yield from" syntax wraps the for loops above,
    making function calls look more natural.
    '''
    page = yield from get_page()
    yield from read_db()

    # yield from is syntactic sugar for much more than just a for loop;
    # the for loops above only handle the "sending" of information,
    # and ignore the "receiving" of information;
    # for the full desugaring, see: https://peps.python.org/pep-0380/#formal-semantics
