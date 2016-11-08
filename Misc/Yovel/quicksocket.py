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