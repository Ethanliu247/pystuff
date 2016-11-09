# OOPS - Object-Oriented Programming Stuff

# As you have learned, many things in python are actually objects
x = 5
def f():
    pass
class C:
    pass

# These are all objects, and you can find their address in the memory like this
hex(id(x))
hex(id(f))
hex(id(C))
# These will return a hexadecimal (using hex()) value for their memory addresses, which indicates that they are objects
# The best way to use objects is as classes. This is how Minecraft works, and how almost everything in Java works
class Player:
    def __init__(self):
        self.inventory = []
    def givePlayer(self, item):
        self.inventory += item  # I don't know why, but this gives the inventory ['D', 'i', 'r', 't'] instead of 'Dirt'

player = Player()

class Block:
    def __init__(self, mineral='BLOCK'):
        self.mineral = mineral
        self.exists = True
    def breakBlock(self, person):
        if self.exists and self.mineral is not 'BLOCK':
            self.exists = False
            person.givePlayer(self.mineral)
        else:
            return 'This block does not exist'

# Now, you can make multiple types of blocks that are still considered Block
class Dirt(Block):
    def __init__(self, mineral):
        super(Dirt, self).__init__(mineral)

# Now we can break blocks of dirt in the world
dirt1 = Dirt('Dirt')
dirt2 = Dirt('Dirt')
dirt3 = Dirt('Dirt')

dirt1.breakBlock(player) # Look at the function parameters inside the class; we must specify who broke the block
dirt2.breakBlock(player)

print(player.inventory)
# As you can see, there is now some dirt in the player's inventory
# This is the power of object-oriented programming, especially when using classes

# I hereby challenge you to take a TEST
# The test is required to move on

# The challenge: Use you knowledge of objects, lists, functions, and classes to make a way for the player to put an
# object into the world again. Also add more blocks, and make a few items too. You can do things like making player
# health without having enemies; you can have redundant things.
# The program you create MUST WORK
# You can get help from me whenever you like. I suggest that you let me guide you while you make this.

# Have fun!
