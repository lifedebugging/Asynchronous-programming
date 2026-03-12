# Async loop

Asynchronous loops allow you to handle multiple operations without blocking your program. 

I want you to focus on `asyncioloop.py` it's a very basic method for asynchronous looping.
Requires no function of `asyncio` library. 

As usual we start with importing the library:

          import asyncio

```
async def task(n):
    await asyncio.sleep(3)
    print(f"Task {n} completed")
```
This is a simple async function where a task will be created *"n"* times. 

```
async def main():
    for i in range(5):
        await task(i)
```
# How it works: 
The await task(i) line tells the program: "Pause here and wait for this specific task to finish before moving to the next iteration of the loop."

Because each task takes 3 seconds, and we are doing 5 of them one-by-one, the total time will be 15 seconds. This is technically "**asynchronous**," but it isn't "**concurrent**."

Output : 

            #As you run the funciton.
            #3 seconds after
            Task 0 completed
            #again after 3 seconds
            Task 1 complete
            .
            .
            Task 4 completed


# Gather for async loop



```
async def main():
    tasks = [task(i) for i in range(5)]
    await asyncio.gather(*tasks)
```
What `.gather()` does it takes multiple awaitables(like coroutines, futures and tasks) and schedules
them to be run concurrently. When all of  tem complete **gather()** returns a list of their results in the same 
order as the input tasks.

In this version, the program starts all 5 tasks simultaneously. After 3 seconds, all 5 tasks will finish almost at once.

                 asyncio.gather(*tasks)
The `*` is  the argument unpacking operator also called the "splat" operator.

It's the wat **gather()** makes sure each element is separated and become it's own argument.

Example without unpacking(wrong for multiple tasks):

          import asyncio
          async def foo(n):
               await asyncio.sleep(1)
          return n
 
          tasks = [foo(1), foo(2), foo(3)]

 ** This passes a single list argument, not three separate coroutines **   

       TypeError: An asyncio.Future, a coroutine or an awaitable is required

  Hence, without it, gather() would see one argument (the list), not multiple tasks.

# Environment Tip

If you are running this code in VS Code or a standard .py file, use:

`asyncio.run(main())`

If you are using Jupyter Notebooks or IPython, the event loop is already running, so you just use:

`await main()`
