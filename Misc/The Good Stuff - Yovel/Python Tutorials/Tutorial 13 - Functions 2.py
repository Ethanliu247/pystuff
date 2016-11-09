# Miles, you aren't understanding functions, so I'm going to give you this tutorial

def f(x):
    return x + 1
# What you don't understand:
# x is a parameter
# x can only be used inside
# return is not print
# functions are objects

# Okay, let's fix your problems

# In this case, x is a parameter
# Parameters can be used ONLY inside the function
# If we call f like this
f(2)
# It will return 2+1, which is 3
def f(x,y,z):
    return x+y+z
f(1,1,1)
# This will return 3 again
# When you do f(1,1,1) you are setting the local variables x,y,z to 1,1,1 RESPECTIVELY
# You CANNOT use x, y, and z outside the function unless you make a new variable for them

# Now, we will focus on returning
def f(x):
    return x+1
# Okay, so here you see the return keyword
# This is the last thing you put into the function
# It is what the function outputs
# Now, you must understand this
# THIS IS NOT THE SAME AS PRINT
# This is returning the value, and the value can be stored in a variable
a = 1
print(a)
# This prints 1
# So, if you do f(1) and store the returned value (2)
x = f(1)
# Therefore, you CAN DO THE SAME THING WITH THE RETURNED VALUE
print(x)
# IS THE SAME THING AS
print(f(1))
# OKAY???? DO YOU GET IT!?!?!? THIS IS VERY SIMPLE!!!!!!

# Finally, you must understand that functions are objects
f(1)
# This returns a value
f
# This is an OBJECT
# Objects are MANIPULABLE
a = f
# THIS SETS a TO f
# NOW YOU CAN CALL IT
a(1)
# THIS IS THE SAME AS
f(1)
# BECAUSE a IS THE FUNCTION OBJECT f

# OKAY MILES!!!! DO YOU GET IT NOW!? IT'S NOT HARD!!!!!!!!!
