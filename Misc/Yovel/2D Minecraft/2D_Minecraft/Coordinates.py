from threading import Thread
from tkinter import *
from time import time, sleep
from random import randint, randrange, choice
from os import system
from os.path import expanduser
from sys import exit
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

class Coords:
    x = 'x'
    y = 'y'
    
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z
    def list(self):
        return self.x, self.y
    def dict(self):
        return {Coords.x:self.x, Coords.y:self.y}
