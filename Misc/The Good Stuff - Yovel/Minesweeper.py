from tkinter import *
from random import randint
from sys import exit
from time import sleep

def chance(n):
    if randint(1, 100) <= int(n):
        return True
    return False

root = Tk()

colorN = 'white'
colors = ['blue', 'dark green', 'gold', 'red', 'magenta', 'deep pink']
colorD = 'black'

limit = 3
freq = 7
full = True

current = 0
size = 32
gridlen = 20
height = width = size*gridlen
mark = False

canvas = Canvas(root, width=width, height=height-size*2)
root.geometry(str(width)+'x'+str(height))
root.title('Minesweeper')
root.resizable(0, 0)
canvas.pack()

world_blocks = {}
world_mines = []

for x in range(gridlen-2):
    for y in range(gridlen-2):
        world_blocks[(x, y)] = canvas.create_rectangle(x*size, y*size, x*size+size, y*size+size, fill=colorN)

for x in range(gridlen):
    for y in range(gridlen):
        if chance(freq):
            world_mines.append((x, y))

def getmine(x, y):
    return (x, y) in world_mines
def getblock(x, y):
    return world_blocks[(x, y)]

markers = []

def update(x, y):
    global size, current, mark
    if not mark:
        w = 0
        
        if getmine(x+1, y-1) and full:
            w += 1
        if getmine(x+1, y):
            w += 1
        if getmine(x+1, y+1) and full:
            w += 1
        if getmine(x, y+1):
            w += 1
        if getmine(x, y-1):
            w += 1
        if getmine(x-1, y-1) and full:
            w += 1
        if getmine(x-1, y):
            w += 1
        if getmine(x-1, y+1) and full:
            w += 1
            
        canvas.itemconfig(getblock(x, y), fill='azure')
        if not getmine(x, y) and w > 0:
            canvas.create_text(x*size+size/2, y*size+size/2, text=str(w), fill=colors[w], font=(None, 16))
        elif w == 0 and not getmine(x, y):
            pass
        else:
            canvas.itemconfig(getblock(x, y), fill=colorD)
            current += 1
    else:
        if (x,y) not in markers:
            markers.append((x,y))
            canvas.itemconfig(getblock(x,y), fill='red')
        else:
            markers.remove((x,y))
            canvas.itemconfig(getblock(x,y), fill=colorN)
            
def callback(event):
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    x = round(x/size-0.5)
    y = round(y/size-0.5)
    if (x, y) in world_blocks:
        update(x, y)
        del world_blocks[(x, y)]

def toggle_marker(event):
    global mark
    if mark:
        mark = False
    else:
        mark = True

root.bind('<Button-1>', callback)
root.bind('<KeyPress-m>', toggle_marker)

m_lab = Label(root, fg='red')
m_lab.pack()

c_lab = Label(root)
c_lab.pack()

l_lab = Label(root, text='Limit: '+str(limit))
l_lab.pack()

def mainloop():
    global limit, current, width, height
    while True:
        try:
            root.update()
            root.update_idletasks()
            canvas.update()
            canvas.update_idletasks()
            m_lab.config(text='Marking: '+str(mark))
            c_lab.config(text='Current: '+str(current))
            if current >= limit:
                canvas.create_text(width/2, height/2, text='GAME OVER', fill='orange', font=(None, 72))
                sleep(2.5)
                root.destroy()
        except TclError:
            print('Application Destroyed')
            exit()

mainloop()
