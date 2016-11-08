from threading import Thread
from tkinter import *
from time import time, sleep
from random import randint, randrange, choice
from os import system
from os.path import expanduser
from sys import exit
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import pickle

def save(blocks, lvlname):
    lvlname += '.dat'
    file = open('worlds/'+lvlname, 'wb')
    sleep(0.1)
    pickle.dump(blocks, file)
    file.close()

def load(lvlname):
    lvlname += '.dat'
    file = open('worlds/'+lvlname, 'rb')
    try: return pickle.load(file)
    except: return {}
