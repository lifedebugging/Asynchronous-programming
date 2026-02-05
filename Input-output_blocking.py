import asyncio
from concurrent.futures import ThreadPoolExecutor

async def read_file(path):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        with open(path) as f:
            return await loop.run_in_executor(pool, f.read)

await (read_file(f'Desktop/requirements.txt'))

#change the file path as per you computer file
#Note that a folder doesn't work it only works in file.
