import socket
import threading

class Socket(socket.socket):
    def __init__(self, HOST='', PORT=37377):
        self.socket = super(Socket, self)
        self.socket.__init__()
        self.HOST=HOST
        self.PORT=PORT
        self.BUFFER=4096
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.c = None
        self.a = None

    def d(self, s):
        return s.decode('utf-8')
    def e(self, s):
        return s.encode('utf-8')

    def sendmsg(self, message):
        self.c.send(self.e(message))
    def sendraw(self, message):
        self.c.send(message)
    def receive(self):
        try:
            return self.d(self.c.recv(self.BUFFER))
        except OSError:
            print('Client exit')
    
    def kill(self):
        self.c.close()
        self.close()

class Server(Socket):
    def __init__(self, PORT=37377, HOST=''):
        super(Server, self).__init__(HOST, PORT)
    def open(self):
        self.bind((self.HOST,self.PORT))
        self.listen(1)
        self.c, self.a = self.accept()
    
class Client(Socket):
    def __init__(self, HOST='localhost', PORT=37377):
        super(Client, self).__init__(HOST, PORT)
    def join(self):
        self.connect((self.HOST, self.PORT))
        
    def sendmsg(self, message):
        self.send(self.e(message+'\n'))
    def sendraw(self, message):
        self.send(message)
    def receive(self):
        return self.d(self.recv(self.BUFFER))
    def kill(self):
        self.close()

from tkinter import *
from time import time, sleep
from sys import exit
from threading import Thread
from datetime import datetime
import random
import encode

log = []

ipp = Tk()
ipp.geometry('250x75+500+200')
ipp.lift()
ipp.title('Setup')
portentry = Entry(ipp)
portentry.grid(row=1, column=0)
portentry.focus()

def ready():
    global PORT
    PORT = int(portentry.get())
    ipp.destroy()

Label(ipp, text='Port').grid(row=1, column=1, sticky=W+N)
doneButton = Button(ipp, text='Open Server', command=ready)
doneButton.place(x=80, y=35)

def ml():
    while True:
        try:
            ipp.update()
            ipp.update_idletasks()
        except TclError:
            return
ml()

server = Server(PORT)
root = Tk()
root.geometry('750x750')
root.title('Chat Room Server')

root.update()
root.update_idletasks()

server.open()

received = Text(root, width=300, height=100, highlightthickness=3, highlightcolor='black', state=DISABLED)
received.place(x=200, y=0)

rbuffer = []
sbuffer = []

userentry = Entry(root)
userentry.place(x=10, y=100)
Label(root, text='Username').place(x=10, y=130)

sendentry = Entry(root)
sendentry.place(x=10, y=0)
userentry.insert(END, 'SERVER')
sendentry.focus()

def write_recv(data, end='\n'):
    global log
    log.append(data+end)
    received.config(state=NORMAL)
    received.insert(END, data+end)
    received.config(state=DISABLED)

def clearchat():
    global STAMPEND
    received.config(state=NORMAL)
    received.delete(STAMPEND, END)
    write_recv('\n~')
    received.config(state=DISABLED)

clearChatButton = Button(root, text='Clear Chat', command=clearchat)
clearChatButton.place(x=10, y=200)

def recieve():
    try:
        data = server.receive()
        rbuffer.append(data.strip())
    except AttributeError:
        write_recv('\nCLIENT EXIT - YOU MAY QUIT')
        root.update()
        root.update_idletasks()

def send(data):
    if data:
        sbuffer.append('<'+userentry.get()+'>  '+data)
        write_recv('<'+userentry.get()+'>  '+data)
    sendentry.delete(0, END)

def flushr():
    global rbuffer
    for i in rbuffer:
        write_recv(i)
    rbuffer = []
def flushs():
    global sbuffer
    for i in sbuffer:
        try:
            Thread(target=lambda: server.sendmsg(i)).start()
        except BrokenPipeError:
            write_recv('CLIENT EXIT - YOU MAY QUIT')
    sbuffer = []
def flush():
    flushr()
    flushs()

def sende():
    ts = sendentry.get()
    send(ts)

send_button = Button(root, text='Send', command=sende)
send_button.place(x=10, y=30)

class PH:
    def __init__(self):
        pass
    def isAlive(self):
        return False

session_id = random.randint(1000000000, 10000000000)

write_recv('Connection:  ', '')
write_recv(server.a[0], ':')
write_recv(str(server.a[1]))
write_recv('Timestamp:  ', '')
write_recv(str(datetime.now())[:-3])
write_recv('SID:  ', '')
write_recv(str(session_id))
write_recv('~')
STAMPEND = str(float(received.search('~', 1.0, END)))

def savelog():
    global log
    filename = 'conv_'+str(session_id)
    data = ''.join(log)+'\n\nExit:  '+str(datetime.now())[:-3]
    f = open(filename, 'w+')
    f.write(encode.encode(data))
    f.close()
    return 0

def mainloop():
    global recvt
    recvt = PH()
    while True:
        try:
            root.update()
            root.update_idletasks()
        except TclError:
            print('Exit')
            server.kill()
            exit()
        finally:
            savelog()
        if not recvt.isAlive():
            recvt = Thread(target=recieve)
            recvt.start()
        flush()
mainloop()
