import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    # Create tasks - they start running immediately
    task1 = asyncio.create_task(fetch("A", 2))
    task2 = asyncio.create_task(fetch("B", 1))

    # Wait for both to complete
    result1 = await task1
    result2 = await task2
    print(result1, result2)

asyncio.run(main())
