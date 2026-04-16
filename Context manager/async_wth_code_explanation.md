# Explanation of above code

`class AsyncConnection:` creating class name AsyncConnection

-----------------------------------------------------------------------------------------------

```
 async def __aenter__(self):
        print("connecting")
        await asyncio.sleep(1)
        print("connected")
        return self
```

first ``__aenter__`` : **The setup guy**

The `a` stands for async.

**This method runs first, right before you enter the indented code block.**

**Job**: Open the connection, log in, allocate memory.

~ Whatever this method returns(`return self`) is what gets assigned to the variable after `as`.

So, `conn` becomes the `AsyncConnection` object.

----------------------------------------------------------------------------------------------

`__aexit__` : **The cleanup guy**

This method runs last, right after the indented code block finishes.

**Job**: Close the connection, release memory, log off.

**It's important because**: This runs even if your code crashes. If conn.query caused an error, Python still runs __aexit__ to ensure you don't leave the database hanging open.


`(exc_type, exc_val, exc_tb):` **The Arguments**

These are just information about crash.

1. `exc_type`: What kind of error? (e.g., ValueError)
2. `exc_val`: The actual error message.
3. `exc_tb`: Where in the code the error happened.
   
**Note**: In 99% of simple connection managers, you ignore these. You just want to close the connection regardless of whether there was an error or not.

----------------------------------------------------------------------------------------------

```
 async def query(self,sql):
        await asyncio.sleep(0.1)
        return f"Resulf of: {sql}"

```

This is a `query` function with timeout of(0.1) and reutrn the result of : `whatever query with pass to the function`

In our case it is : `("Select * from users")`

----------------------------------------------------------------------------------------------

```
async def main():
    async with AsyncConnection() as conn:
        result = await conn.query("Select * from users")
        print(result)
```

This is `main` function :

`async with AsyncConnection() as conn:` This is our **context manager** with **async** opening connection as *conn*.

# What's happening 
You run the code :

1. It creates the instance of `AsyncConnection` as conn.

2. pauses the `main` function

3. enters the `AsyncConnetion` class inside it is first `__aenter__`

4. Inside `__aenter__` :

    1. print "connecting"
    2. wait 1 second
    3. print "connected"
    4. return `self` - In plain english **"I am giving you... ME."**
    5. Python takes whatever `self` has and puts it into the variable named conn.
    6. Now `conn` is your active connection object

5. python runs the code inside `main`

6. print the result

7. cleanup(automatic) : once the code inside the block is done(or if it crashed), python automatically calls `__aexit__`

8. Inside `__aexit__`:

   1. print "disconnecting"
   2. wait o.5 second
   3. print "disconnected"

**End of explanation**
