import asyncio

async def fetch (name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    task1 = asyncio.create_task(fetch("a", 3))
    task2 = asyncio.create_task(fetch("b", 1))
    #.create_task is a function of asyncio to create task

    result1 = await task1
    result2 = await task2
    print(result1 ,"\n", result2)

await main()
