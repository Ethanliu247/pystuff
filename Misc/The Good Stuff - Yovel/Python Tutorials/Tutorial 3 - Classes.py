# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#
#   Miles, this is going to break your brain, so if you aren't ready then go study functions some more, then come back.
#
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

# Classes are very complex, and require a creative mind. This is a basic class

class Example:
    # By convention class names are capitalized
    def __init__(self): # This is automatically run when the class is instantiated
        print('Class initialized!')
    def doStuff(self):
        pass

# Classes are objects. A class like this is just the idea of a class, something that has the potential to be made.
example = Example()
# When you do this, you are creating an instance of the class Example by using the ()
# example is now an instance of the class
# When the instance of the class is created, the __init__ function will be run automatically
# In this case, doing example = Example() would print 'Class initialized!'

# The functions inside of classes can be called like this
example.doStuff()
# Functions in classes act differently than normal functions
# For example, inside the class you see that doStuff has a parameter self
# Self is a conventional name (it can be other things), but you should always use it
# Self is what allows instances to have their own things
# You don't treat self as a parameter
class Example:
    def __init__(self, name):
        self.name = name
        # This sets what you pass as the name to its personal name
# In this example, the __init__ function has a new parameter: name
bob = Example('bob')
# This creates a class instance in the variable bob, with the name bob
# __init__ takes the parameters when creating an instance of the class
person = Example('person')
# Instance person has the name person

print(bob.name)
# This will print bob
print(person.name)
# This will print person

# This is the basic idea behind object-oriented programming
# You have classes, which are instantiated into variables
# These instances of a class are really objects
print(person)
# This attempts to print the object
# You will receive a location in the memory and its type, indicating that it is an object

# Classes are very powerful tools, and you can have instances inside of lists too!

# The following is how inheritance works:
class Animal:
    def __init__(self, name):
        self.name = name
    def play(self):
        print('%s is playing!' % self.name)

class Cat(Animal):  # As you can see, there is something in parentheses here. This is called inheritance.
    def __init__(self, name): # Accepts a name
        super(Cat, self).__init__(name) # Passes the name down here
        # This is complicated, but basically the class Cat is inheriting all the functions from Animal, making the Cat
        # an extension of Animal.

        # super(Cat, self).__init__('Miles')
        # This calls the __init__ function of Animal so that Cat can have its own name too!

cat = Cat('Miles') # Instantiates a Cat with the inherited traits from Animal

# The cool thing about inheritance is that you share functions. In Cat, there is no play() function.
cat.play()
# But this works. Cat inherited the play ability from Animal.
print(cat.name)

# The cat's name is Miles!