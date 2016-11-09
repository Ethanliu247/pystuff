# Okay Miles, so today you will be learning about generators
# Generators are special functions that return a different value every time
def gen(n):
    yield n + 1
# Okay, so first of all, you will notice that there is a special keyword: yield
# Yield is like return, except it works in a special way
generator = gen(0)
# This creates a generator object, which starts at zero
n = next(generator)
print(n)
# This is where the magic happens
# When you call next(generator), the special return (yield) increases n by 1

# If you don't understand, I suggest you run this code and play with the yield

def gen(n):
    yield n * 5

g = gen(2)
n = next(g)
print(n)

# This will 'yield' 2*5... 10
# Now, you cannot do this multiple times unless you do this
def gen(n):
    while True:
        yield n * 5
        n += 1
        # You have to incerment n by an amount every time for different values
g = gen(2)
for i in range(5):
    n = next(g)
    print(n)

# This will increment the yield by 5 for every call

# Generators are very useful!
