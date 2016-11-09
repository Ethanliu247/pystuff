# Today, we will be looking at some very useful imports
import sys
import os

# It is recommended that you know a little Bash (that's a programming language)

# First, we will look at Pickle
import pickle
# Pickle is used for taking an object and storing it in a binary file
# Oh wow, I just realized you don't know anything about making files in python!

# Well... we gotta start sometime...
filename = 'file.txt'  # This is the name of the file. If it is not in the same directory as the program, enter the path
mode = 'w+' # This is the mode. There are several, but the important ones are 'w' (write) and 'r' (read), also 'w+','r+'
file = open(filename, mode)  # This opens the file; if it doesn't exist (and mode is 'w') then it is created
# Okay, so we've created a file object stored inside of file
# Now we can write text to it
file.write('some lovely text')  # Writes data to the file
file.close()  # Saves the file and closes the file

mode = 'r'  # Setting the mode to read
file = open(filename, mode)  # Opening the file
text = file.read()  # Reading the file data and storing it in a variable
print(text)
file.close()  # Closes file

# As you can see, we have created and read files with python!

# Okay, now we can move on to pickling
file = open('pickle.dat', 'wb+')
# Okay, so there are two differences
# '.dat' is the extension for a binary file; pickling stores data in binary format
# 'wb+' is writing in binary format

# Now, pickling is very simple

# Pickle is often used for storing objects
# Remember that objects include integers, lists, classes, functions, and strings
# You will most often use pickle for lists or dictionaries
toSave = {'data':'stuff', 478:'blah', 'some text':'more stuff'}
pickle.dump(toSave, file)  # Writing the toSave dict into the file
file.close()  # You should still close it normally afterwards

# Now, you can try to read the file
file = open('pickle.dat', 'rb')
data = file.read()
print(data)
# And you will get some barely readable binary stuff
file.close()

file = open('pickle.dat', 'rb')
pickled = pickle.load(file)
print(pickled)  # This will return you original dictionary exactly the way it was!
print(pickled['some text'])  # If you remember everything from Tutorial 2, then you know that this should give the value
# And it does, it returns exactly what you'd expect!

file.close()

# And that's pickle!


# Moving on, we import os and sys earlier
# The thing from sys I most often use is sys.exit()
exit_code = 0
sys.exit(0)
# There are many exit codes, but you will be using 0 because that means everything went well

# In os, there are several useful things
os.remove('pickle.dat')
# This will delete any file name specified
try:
    os.remove('file.txt')
except:
    pass
# Shoot, I forgot to teach you error handling
# I suppose that will be next!

# Another thing in os that is nice is
command = 'cd Desktop'
os.system(command)
# This executes any Bash/Batch command
# This is very useful if you know Bash/Batch
# In case you didn't know, the interactive Bash interface is Terminal on Mac and Linux. The command line is Batch on Win

# And that is all!
