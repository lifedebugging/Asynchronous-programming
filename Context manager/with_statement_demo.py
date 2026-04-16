f = open(r"file.txt", "r")
print(f.closed)   # False — still open

f.close()
print(f.closed)   # True — now closed

# With 'with':
with open(r"D:\Documents\ai_basics.txt", "r") as f:
    print(f.closed)  # False — inside, still open

print(f.closed)  # True — outside, auto closed 
