import asyncio

async def fetch(url, delay):
    asyncio.sleep(delay)
    return f"Response from {url}"

async def main():
    urls = ["site1.com", "site2.com", "site3.com"]
    coros = [fetch(url, i * 1) for i, url in enumerate(urls)]

    results = await asyncio.gather(*coros)
    for r in results:
        print(r)

await main()
