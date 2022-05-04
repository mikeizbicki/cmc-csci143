import asyncio

async def worker(i):
    print(f'worker({i}): hello')
    await asyncio.sleep(1)
    print(f'worker({i}): world')
    return i*2

async def main():
    workers = []
    for i in range(10):
        workers.append(worker(i))
    return await asyncio.gather(*workers)

loop = asyncio.new_event_loop()
xs = loop.run_until_complete(main())
print(f"xs={xs}")
loop.close()

