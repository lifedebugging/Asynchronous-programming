import asyncio

class AsyncConnection:
    """Fake async database connection"""

    async def __aenter__(self):
        print("connecting")
        await asyncio.sleep(1)
        print("connected")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Disconnectiong..")
        await asyncio.sleep(0.5)
        print("Disconnected")

    async def query(self,sql):
        await asyncio.sleep(0.1)
        return f"Resulf of: {sql}"
async def main():
    async with AsyncConnection() as conn:
        result = await conn.query("Select * from users")
        print(result)

await main()
