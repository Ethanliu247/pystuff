class Block:
    def __init__(self, x, y, name = 'BLOCK', drop = None, breakable = True,
                 texture = 'Blocks/textures/missing_texture.gif',
                 durability = 2, tier = 0, breakTool = 'pickaxe'):
        self.breakable = breakable
        self.exists = True
        self.name = name
        self.drop = drop
        self.tier = tier
        self.texture = texture
        self.durability = durability
        self.breakTool = breakTool
        self.x = x
        self.y = y
        self.coords = x,y
        self.power = 0
    def destroy(self):
        self.breakable = True
        self.exists = False
    def place(self):
        self.exists = True
    def powered(self):
        return self.power == True
    def on(self):
        self.power = 1
    def off(self):
        self.power = 0
