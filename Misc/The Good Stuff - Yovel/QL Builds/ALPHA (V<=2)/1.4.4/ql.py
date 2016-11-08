'''
Quick Language (see changelog for version) by Yovel Key-Cohen

Featuring a changelog!
'''

import os
from tkinter import *
import socket
import sys
import pickle
import threading
import random
from time import sleep, time

embedding = False

# Lexer
def words(string):
    word = ''
    state = 0
    tokens = []
    escape = False
    func = 0
    ftemp = []
    for char in string:
        if char is ' ' and state is 0:
            tokens.append(word)
            word = ''
        elif char is '|':
            if escape == True: escape = False
            elif escape == False: escape = True
        elif char is ' ' and state is 1 or func is 1:
            word += ' '
        elif char is '<' and escape == False:
            if word != ' ' and word != '' and func != True: tokens.append(word)
            elif func == True: ftemp.append(word)
            if state == 0: word = ''
            state = 1
        elif char is '>' and escape == False:
            if state == 1: state = 0
            if func != True:
                tokens.append(word)
            elif func == True:
                ftemp.append(word)
            word = ''
        elif char == '{' and escape == False:
            func = 1
            tokens.append(word)
            word = ''
        elif char == '}' and escape == False:
            func = 0
            tokens.append(ftemp)
            word= ''
        elif char is '\n' and state is 0 and func is 0:
            tokens.append(word)
            word = ''
        elif char is '\r' and state is 0:
            tokens.append(word)
            word = ''
        elif char is ';' and state is 0:
            tokens.append(word)
            word = ''
        else:
            word += char
    tokens.append('<EOF_TOKEN>')
    return tokens

# Helps me out in parser
def nextTok(l='',it=''):
    return l[it+1]

# Globals initialization for parsing
s = ''
stack = list()
heap = dict()
working_dir = os.path.expanduser('~')+'/Desktop/'
root = ''
funcs = dict()

# Parser
def parse(codelist, embed=False):
    def ql(code):
        global embedding
        try:
            coded = words(code)
            if embedding: 
                return parse(coded, embed=True)
            elif not embedding:
                parse(coded)
        except KeyboardInterrupt:
            sys.exit(0)
    i = -1
    global stack
    global working_dir
    global heap
    global root
    nextToken = lambda: nextTok(codelist, i)
    nextnextToken = lambda: nextTok(l=codelist, it=i+2)
    skip = False
    dubSkip = False
    for token in codelist:
        i += 1
        if skip:
            if not dubSkip: skip = False
            else:
                skip = True
                dubSkip = False
            continue
        
        # Print output
        elif token == 'out':
            skip = True
            if not embed: print(nextToken(), end='')
            try:
                if nextnextToken() == 'n':
                    print()
            except:
                pass
            if embed: return nextToken()

        # File IO
        elif token == 'file':
            skip = True
            f = open(working_dir+nextToken(), 'w+')
            f.write('')
            f.close()
            del f
        elif token == 'scrap':
            skip = True
            os.remove(working_dir+nextToken())
        elif token == 'overwrite':
            skip = True
            dubSkip = True
            f = open(working_dir+nextToken(), 'w+')
            f.write(nextnextToken())
            f.write('\n')
            f.close()
        elif token == 'write':
            skip = True
            dubSkip = True
            f = open(working_dir+nextToken(), 'a+')
            f.write(nextnextToken())
            f.write('\n')
            f.close()
        elif token == 'read':
            skip = True
            f = open(working_dir+nextToken(), 'r+')
            if not embed: print(f.read())
            if embed: return f.read()
        elif token == 'working':
            skip = True
            working_dir = nextToken()
        elif token == 'getworking':
            if not embed: print(working_dir)
            if embed: return working_dir

        # GUI Implementation (Work in progress)
        elif token == 'window':
            skip = True
            root = Tk()
            root.title(nextToken())
            root.geometry('300x300')
        elif token == 'configBG':
            value = nextToken()
            root.config(bg=value)

                #  ???

        # Very messy and bad function stuff, doesn't really work right now
        elif token == 'func':
            global funcs
            funcs[nextToken()] = nextnextToken()
            print(funcs)
        elif token == 'call':
            try:
                ql(funcs[nextToken()])
            except KeyError:
                print('Function does not exist')

        # Variables and pseudo-memory management
        elif token == 'stack':
            skip = True
            stack.append(nextToken())
        elif token == 'stackin':
            skip = True
            stack.append(input(nextToken()))
        elif token == 'stackpop':
            sp = stack.pop()
            if not embed and nextToken() != 'void': print(sp, end='')
            if embed and nextToken() != 'void': return sp
            try:
                if nextToken() == 'n':
                    print()
            except:
                pass
            if embed: return sp
        elif token == 'heapadd':
            skip = True
            try: heap[int(nextToken())] = ''
            except: print('Integer address expected')
        elif token == 'heapmod':
            skip = True
            dubSkip = True
            if int(nextToken()) in heap.keys(): heap[int(nextToken())] = nextnextToken()
            else: print('Does not exist')
        elif token == 'heapdel':
            skip = True
            del heap[int(nextToken())]
#PROBLEMS \/
        elif token == 'heapget':
            if not embed: print(heap[int(nextToken())], end='')
            try:
                if nextnextToken() == 'n':
                    print()
            except:
                pass
            if embed: return heap[int(nextToken())]

        elif token == 'heapin':
            skip = True
            dubSkip = True
            heap[int(nextToken())] = input(nextnextToken()+'\n')

        # EOF and spacing            
        elif token == '\n':
            pass
        elif token == ';':
            continue
        elif token == '<EOF_TOKEN>':
            break

        # Mathematical Operators
        elif token == 'add':
            try:
                if not embed: print(int(nextToken()) + int(nextnextToken()), end='')
                if embed: return int(nextToken()) + int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'multiply':
            try:
                if not embed: print(int(nextToken()) * int(nextnextToken()), end='')
                if embed: return int(nextToken()) * int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'subtract':
            try:
                if not embed: print(int(nextToken()) - int(nextnextToken()), end='')
                if embed: return int(nextToken()) - int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'divide':
            try:
                if not embed: print(int(nextToken()) / int(nextnextToken()), end='')
                if embed: return int(nextToken()) / int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'mod':
            try:
                if not embed: print(int(nextToken()) % int(nextnextToken()), end='')
                if embed: return int(nextToken()) % int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'power':
            try:
                if not embed: print(int(nextToken()) ** int(nextnextToken()), end='')
                if embed: return int(nextToken()) ** int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')

        # Executing other scripts
        # It's a bit messy because of the closures but it gets the job done
        elif token == 'execute':
            def ql(code):
                global embedding
                try:
                    coded = words(code)
                    if embed: return parse(coded, embed=embedding)
                except KeyboardInterrupt:
                    sys.exit(0)
            def openrun(file):
                try:
                    if file[-3:] == '.ql' or file[-4:] == '.qcl':
                        f = open(working_dir+file, 'r')
                        if embed: return ql(f.read())
                    else:
                        print('Invalid file extension')
                except KeyboardInterrupt:
                    sys.exit(0)
            if embed: return openrun(nextToken())
        
        # Nice to quit the program, right?
        # From this I learned that none of this works without <>
        # Example: to exit you must do 'exit <>'
        # This is solved within the shell
        elif token == 'exit':
            sys.exit(0)
        elif token == 'close':
            return
        elif token == 'scrape':
            host = nextToken()
            port = int(nextnextToken())
            s = socket.socket()
            s.connect((host,port))
            threading.Thread(target=lambda: print(s.recv(2048)))
        elif token == 'wait':
            sleep(int(nextToken()))

# Run Quick Language from within Python     
def ql(code):
    global embedding
    coded = words(code)
    return parse(coded, embed=embedding)

# Run Quick Language from a file
def openrun(file):
    if file[-3:] == '.ql' or file[-4:] == '.qcl':
        f = open(file, 'r')
        ql(f.read())
    else:
        print('Invalid file extension')
