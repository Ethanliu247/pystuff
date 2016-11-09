# Threading is simple yet powerful, and is very useful for quickening or synchronizing step-by-step processes
# Threading is another word for multiprocessing
import threading
# Threading import
from random import randint

def rangeBig():
    x = 0
    for i in range(randint(1000,1000000)):
        x += i
    print(x)
# Now, if you want to do this fifty times, then it will be a bit slow
testThread = threading.Thread(target=rangeBig)
# This is how you create a thread. The function you thread is defined by target= in the parameters
# The target must be an object, not the function itself, so you don't so rangeBig()
# There is a way to work around this which I will show later

# Start the thread:
testThread.start()
# It will finish, and print out the number!

# But what if you want to do this many times to utilize the speed of multiprocessing?
things = []
for i in range(50):
    things.append(threading.Thread(target=rangeBig))
    # threading.Thread() returns a class instance, so we can add that to a list
for i in range(len(things)):  # For every object in the list
    things[i].start()
    # This will start the thread by using the object within the list

# This finished relatively fast, but you saw it hesitated in the beginning and printed output in chunks!
# Without threading, this would do the function 50 times one after the other! This would take far longer!

# Now, you may run into the problem where you want to pass parameters to the target function
del testThread, things, rangeBig
# Cleaning up

def randomStuff(a, b):
    print(randint(a, b))

thread = threading.Thread(target=randomStuff)
# You can't pass arguments because it needs an object, not function call
# There are two ways around this
thread = threading.Thread(target=randomStuff, args=(1, 10))
# Thread() gives a nice way to do this, where you pass a tuple to args= in the parameters

thread = threading.Thread(target=lambda: randomStuff(1, 10))
# This gives target= an object WITH the parameters (1, 10)
# Lambda itself is an interesting keyword, that will be covered in the next tutorial!
