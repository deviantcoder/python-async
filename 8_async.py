import requests
from time import time
from random import randint

# ***** 1 - sync pics downloader *****

def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = str(randint(1, 100)) + response.url.split('/')[-1]

    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    count = 0
    for i in range(10):
        write_file(get_file(url))
        count += 1

    print(time() - t0)
    print('Files downloaded: {}'.format(count))


# if __name__ == '__main__':
#     main()

# ***********

# ***** 2 - async pics downloader *****

import asyncio
import aiohttp


def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))

    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    url = 'https://loremflickr.com/320/240'

    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)