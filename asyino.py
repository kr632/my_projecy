# without_gather

import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")

async def main():
    await task1()
    await task2()

asyncio.run(main())


# with asyncio.gather

import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())


