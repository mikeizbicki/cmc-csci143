'''
Explanation of [PEP492 - Coroutines with async and await syntax](https://peps.python.org/pep-0492/)
(2015)

Changes:
1. All coroutines defined with the "async def" keyword.
2. Results extracted using the "await" syntax.
'''

import time
from collections import deque
import heapq

async def get_page():
    print("Starting to download page")
    await sleep(1)
    print("Done downloading page")
    return "<html>Hello</html>"

async def write_db(data):
    print("Starting to write data to db")
    await sleep(0.5)
    print("Connected to db")
    await sleep(1)
    print("Done writing data to db")

async def worker():
    page = await get_page()
    await write_db(page)

class Sleep:
    def __init__(self, delay):
        self.delay = delay
        
    def __await__(self):
        yield ("sleep", self.delay)

def sleep(delay):
    return Sleep(delay)

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

