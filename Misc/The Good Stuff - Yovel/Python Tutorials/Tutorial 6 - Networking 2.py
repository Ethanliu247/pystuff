# Yay you got through Networking 1!

# So let's make our server again
import socket
s = socket.socket()
host = ''
port = 37377
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    # I will be using some shortened variables names; last time I was verbose so that it was easier to understand
    conn.send(str.encode('Hello, %s' % addr))
    print(addr)
    msg = conn.recv(1024)  # This is the buffer size of what you receive. It should be in the 1000s and a power of 2
    print(msg.decode('utf-8'))  # If you don't decode the message, you will get a TypeError
    conn.send(str.encode('Message received!'))
    conn.close()

# You can test this inside the terminal by typing the following command:

# telnet localhost 37377

# And that's the basics! There is also a way to create a client program, which is actually simpler than this
del s, conn, addr, msg
# Cleaning up our earlier program
s = socket.socket()
s.connect((host, port))  # Instead of binding and listening, we connect to our tupley address
print(s.recv(1024).decode('utf-8'))  # Prints what the function returns, which will be the message
s.send(str.encode('HALLO'))  # In the client, we use the socket itself to send and receive instead of conn
print(s.recv(1024).decode('utf-8'))
s.close()  # This disconnects the actual socket; don't do this in the server program or you will have problems

# And that is it for networking right now!
# Now we move on to threading! Yay!
