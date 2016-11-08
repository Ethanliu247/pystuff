from threading import Thread
from tkinter import *
from time import time, sleep
from random import randint, randrange, choice
from os import system
from os.path import expanduser, realpath, dirname
from sys import exit
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

import Blocks.Block

# Note: This is ONLY meant to be run from main
# If this is not run from main, it will crash and burn

class Create(Blocks.Block.Block):
    def __init__(self, x, y):
        super(Create, self).__init__(x, y, 'Stone', None, True, 'Blocks/textures/stone.gif',
                                   0, 0, 'hand')
