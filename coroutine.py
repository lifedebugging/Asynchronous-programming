
import asyncio 

async def worker(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")

async def main():
    task1 = worker("Task 1",5)
    task2 = worker("Task 2", 3)
    task3 = worker("Task 3", 1)

    await asyncio.gather(task1, task2, task3)
    
await worker("task2", 4)
