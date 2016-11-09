#!/usr/bin/python3
from tkinter import *
import time
from sys import exit

root = Tk()
root.geometry('700x200+300+200')
root.title('Timer')

hr = 0
mn = 0
sc = 0
ms = 0

timing = 0

def timelist():
    h, m, s, _ms = str(hr), str(mn), str(sc), str(ms)
    if len(h) < 2:
        h = '0'+h
    if len(m) < 2:
        m = '0'+m
    if len(s) < 2:
        s = '0'+s
    if len(_ms) < 2:
        _ms = '0'+_ms
        
    return h, m, s, _ms

def getTime():
    return ':'.join(timelist())

timer = Label(root, text=getTime(), font='-size 100', fg='dark green')
timer.pack()

def run():
    global timing
    if timing:
        timing = 0
    elif not timing:
        timing = 1

runButton = Button(root, text='Start/Stop', command=run)
runButton.pack()

def mainloop():
    global timing, timer
    global ms, sc, mn, hr
    while True:
        time.sleep(0.1)
        try:
            root.update()
            root.update_idletasks()
        except TclError:
            print('Exit')
            exit()
        if timing:
            ms += 10
            if ms >= 100:
                ms = 0
                sc += 1
            if sc >= 60:
                sc = 0
                mn += 1
            if mn >= 60:
                mn = 0
                hr += 1
            if hr >= 24:
                return 0
            timer.config(text=getTime())
        
mainloop()
