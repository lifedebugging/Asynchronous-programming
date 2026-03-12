import asyncio
async def task(n):
    await asyncio.sleep(3)
    print(f" task {n} completed")

async def main():
    tasks = [task(i) for i in range(5)]
    await asyncio.gather(*tasks)

await main()
