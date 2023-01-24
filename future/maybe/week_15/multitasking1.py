def coro1():
    print("coro1 doing some work")
    yield
    print("coro1 doing some work")
    yield

def coro2():
    print("coro2 doing some work")
    yield
    print("coro2 doing some work")
    yield

def scheduler():
    c1 = coro1()
    c2 = coro2()
    c1.send(None)
    c2.send(None)
    c1.send(None)
    c2.send(None)

from collections import deque

def auto_scheduler(coros):
    ready = deque(coros)
    while ready:
        try:
            # take next coroutine that is ready to run
            coro = ready.popleft()
            # run it until the next "yield"
            result = coro.send(None)
            # schedule it for another execution
            ready.append(coro)
        except StopIteration:
            pass
