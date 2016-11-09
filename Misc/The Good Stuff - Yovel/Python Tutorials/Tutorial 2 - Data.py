# This is tutorial number 2!
import random
import time
# Okay, so this tutorial will cover everything I taught you today that isn't in the other tutorial

# First off, you get an item from a list in two ways: one is through a 'for' loop, and the other is
l = ['a', 'b', 'c']
print(l[1])
# Remember, lists are zero-indexed, so the first item in a list is l[0]

# The next thing I taught you were these important commands
random.choice(l) # Returns an item from a list
random.randint(0, 10) # Returns a random integer within specified range
time.time() # Returns current system time in milliseconds
time.sleep(0.5) # Forces the program to wait for an amount of seconds

# Now, I will teach you a few new things
s = 'string'
print(s[0])
# Based on what you know about lists, what do you think will happen?
# Now, I will teach you something similar
print(s[:])
# This is called 'splicing'
# It gets the characters in the range [:]
# It works like this
print(s[1:]) # Gives s[1] and above
print(s[:4]) # Gives all up to s[4]
print(s[:]) # Gives all
print(s[:-1]) # Gives everything up to the last character
print(s[:-5]) # Gives everything up to the 5th character from the end
print(s[-3:]) # Gives everything passed the 3rd to last character
# And so on, so forth

# Now, a few tricks
import time
# As you know, requires time.time() to get system time
from time import time
# This imports only the function time(), but allows you to throw out the time.blah
from time import *
# This will import everything from time, including things like time() and sleep() so you don't need the time.blah
# This is generally not a good idea, in case two imports have the same function name and then everything gets messed up
# So usually, I only do this (for time, at least)
from time import sleep, time
# Which imports sleep and time from time so you don't need time.blah

# The last thing I have to teach you in this file is two more methods of string concatenation
print('Some text '+'some more text') # You know this one, with the +. This will work in many cases (only use strings!)
print('Some text', 'some more text') # This eliminates the need for a space at the end of the first string, and will
# work with any data type including integers and strings, BUT THIS ONLY WORKS INSIDE OF print()
print('Some text %s' % 'some more text')
# This is by far the best way, because it lets you quickly place text wherever you need and it works with
# all data types. It looks hard to understand, but it is very useful. If you have questions, ask Yovel

# The final lessons are the other data types and various conversions
x = 2
# If you need to do
print('some text' + x)
# This will throw an error. You need
print('some text' + str(x))
# If you need
x = '6'
print(5 + x)
# This will throw an error. You need
print(5 + int(x))
# This will work
# There are other things you can do like
l = list('helloworld')
# If you print l, it won't say 'helloworld', it will say ['h','e','l','l','o','w','o','r','l','d']
# You can make it a tuple (which can't change)
t = tuple(l)
# You can make integers (no decimals) into floating point numbers (have decimals) like
f = float(1)
# There isn't much use to this, but it's nice to know. Variable f will now give 1.0 instead of 1

# Now, there are some other things you must know about variables
# To delete a variable (YOU CAN'T USE IT AGAIN UNLESS YOU MAKE IT AGAIN)
del f
# You can do multiple like this
del t, l, s, x
# You can do similar things when assigning variables
t, l, s, x = 1, 2, 3, 4
# This will set t to 1, l to 2, s to 3, and x to 4
# You can also
a = b = c = 1
# Now a, b, and c are 1


# Well, that's all for this tutorial file!
# Next time, we are doing Classes!
# They are incredibly complicated! Yay!

# Questions: go to Yovel or TRY TO FIGURE THEM OUT ON YOUR OWN FOR MORENDAS' SAKE IT IS REALLY EASY JUST TRY!!!!!!!!!!!!
