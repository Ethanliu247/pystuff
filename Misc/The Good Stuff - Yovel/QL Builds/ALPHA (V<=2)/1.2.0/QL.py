import os
from tkinter import *
import socket
import sys
import pickle

embedding = False

# Lexer
def words(string):
    word = ''
    state = 0
    tokens = []
    escape = False
    for char in string:
        if char is ' ' and state is 0:
            tokens.append(word)
            word = ''
        elif char is '|':
            if escape == True: escape = False
            elif escape == False: escape = True
        elif char is ' ' and state is 1:
            word += ' '
        elif char is '<' and escape == False:
            if word != ' ' and word != '': tokens.append(word)
            if state == 0: word = ''
            state = 1
        elif char is '>' and escape == False:
            if state == 1: state = 0
            tokens.append(word)
        elif char is '\n' and state is 0:
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

# Parser
def parse(codelist, embed=False):
    i = -1
    global stack
    global working_dir
    global heap
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
            if not embed: print(nextToken())
            return nextToken()

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
            return f.read()
        elif token == 'working':
            skip = True
            working_dir = nextToken()
        elif token == 'getworking':
            if not embed: print(working_dir)
            return working_dir

        # GUI Implementation (Work in progress)
        # DO THIS!!!
        elif token == 'window':
            skip = True
            root = Tk()
            root.title(nextToken())
            root.geometry('300x300')

        # Variables and pseudo-memory management
        elif token == 'stack':
            skip = True
            stack.append(nextToken())
        elif token == 'pop':
            sp = stack.pop()
            if not embed: print(sp)
            return sp
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
        elif token == 'heapget':
            skip = True
            n = nextToken()
            if not embed: print(heap[int(n)])
            return heap[int(n)]
        elif token == 'heapin':
            skip = True
            dubSkip = True
            heap[int(nextToken())] = input(nextnextToken()+'\n')

        # EOF and spacing            
        elif token == '\n':
            continue
        elif token == ';':
            continue
        elif token == '<EOF_TOKEN>':
            break

        # Mathematical Operators
        elif token == 'add':
            try:
                if not embed: print(int(nextToken()) + int(nextnextToken()))
                return int(nextToken()) + int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'multiply':
            try:
                if not embed: print(int(nextToken()) * int(nextnextToken()))
                return int(nextToken()) * int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'subtract':
            try:
                if not embed: print(int(nextToken()) - int(nextnextToken()))
                return int(nextToken()) - int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'divide':
            try:
                if not embed: print(int(nextToken()) / int(nextnextToken()))
                return int(nextToken()) / int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'mod':
            try:
                if not embed: print(int(nextToken()) % int(nextnextToken()))
                return int(nextToken()) % int(nextnextToken())
            except TypeError:
                print('Integers expected')
            except ValueError:
                print('Integers expected')
        elif token == 'power':
            try:
                if not embed: print(int(nextToken()) ** int(nextnextToken()))
                return int(nextToken()) ** int(nextnextToken())
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
                    return parse(coded, embed=embedding)
                except KeyboardInterrupt:
                    sys.exit(0)
            def openrun(file):
                try:
                    if file[-3:] == '.ql' or file[-4:] == '.qcl':
                        f = open(working_dir+file, 'r')
                        return ql(f.read())
                    else:
                        print('Invalid file extension')
                except KeyboardInterrupt:
                    sys.exit(0)
            return openrun(nextToken())
        
        # Nice to quit the program, right?
        # From this I learned that none of this works without <>
        # Example: to exit you must do 'exit <>'
        # This is solved within the shell
        elif token == 'exit':
            sys.exit(0)
                        
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
