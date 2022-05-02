'''
`asyncio` is python's standard library for working with async functions
'''

from asyncio import sleep

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

