# Welcome to Tutorial 9!
# This covers another useful function tool, but I moved it over here because it is complex and profound

# Finally, decorators!
# This may confuse you quite a bit, it confused me very much at first
# Decorators utilize wrappers (which we talked a bit about earlier) and look something like closures
# Let's make a basic one to start
def p_tag_decorator(func):
    def wrapper():
        return '<p> {0} </p>'.format(func()) # The <p> tags are HTML, they are used for example here
    return wrapper
# What's interesting is that at the end, we return the wrapper object
f = lambda: 'some text'
thing = p_tag_decorator(f)
# So we give the object over to a variable
print(thing())
# And call it like a function, printing what's returned
# Yay!

# There is a simpler way of doing this though
@p_tag_decorator # This basically takes the function that is defined and passes it as the decorator's argument
def f():
    return 'some text'
print(f()) # Print what it returns
# Both of these methods should print '<p> some text </p>
# Note that this method must be used right before defining a function; not when calling, not using lambda.

# Now that we know what we're doing, let's chain some together!

def strong_tag_decorator(func):
    def wrapper():
        return '<strong> {0} </strong>'.format(func())
    return wrapper

@p_tag_decorator
@strong_tag_decorator
def f():
    return 'decorated stuff!'

print(f())
# We get what we expected!

# Now, there will be a small problem when we try this inside of classes
class Thing:
    def __init__(self):
        pass
    @p_tag_decorator
    def doStuff(self): # See the self? That's the problem
        return 'stuff got done'
# When creating the wrapper(), we would need to add self as a parameter and inside the func() call
def p_tag_decorator(func):
    def wrapper(self): # Self
        return '<p> {0} </p>'.format(func(self)) # Self
    return wrapper

# So, I am going to teach you a very useful thing
def p_tag_decorator(func):
    def wrapper(*args, **kwargs):
        return '<p> {0} </p>'.format(func(*args, **kwargs))
    return wrapper

# Ta da! It worked!
# The *args parameter accepts any number of arguments, and **kwargs accepts any number of keyword arguments!
# This lets us pass self optionally, along with any other arguments

# There is one more thing to mention
# You can have arguments for the decorators

del p_tag_decorator, Thing, strong_tag_decorator
# Cleaning up

# This is going to look strange
def tags(name):
    def decorator(func):
        def wrapper(*args, **kwargs): # So that we can use it in classes
            return '<{0}> {1} </{0}>'.format(name, func(*args, **kwargs)) # Custom tags!
            # Something worth mentioning: functions inside functions can get variables from outside functions
        return wrapper
    return decorator
# Okay, so we created 3 functions, all inside of each other

# Normally, decorators accept a defined function as a parameter with two functions, meaning you don't need ()
# Therefore, adding another function will add a set of parentheses
# I explained that poorly, but that's the way things work; go test out some patterns and observe what happens

# Now, we can decorate!

@tags('p')
@tags('decorated')
@tags('blah')
def f():
    return 'decorated text'  # Note that it doesn't have to return, it can print() or input() or anything that takes str
print(f())

class Miles:
    def __init__(self):
        pass

    @tags('incompetent')  # It works in classes too!
    def get_attributes(self):
        print('Miles')

miles = Miles()
miles.get_attributes()

# And that wraps (ha! wraps!) up the 9th python tutorial! Yay!
