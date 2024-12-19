import asyncio
import time
import requests
import aiohttp


async def blocking():
    resp = requests.get('https://github.com')
    print(resp.status_code)


async def async_http():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://github.com') as resp:
            print(resp.status)


async def one():
    print('Start one')
    await asyncio.sleep(1)
    print('Stop one')

async def two():
    print('Start two')
    # await asyncio.sleep(2)
    time.sleep(5)
    print('Stop two')

async def three():
    print('Start three')
    await asyncio.sleep(3)
    print('Stop three')

async def main():
    # asyncio.create_task(one())
    # asyncio.create_task(two())
    # await asyncio.create_task(three())

    # await asyncio.gather(*(blocking() for _ in range(5)))
    await asyncio.gather(*(async_http() for _ in range(5)))

if __name__ == '__main__':
    start = time.time()

    asyncio.run(main())

    print(time.time() - start)