from tkinter import *
import threading
from time import time, sleep
import sys
import os
import socket
import random

# Set up window
root = Tk()
root.geometry('500x500')
root.title('Learning')

# Create our canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Make our mainloop, with a nice try-except to catch the error on closing and exit cleanly
def mainloop(objects):
    while True:
        try:
            root.update()
            root.update_idletasks()
            canvas.update()
            canvas.update_idletasks()
            sleep(0.025)
            for obj in objects:  # This is used to update all of our objects
                obj.draw()
        except TclError:
            print('Application Destroyed')
            sys.exit()

# Okay... Now we will add some fancy images to our canvas and make it move with our arrow keys!
# Then, in tutorial 4, we will do something I forget!

# To make an image that can be used in the tkinter canvas, we need to do something special
# First get your image, and add script directory with os.getcwd()
image = os.getcwd()+'/emerald.gif' # You do not have this image. Use your own .gif and make sure it's in the same directory as your file
# Now the special part
emerald_block = PhotoImage(file=image)
# This turns the image file into a format tkinter can read
# The image MUST be a .gif

# Now put the image on the canvas
emerald = canvas.create_image(200, 200, image=emerald_block)  # Only need x and y instead of x1, y1, x2, y2

# Now we have our image!
# This is a bit drab, so let's make it move!
# To do this, we will need ALL of the skills that we have obtained so far
# We will start by deleting the image
canvas.delete(emerald)

# And then we will make ourselves a class for it
class EmeraldBlock:
    def __init__(self):
        self.texture = emerald_block # Using the predefined emerald texture

        # Now, here is something you should know about PhotoImages:
        self.texture = self.texture.zoom(5, 5)
        # This will increase the size by the factors specified for each axis (x and y)
        self.texture = self.texture.subsample(5, 5)
        # This will decrease the size by only using every Nth pixel for each specified axis
        # In my case, the texture is only 16x16, so I will make it 128x128
        self.texture = self.texture.zoom(8, 8)
        # This multiplies the size by 8 on both axes, therefore getting 128x128

        self.x = 50
        self.y = 50
        self.x = 0
        self.dx = 0
        self.dy = 0
        self.canvas = canvas
        self.id = self.canvas.create_image(self.x, self.y, image=self.texture)
        self.speed = 10
    def draw(self):
        self.x, self.y = self.canvas.coords(self.id)
        self.canvas.move(self.id, self.dx, self.dy)
    def up(self, event):
        self.dy = -self.speed # The up-down directions are reversed
    def down(self, event):
        self.dy = self.speed # Reversed
    def right(self, event):
        self.dx = self.speed
    def left(self, event):
        self.dx = -self.speed
    def stopX(self, event):
        self.dx = 0
    def stopY(self, event):
        self.dy = 0

# Let's dissect this lovely class
# In __init__(), we set the position, texture, and create it on the canvas, as well as initialize dx and dy
# In draw(), we collected the coordinates of our object and moved it based on the dx and dy
# The "event" parameter is passed in with the key press, so you need to add it at the end of your other parameters
# The rest change dx and dy so that we can move around

block = EmeraldBlock()

# But how do we move?
# We can do this with keybinds, like this
root.bind('<KeyPress-Down>', block.down) # Use function object, don't call it
root.bind('<KeyPress-Up>', block.up)
root.bind('<KeyPress-Left>', block.left)
root.bind('<KeyPress-Right>', block.right)
# These make it so that when we have the window selected, we can press the arrow keys to move
# But you will notice that we can't stop
# dx and dy never go to zero unless we use stopX and stopY
# We can do this so that whenever we release one of these keys, we stop
root.bind('<KeyRelease-Down>', block.stopY)
root.bind('<KeyRelease-Up>', block.stopY)
root.bind('<KeyRelease-Left>', block.stopX)
root.bind('<KeyRelease-Right>', block.stopX)

# Now run, and enjoy the lovely moving image!
# Note that the same can be done for any tkinter object
mainloop([block])  # <---- Also remember that you must pass a list of objects (only block right now) to mainloop
