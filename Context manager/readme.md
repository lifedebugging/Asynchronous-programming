# Context manager

Think of it as an event manager, it's job is to see through the function, from very start to the end making sure whatever happens event get through.
Whether the event gonna get successful or something happens like neighbours getting ~heart attack~ hope not. Even manager will make sure they still wrap up the event.

That's exactly what context manager is it's just "**A wrapper that handles setup and cleanup**".

# Why do we need it?

Well in techincal terms : **T prevent resource leaks**

# Examples 

To understand what that means let's look at the examples:

```
#without `with`
f = open(r"D:\Documents\ai_basics.txt", "r")
text = f.read()
# you forget to close... or an error happens here 
print(undefined_variable) # crashes!
f.close()  # ← this NEVER runs
```

Here, if this was a very big file, it would be eating my memory and crashing my whole system because the `f.read()` is still open.

```
#with `with`
with open(r"D:\Documents\ai_basics.txt", "r") as f:
    text = f.read()
    print(undefined_variable)# crashes too!
# but f.close() runs AUTOMATICALLY even after the crash ✅
```

Here, `f.close()` will close regardless the program will crash or not.

See? Just like our **event manager** they will wrap up the wedding and clean up, making sure everything is closed and safe whether the wedding crashes or not.

To fully undersand the `with` statement need, run this piece of code.

