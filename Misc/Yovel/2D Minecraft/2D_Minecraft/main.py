from threading import Thread
from tkinter import *
from time import time, sleep
from random import randint, randrange, choice
from os import system, listdir, getcwd
from os.path import expanduser
from sys import exit
from platform import system
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import pickle
import subprocess

from Blocks import *
import progress
import Blocks
import Coordinates
from changelog import version

directory = listdir(getcwd()+'/worlds/')

NewWorld = False

loc = getcwd()+'/music/'
tracks = [
        'Subwoofer',
        'Haggstrom',
        'Minecraft'
        ]

class Music(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.process = None
    def play(self):
        self.process = subprocess.Popen([('play' if system() == 'Linux' else 'afplay'), loc+choice(tracks)+'.mp3'])
    def playing(self):
        return self.process != None
    def stop(self):
        if self.process != None:
            self.process.terminate()
            self.process = None

music = Music()

looping_wp = True

wp = Tk()
wp.geometry('400x300+440+200')
wp.title('Title Screen')

def quit_cmd():
    global looping_wp
    global music
    
    looping_wp = False
    wp.destroy()
    music.stop()
    exit()

version = Label(wp,
text='2D Minecraft\nVersion '+str(version[0])+' '+version[1]+'\nBy Yovel Key-Cohen',
fg='dark green', anchor=SW, justify=LEFT)
version.place(x=0, y=250)
quitButton = Button(wp, text='Quit', command=quit_cmd)

WORLDTYPE = StringVar()

if not music.playing():
    try: music.play()
    except RuntimeError: music = Music()

def newworldwindow():
    global NewWorld
    global wp
    global WORLDTYPE
    global music

    wp.title('New World')
    
    Label(wp, text='Enter world name').pack()
    worldName = Entry(wp)
    worldName.pack()

    if not music.playing():
        try: music.play()
        except RuntimeError: music = Music()

    worldSelect = Label(wp, text='World Type:')
    worldSelect.place(x=0, y=75)
    flatWorld = Radiobutton(wp, text='Flat', value='flat', variable=WORLDTYPE)
    voidWorld = Radiobutton(wp, text='Void', value='void', variable=WORLDTYPE)
    flatWorld.place(x=10, y=100)
    voidWorld.place(x=10, y=125)
    flatWorld.invoke()
    
    submitButton = Button(wp, text='Submit', command=lambda: setWorldName(worldName.get()))
    submitButton.pack()
    newWorldButton.destroy()
    loadWorldButton.destroy()
    version.destroy()

WorldName = ''

def setWorldName(name):
    global WorldName
    global NewWorld
    global wp
    global WORLDTYPE
    global music
    
    if not music.playing():
        try: music.play()
        except RuntimeError: music = Music()
        
    wp.destroy()
    WorldName = name
    WORLDTYPE = WORLDTYPE.get()
    NewWorld = True

LoadWorld = False
world = ''

def loadworldgui():
    global NewWorld
    global wp
    global directory
    global music
    
    wp.title('Load World')

    if not music.playing():
        try: music.play()
        except RuntimeError: music = Music()

    Label(wp, text='Enter world name').pack()
    worldName = Entry(wp)
    worldName.pack()
    alldafiles = Text(wp)
    alldafiles.insert(END, 'WORLDS:\n')
    
    for file in directory:
        if file[-4:] == '.dat':
            try:
                if pickle.load(open('worlds/'+file, 'rb')): isaworld = True
            except pickle.UnpicklingError:
                isaworld = False
            if isaworld: alldafiles.insert(END, file+'\n')
    submitButton = Button(wp, text='Open', command=lambda: loadworld(worldName.get()))
    submitButton.pack()
    alldafiles.pack()
    alldafiles.config(state=DISABLED)
    newWorldButton.destroy()
    loadWorldButton.destroy()
    version.destroy()

def loadworld(name):
    global world
    global LoadWorld
    global wp
    global WorldName
    global music

    if not music.playing():
        try: music.play()
        except RuntimeError: music = Music()

    if name[-4:] == '.dat': name = name[:-4]
    try:
        world = progress.load(name)
        WorldName = name
        if world:
            LoadWorld = True
            wp.destroy()
    except FileNotFoundError:
        pass

newWorldButton = Button(wp, text='New World', command=newworldwindow)
loadWorldButton = Button(wp, text='Load World', command=loadworldgui)

newWorldButton.pack()
loadWorldButton.pack()
quitButton.pack()

def mainloop_wp():
    while looping_wp:
        wp.update()
        wp.update_idletasks()
        sleep(0.05)

try: mainloop_wp()
except TclError:
    print('Application Destroyed')
    looping_wp = False
    music.stop()

while looping_wp:
    pass

if NewWorld == True or LoadWorld == True:
    root = Tk()

    chooser = Tk()
    chooser.geometry('250x800+2000+0')
    chooser.title('Editor')
    chooser.lift()
    root.lift()

    width = 1035
    height = 650
    root.geometry(str(width)+'x'+str(height)+'+0+0')

    root.title('Minecraft - '+WorldName.upper())

    root.resizable(0,0)
    chooser.resizable(0,0)

    SIZE = 16
    TICKRATE = 64
    SKYCOLOR = 'SteelBlue1'

    canvas = Canvas(root, width=width, height=height, highlightthickness=1,
                    highlightbackground='black', bg=SKYCOLOR)
    canvas.pack()

    blocks = {}

    image_buffer = set()

    def multiple(number, mult_of):
        return(number/mult_of).is_integer()


    def grid(x=0, y=0):
        return x*SIZE, y*SIZE
    def ungrid(x=0, y=0):
        return x/SIZE, y/SIZE

    selected_block_path = 'Blocks.Dirt.Create(x,y)'

    def placer(event):
        global blocks
        global selected_block_path

        c = event.widget
        try:
            oldx = c.canvasx(event.x)
            oldy = c.canvasy(event.y)
        except AttributeError:
            pass
        except UnboundLocalError:
            pass
        try:
            x, y = round(ungrid(oldx, oldy)[0])-1, round(ungrid(oldx, oldy)[1])-1

            if not (x,y) in blocks.keys():
                addBlock(eval(selected_block_path))
        except UnboundLocalError:
            pass

    def remover(event):
        global blocks

        c = event.widget
        try:
            oldx = c.canvasx(event.x)
            oldy = c.canvasy(event.y)
        except AttributeError:
            pass
        except UnboundLocalError:
            pass

        try:
            x, y = round(ungrid(oldx, oldy)[0])-1, round(ungrid(oldx, oldy)[1])-1

            if (x,y) in blocks.keys():
                removeBlock((x,y))

        except UnboundLocalError:
            pass

    def coords(x,y):
        return Coordinates.Coords(x,y).list()

    def addBlock(block):
        padding = 0
        try:
            img = PhotoImage(file=block.texture)
            blocks[block.coords] = canvas.create_image(grid(block.x+padding+1, block.y+padding+1), image=img), block.breakable, block
            image_buffer.add(img)
        except Exception as e:
            print(e)
            old = block
            block = Blocks.Block.Block(old.x, old.y)
            img = PhotoImage(file=block.texture)
            blocks[block.coords] = canvas.create_image(grid(block.x+padding+1, block.y+padding+1), image=img), block.breakable, block
            image_buffer.add(img)

    def removeBlock(coords):
        if blocks[coords][1]:
            canvas.delete(blocks[coords][0])
            del blocks[coords]

    def fill(block_class, x1, y1, x2, y2):
        for x in range(x1,x2):
            for y in range(y1,y2):
                addBlock(block_class(x,y))

    def pick(string):
        global selected_block_path
        selected_block_path = ('Blocks.'+string+'.Create(x,y)')

    if NewWorld:
        import world_types
        if WORLDTYPE == 'flat':
            world_types.autoFlatWorld(addBlock)
        elif WORLDTYPE == 'void':
            world_types.voidWorld(addBlock)
    elif LoadWorld:
        for block in world:
            addBlock(world[block][2])

    root.bind('<Button-1>', remover)
    root.bind('<Button-2>', placer)

    dirtButton = Button(chooser, text='Dirt',
                        command=lambda: pick('Dirt'))
    grassButton = Button(chooser, text='Grass',
                        command=lambda: pick('GrassyDirt'))
    woodButton = Button(chooser, text='Wooden Planks',
                        command=lambda: pick('Planks'))
    stoneButton = Button(chooser, text='Stone',
                        command=lambda: pick('Stone'))
    cobbleButton = Button(chooser, text='Cobblestone',
                        command=lambda: pick('Cobblestone'))
    bedrockButton = Button(chooser, text='Bedrock',
                        command=lambda: pick('Bedrock'))
    brickButton = Button(chooser, text='Brick',
                        command=lambda: pick('Brick'))
    diamondButton = Button(chooser, text='Diamond Block',
                        command=lambda: pick('DiamondBlock'))
    goldButton = Button(chooser, text='Gold Block',
                        command=lambda: pick('GoldBlock'))
    ironButton = Button(chooser, text='Iron Block',
                        command=lambda: pick('IronBlock'))
    logButton = Button(chooser, text='Log',
                        command=lambda: pick('Log'))
    glassButton = Button(chooser, text='Glass',
                        command=lambda: pick('Glass'))
    obsidianButton = Button(chooser, text='Obsidian',
                        command=lambda: pick('Obsidian'))
    emeraldButton = Button(chooser, text='Emerald Block',
                        command=lambda: pick('EmeraldBlock'))
    lapisButton = Button(chooser, text='Lapis Block',
                        command=lambda: pick('LapisBlock'))
    redstoneButton = Button(chooser, text='Redstone Block',
                        command=lambda: pick('RedstoneBlock'))
    cobwebButton = Button(chooser, text='Cobweb',
                        command=lambda: pick('Cobweb'))
    glowstoneButton = Button(chooser, text='Glowstone',
                        command=lambda: pick('Glowstone'))

    dirtButton.pack()
    grassButton.pack()
    woodButton.pack()
    stoneButton.pack()
    cobbleButton.pack()
    bedrockButton.pack()
    brickButton.pack()
    diamondButton.pack()
    goldButton.pack()
    ironButton.pack()
    logButton.pack()
    glassButton.pack()
    emeraldButton.pack()
    lapisButton.pack()
    redstoneButton.pack()
    obsidianButton.pack()
    cobwebButton.pack()
    glowstoneButton.pack()

    steve_left = PhotoImage(file='SteveLeft.gif')
    steve_right = PhotoImage(file='SteveRight.gif')
    steve_left = steve_left.subsample(2,2)
    steve_right = steve_right.subsample(2,2)

    image_buffer.add(steve_left)
    image_buffer.add(steve_right)

    playing = False

    def save():
        global blocks
        global WorldName
        
        progress.save(blocks, WorldName)
    
    class Steve:
        def __init__(self):
            self.left = steve_left
            self.right = steve_right
            self.canvas = canvas
            self.startx = None
            self.starty = None
            self.img = self.right
            self.upDisabled = False
            self.downDisabled = False
            self.rightDisabled = False
            self.leftDisabled = False
            self.pos = (0, 0)
            self.dx = 0
            self.dy = 0
            self.speed = 0.2
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.dim = (16, 62)
        def top(self):
            return self.pos[1] - self.dim[1]/2
        def bottom(self):
            return self.pos[1] + self.dim[1]/2
        def sideL(self):
            return self.pos[0] - self.dim[0]/2
        def sideR(self):
            return self.pos[0] + self.dim[0]/2
        def create(self, x, y):
            self.id = self.canvas.create_image(grid(x, y), image=self.img)
            self.startx = x
            self.starty = y
        def getX(self):
            return self.pos[0]
        def getY(self):
            return self.pos[1]
        def draw(self):
            self.canvas.move(self.id, grid(self.dx)[0], grid(y=self.dy)[1])
            self.pos = ungrid(self.canvas.coords(self.id)[0], self.canvas.coords(self.id)[1])
        def moveRight(self, event=''):
            if not self.rightDisabled:
                self.dx = self.speed
            else:
                self.dx = 0
            self.img = self.right
        def moveLeft(self, event=''):
            if not self.leftDisabled:
                self.dx = 0-self.speed
            self.img = self.left
        def moveUp(self, event=''):
            if not self.upDisabled:
                self.dy = 0-self.speed
        def moveDown(self, event=''):
            if not self.downDisabled:
                self.dy = self.speed
            else:
                self.dy = 0
        def stopY(self, event=''):
            self.dy = 0
        def stopX(self, event=''):
            self.dx = 0

    steve = Steve()

    def play():
        global playing
        global steve
        global blocks
        global WorldName

        save()

        root.geometry(str(width+250)+'x'+str(height))
        root.lift()

        steve.create(1, 2)

        sleep(0.05)
        chooser.destroy()
        playing = True

        root.unbind('<Button-1>')
        root.unbind('<Button-2>')

        root.bind('<KeyPress-w>', steve.moveUp)
        root.bind('<KeyPress-d>', steve.moveRight)
        root.bind('<KeyPress-a>', steve.moveLeft)
        root.bind('<KeyPress-s>', steve.moveDown)
        root.bind('<KeyRelease-w>', steve.stopY)
        root.bind('<KeyRelease-d>', steve.stopX)
        root.bind('<KeyRelease-a>', steve.stopX)
        root.bind('<KeyRelease-s>', steve.stopY)

    you_can_play = True

    if you_can_play:
        playButton = Button(chooser, text='Save and Fly', command=play, foreground='blue')
        playButton.place(x=75, y=575)

    def mainloop():
        global playing
        global steve
        global TICKRATE
        global music
        
        while True:
            try:
                if playing:
                    steve.draw()
                    canvas.itemconfig(steve.id, image=steve.img)
                if not music.playing():
                    try: music.play()
                    except RuntimeError: music = Music()
                root.update()
                root.update_idletasks()
                canvas.update()
                sleep(TICKRATE**-1)
            except TclError as e:
                if str(e) != \
                   '''can't invoke "update" command:  application has been destroyed''':\
                   print(str(e)+'\n')
                print('Application Destroyed')
                try: root.destroy()
                except: pass
                try: chooser.destroy()
                except: pass
                music.stop()
                exit()

    mainloop()
    NewWorld = False
    LoadWorld = False

# Well, that's the end of the program!

