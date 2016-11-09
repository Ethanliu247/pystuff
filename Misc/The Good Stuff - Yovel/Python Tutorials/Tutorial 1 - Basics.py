print('Hello World!')
# Prints out 'Hello World!'

str(2)
# Converts the number 2 to the string '2'

int('2')
# Converts the string '2' to the number 2

input('What is your name?\n')
# Allows the user to give input with the prompt 'What is your name?'
# The \n is how you make a new line within a string

True
# True statement
False
# False statement
None
# An endless void of nothingness

# Operators:
#   +, -, *, /
#   ** is exponent;                      5 ** 2 = 25
#   // is drop decimal of division;      5 // 2 = 2
#   % is find remainder of division;     5 % 2 = 1
#   +=, -=, *=, /=, //=, %=;     Increments a variable by a certain amount and operation
#   Say x is 5
#   Example:             x *= 2 will give 10
#   This is the same as: x = x * 2

x = 5
# This assigns the value 5 to the variable x
# We can use this knowledge like this:
x = input('What is your name?\n')
# This will set the variable x to whatever you reply for the input prompt

def function():
    pass
# This is a function
# Pass means to do nothing

function()
# This is how you call a function

def function(param):
    return param
# In parentheses after the function definition, you see what's called a parameter
# It works like this:
function('String')
# This parameter is then returned to you
# The return passes whatever it says to the program, which can be intercepted by a variable like this:
x = function('String')
# This will set x to whatever is returned. The function returns what you set as param, which is the string 'String'
# Therefore, print(x) will give us 'String'

def p(someText):
    print(someText)
# This is a simple version of what's called a wrapper
# Wrappers are used to provide an easy way to call a large command

def printFormatted(someText):
    print(someText.strip().capitalize())
# As you can see, calling printFormatted('Text') is much easier than using all that blah directly
# This is what wrappers are for (they are only considered wrappers if they are one command long)
x = printFormatted('String')
# This will not work, as printFormatted() doesn't return any values


1 is 1
# This will return True
1 is not 1
# This will return False
1 is 2
# This will return False
1 is not 2
# This will return True
# Another way to do 'is' would be ==
# Another way to do 'is not' would be !=

x = 0

while x < 10:
    x += 1
    print(x)
# This is called a while loop
# First x is set to 0
# Keep in mind that by convention the variables i, j, and k are usually used as iterators
# Then, you start a loop that runs as long as x < 10
# Inside the loop, x is increased by 1
# Then, x is printed out
# The loop repeats until x is not less than 10
# The expected output of this will be 9 lines with the numbers 1 through 9

if x < 11:
    print('x is less than 11')
# This is an if statement, used to check if something is True
elif x > 11:
    print('x is greater than 11')
# The keyword 'elif' is used if you want to check something else as well
else:
    print('x must be 11!')
# 'Else' is used at the end
# Else is used if there is something else you want to check for, but cannot specify
# This is maybe a bad example because it is easy to check if x is 11 (I just did it, in the comment)

for item in range(10):
    print(item)
# This is a bit complex and hard to understand
# Basically it is saying: "for every item in a list of numbers between 0 and 10:"
#                          for     item     in        range(10):
#                              "print out that item"
#                              print(item)

# You can do something interesting with this concept:
# Lets say that
x = 'string'
# We can get each character by
for char in x:
    print(x)
# This will print each individual character in 'string'
# You can also do
if 'ing' in x:
    print('Some of the word '+x+' is ing')
# This checks for the string 'ing' inside of x, which is 'string'
# This will be true, because 'ing' is part of 'string'

basic_list = [1, 2, 3]
# This is a list
# You can do various things like basic_list.append(something)
# This list can be changed

basic_tuple = (1, 2, 3)
# This is a tuple (pronounced as in quinTUPLE or ocTUPLE)
# This list cannot be changed for the remainder of its sad life

basic_dictionary = {'word':'meaning', 'key':'value'}
# A dictionary is an ordered list of key-value pairs
# You add to it like this:  basic_dictionary['new addition'] = 'any value'
# This will add {'new addition':'any value'} to the dictionary
# You get a value from it like this:    print(basic_dictionary['key'])
# This will print 'value'

# Now we can use this knowledge with for loops!
# Keep in mind that you don't have to use i, you can use anything like this:
for item in basic_list:
    print(item)
# If you are smart and can infer things, then you can assume correctly that this will print out 1, 2, and 3

# This should be all you need to know right now!
# From now on, you can program many many useful applications!

# IDEAS:
# Try using your knowledge of dictionaries and functions to make a small text-based dictionary
# Try making a simple text-based game with functions and input
# Try making an insult generator
