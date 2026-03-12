# Async loop

Async loop allow you to iterate over a **task** without blocking the I/O

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

        asyncio.sleep()
Allow us to use one of the common function of **asyncio**. What it does is makes the 
function sleep/wait for given amount of time. In our case it's **3 seconds**.


```
async def main():
    for i in range(5):
        await task(i)
```
This is our **main()** function that has a for loop given a **range** of 5 means
the task will iterate over 5 times. Followed by :

           await task(i)
This is similar to saying : "**pause the execution of function until tge awaited task is completed**".
In our case it will make the task wait 3 seconds.

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

It's the same function the only difference is we're using **gather** here.

What `.gather()` does it takes multiple awaitables(like coroutines, futures and tasks) and schedules
them to be run concurrently. When all of  tem complete **gather()** returns a list of their results in the same 
order as the input tasks.

If you pass an coroutine to **gather()** it  will automatically wraps it into a **task**.

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

  Note : If you running the code in VS code or similar IDE. You muse use `asyncio.run((main))`.
  The `await main()` is the way to run asynchronous code in **Jupyter**.
  
