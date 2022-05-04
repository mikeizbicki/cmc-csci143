import asyncio
import time

def worker(i):
    print(f'worker({i}): hello')
    time.sleep(1)
    print(f'worker({i}): world')
    return i*2

def main():
    xs = []
    for i in range(10):
        xs.append(worker(i))
    return xs

xs = main()
print(f"xs={xs}")
