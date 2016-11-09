#!/usr/bin/python3
import tkinter as tk
import random
import time
import math
p = input("Enter number of players (1-4, default 1): ")
while not (p in ("", "1", "2", "3", "4")):
    p = input("Invalid. Enter number of players: ")
if p == "":
    p = 1

GI = 0.5 #important value; determines lots of things like spood
window = tk.Tk()
window.title("WaveWave.exe")
c = tk.Canvas(window, width=400, height=300, bg="#ffffff")
k = False
waves = []
keys = ("space", "Delete", "Escape", "KP_Add")
colors = (("#0088ff", "#88aaff"), ("#ff0044", "#ff00aa"), ("#448800", "#44aa00"), ("#bbbb00", "#ffff00"))
obstacles = []

class Obstacle:
    def __init__(self):
        obstacles.append(self)
        self.radius = 10
        self.color = 'black'
        self.x = 400
        self.y = random.randint(50, 250)
        self.render = c.create_oval(self.x-self.radius, self.y-self.radius,
                                    self.x+self.radius, self.y+self.radius,
                                    fill=self.color)
    def update(self):
        for wave in waves:
            if wave.w in c.find_overlapping(*c.bbox(self.render)):
                raise Exception('A player died and I don\'t know what you want to happen so this error was thrown!')
                return
        if self.x >= -self.radius:
            self.x -= 2
        else:
            obstacles.remove(self)
        c.delete(self.render)
        self.render = c.create_oval(self.x-self.radius, self.y-self.radius,
                                    self.x+self.radius, self.y+self.radius,
                                    fill=self.color)

class EdgeManager:
    def __init__(self):
        self.d = 0
        self.fakeY = 0
        self.edges = [EdgeNode(150)]
    def update(self):
        pass

class EdgeNode:
    def __init__(self, y, l=None):
        self.x = 400
        self.y = y
        self.l = l

class TNode:
    def __init__(self, x, y, l=None):
        self.x = x
        self.y = y
        self.l = l
    def disb(self):
        c.delete(self.l)
class Wave:
    def __init__(self, key, cols):
        self.direction = GI
        self.y = 150
        self.key = key
        self.ded = False
        self.nodes = [TNode(50, 150)]
        self.score = 0
        self.s = c.create_text((398,2+20*len(waves)), anchor="ne", text="0", fill=cols[0], font=("sans-serif", 15))
        self.v = len(waves)
#       self.t = c.create_line(50, 150, 0, 200, fill=colors[1], width=3)
        self.w = c.create_polygon(45, self.y + 5, 55, self.y - 5, 62, self.y + 12, outline="", fill=cols[0])
        self.c = c.create_oval(47, self.y + 3, 53, self.y - 3, outline="", fill=cols[1])
        self.f = True
        waves.append(self)
    def createNode(self):
        k = c.create_line(50,self.y, self.nodes[len(self.nodes)-1].x, self.nodes[len(self.nodes)-1].y, fill=colors[self.v][1], width=3)
        self.nodes.append(TNode(50, self.y, k))
    def kill(self):
        self.ded = True
        print("You just KYSed, retard!")
    def flipu(self, self1):
        if self.ded:
            return
        self.direction = -GI
        self.f = True
        c.coords(self.w, 45, self.y - 5, 55, self.y + 5, 62, self.y - 12)
        self.createNode()
    def flipd(self, self1):
        if self.ded:
            return
        self.direction = GI
        self.f = True
        c.coords(self.w, 45, self.y + 5, 55, self.y - 5, 62, self.y + 12)
        self.createNode()
    def update(self):
        if self.ded:
#            for i in self.nodes:
#                i.disb()
            c.move(self.w, -GI, 0)
            c.move(self.c, -GI, 0)
            self.nodes[0].x -= GI
            for i in range(1,len(self.nodes)):
                self.nodes[i].x -= GI
                c.move(self.nodes[i].l, -GI, 0)
            return
        tbd = -3
        self.score += GI / 25
        c.itemconfig(self.s, text=math.floor(self.score))
        if (self.y < 7 and self.direction < 0) or (self.y > 293 and self.direction > 0):
            if self.f is True:
                c.coords(self.w, 50, self.y + 7, 50, self.y - 7, 67, self.y)
                self.f = False
                self.createNode()
            k = 0
        else:
            k = self.direction
        self.y += k
        c.move(self.w, 0, k)
        c.move(self.c, 0, k)
        self.nodes[0].x -= GI
        for i in range(1,len(self.nodes)-1):
            self.nodes[i].x -= GI
            c.move(self.nodes[i].l, -GI, 0)
            if self.nodes[i].x < 0:
                self.nodes[i].disb()
                tbd = i - 1
        if tbd != -3:
            self.nodes.remove(self.nodes[tbd])
        q = len(self.nodes) - 1
        self.nodes[q].y = self.y
        self.nodes[q].x = 50
        c.coords(self.nodes[q].l, self.nodes[q].x, self.nodes[q].y, self.nodes[q-1].x, self.nodes[q-1].y)
for i in range(0, int(p)):
    Wave(keys[i], colors[i])
    waves[i].createNode()
edges = EdgeManager()
def doNothing(self):
    pass
c.pack()
for i in waves:
    print(i)
    c.bind_all("<KeyRelease-" + i.key + ">", i.flipd)
    c.bind_all("<KeyPress-" + i.key + ">", i.flipu)
    c.bind("<KeyPress-q>", i.kill)
def tick(e=None):
    if random.randint(0, 100)== 50:
        Obstacle()
    for obs in obstacles:
        obs.update()
    allded = True
    for i in waves:
        i.update()
        if not i.ded:
            allded = False
    if allded:
        gameover()
        return
    edges.update()
    c.update()
    window.after(2, tick)
def gameover(e=None):
    if not s:
        s = 1
        if s == 1:
            print("The highscore this round was", str(max(waves, key=lambda x: x.score))+".")

tick()
window.mainloop()
