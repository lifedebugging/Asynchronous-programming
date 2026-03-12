import asyncio
async def task(n):
    await asyncio.sleep(3)
    print(f"Task {n} completed")

async def main():
    for i in range(5):
        await task(i)

await main()
