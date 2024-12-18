# Event Loop:
#     coroutine > Task(Future)

import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    pass


async def main():
    pass


if __name__ == '__main__':
    main()