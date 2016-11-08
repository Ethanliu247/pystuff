import Blocks

def autoFlatWorld(*args):
    addBlock = args[0]
    
    for y in range(31, 35):
        for x in range(-2, 80):
            addBlock(Blocks.Dirt.Create(x,y))

    for y in range(35, 39):
        for x in range(-2, 80):
            addBlock(Blocks.Stone.Create(x,y))

    for x in range(-2, 80):
        addBlock(Blocks.GrassyDirt.Create(x, 30))

    for x in range(-2, 80):
        addBlock(Blocks.Bedrock.Create(x, 39))

def voidWorld(*args):
    pass

