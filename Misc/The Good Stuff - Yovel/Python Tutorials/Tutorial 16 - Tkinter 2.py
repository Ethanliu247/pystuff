from tkinter import *
import threading
from time import time, sleep
import sys
import os
import socket
import random

# Okay here you go - real customized graphics in tkinter!
# First, we will begin by learning what mainloop does and making our own better version

root = Tk()
root.geometry('500x500')
root.title('Learning')

def mainloop():
    while True: # Forever
        root.update() # Update the window
        root.update_idletasks() # Update the window in a different way I have no idea why it needs two ways but okay let's listen to tkinter people because it knows more than me

# Mainloop updates the window so that you can change it while your program is running

# Now we learn about graphics!
canvas = Canvas(root) # Pass in the main window
# This creates a canvas for us that we can pack
# On occasion, the canvas will be only a few pixel big
# So, we need to make it bigger
canvas = Canvas(root, width=500, height=500) # Pass in window sizes
canvas.pack()
# And now we can do stuff with it just like a canvas would do
# Let's start with some simple stuff

canvas.create_rectangle(0, 0, 50, 50, fill='green', outline='')
# Creating shapes takes a number of arguments
# The first four are x1, y1, x2, and y2
# The fill keyword changes the color of the shape
# The outline changes the color of the border, which can be set to have no border like that

# There are other things we can do
canvas.create_oval(50, 50, 100, 100, fill='red', outline='')
canvas.create_line(0, 200, 500, 200, fill='blue') # Can't use outline here because it's a line

# Now, if you run this, you will find that there is no line!
# We have our special mainloop, but it doesn't update the canvas
def mainloop():
    while True:
        root.update()
        root.update_idletasks()
        canvas.update()
        canvas.update_idletasks()
# Now, it will update the canvas too!
# Run mainloop at the end of your program:
mainloop()
# And you have the shapes!
