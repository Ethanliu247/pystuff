# And so that concludes the Python tutorials!
# The next step is to learn something else

# I have more tutorials coming, a series of C++ and then maybe Java or Perl


# There are a couple of things I forgot to teach you with tkinter, so here are some examples:

# Threading in tkinter doesn't work, and time.sleep() pauses the entire program, so how do we do timed commands with tkinter?
root = Tk()
def func():
	print('Hello')
root.after(1000, func)
# Main window (possibly canvas.after works too) has the command after
# You pass in the number of milliseconds to wait, and then the function to call

# Another possibly important thing you ought to know is
canvas = Canvas(root)
search = canvas.find_overlapping(0, 0, 50, 50)
# The find_overlapping creates a box (with x1, y1, x2, y2) that is used to find object that overlap with the rectangle
# You can create a cool hitbox class that checks for non-directional collisions

# If you want to see these in action, check out the snake.py I made. In the top of the program, there are some
# settings you can fiddle with. I used find_overlapping to make a hitbox class for collisions, and without infinite_lines the after command tells the lines when to die


# The rest you don't know how to do just requires inference and creativity
# Enjoy knowing Python