# Okay... You've made it this far!
# Now, you will learn basic GUI programming!

from tkinter import *
import threading
from time import time, sleep
import sys
import os
import socket
import random

# We will require our entire arsenal to accomplish our final task.
# IMPORT EVERYTHING!!!!

# Now, you must understand everything you have been taught
# Most importantly, you must understand objects

root = Tk()
# This creates a window object, and a window!

# At the end of a progrsm you have to do root.mainloop() so that the window constantly updates
# You will create your own improved version later

root.geometry('750x750')
# This sets the window size, inside of a string in the format of '100x100'

root.title('Test Window')
# This sets the window title

# Now that we've set some basic configurations, let's add some stuff
label = Label(root, text = 'This is a label')
button = Button(root, text = 'Test Button')
entry = Entry(root)
# These are tkinter objects that I will explain in a moment
# To put them in the window, we have to pack them like so
label.pack()
button.pack()
entry.pack()
# Run the program you should have copied down and look at the beautiful window we made! Yay!

# There are some things that could be improved here. Let's take a closer look.
def buttonCommand():
    global label
    global root
    global entry
    label = Label(root, text = entry.get())
    label.pack()

entry = Entry(root)
button = Button(root, text = 'Submit', command = buttonCommand)
# Here, there are three parameters
# root: the main window
# text: the text of the button
# command: the function OBJECT to call when the button is pressed
entry.pack()
button.pack()
label = None

# This time, we are going to add root.mainloop()
root.mainloop()
# This makes the window constantly update itself so that everything is shown
# ALWAYS PUT THIS AT THE END OF THE PROGRAM

# ALWAYS!!!!!
