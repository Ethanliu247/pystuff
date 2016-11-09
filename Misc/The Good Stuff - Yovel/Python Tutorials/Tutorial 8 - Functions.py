# You understand functions by now, I hope
# As a recap, here is some new stuff and some old stuff
def f(x):
    return x + 1
f(2)
# This will return 3, because what you put in the parentheses is passed and returned +1
# You won't see the output, because you aren't printing it. You are RETURNING it.
# This means that you have to do something with it like
print(
    f(5) * 5
)
# This returns f(5), which is 6, multiplies what is returned (which is 6) by 5, and prints the whole thing out for 30

# DO YOU GET IT!? IF YOU DON'T THEN GO BACK TO THE BEGINNING OF THE FILE AND READ AGAIN!!!
# YOU MUST UNDERSTAND PARAMETERS TO DO THINGS!!!

# Now, we will cover lambda
# Lambda is a fancy way of creating a function; it returns an object which you should assign to a variable like so
function = lambda parameter: parameter + 1
# Now you can call
function(1)
# And you will get 2
# Let's dissect this further:
f = lambda x: x+1
# In your mind, replace lambda with the function name and stick some imaginary parentheses after it around x
# Your mind should be picturing:
def f(x):
# Instead of
f = lambda x:
# Now, what the lambda function returns goes right after the colon, which is
x + 1
# The whole thing in your head should look like this
def f(x):
    return x + 1
# This is the same as
f = lambda x: x + 1
# And that's a bit quicker to write, and it's all in one line!

# So if you ever need a quick function or a one-time function object, use lambda!


#  Next, you will learn another way to stick text into a string because you should know every way
print(
    'this is a string {0}'.format('this is also a string')
)
# This will print 'this is a string this is also a string'
# The {0} is referring to the index (zero-indexed) of the list of strings in .format()
print(
    '{0} {1} {2}'.format('some', 'text', 'blah')
)
# 0, 1, and 2 are replaced by their corresponding positions in the .format()


# Now, we will look at closures (they are very important for later)
# Closures are interesting tools that look a bit like functions within functions
def func(x):
    def closure(y):
        return x+y
# Now, this works interestingly
add5 = func(5)
total10 = add5(5)

# Okay, let's break this down
# In add5, you are assigning the object (which is the closure within) to add5

# Then, you make a new variable called total10 which calls the closure object and returns the param for func() plus
# the closure call
# This can be very useful in certain cases I'm sure!


# Next you will be decorating some code! Literally!