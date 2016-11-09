# Congratulations Miles!
# You have officially finished the basic courses!
# We will now be moving on to Networking, which will employ your knowledge of classes and objects

# You are required to know about IPs, ports, TCP, and you need to know that things are separated into client and server
import socket
# This is the networking framework that comes with Python

# Here, we are going to create a socket object, which will be used to do the networking
socketObject = socket.socket()
# There are two parameters here, which you usually set as socket.AF_INET and socket.SOCK_STREAM
# They are set as default, so all we need here is the open-close parentheses

HOST = ''  # We leave this empty so that a client can connect on any relevant IP address
PORT = 37377  # This can be any set of numbers below 65535, but should be at least 4 digits because lower numbers are
# reserved for the system
# These are capitalized because by convention, if you won't change the value they are constants and they are capitalized

socketObject.bind((HOST, PORT)) # We need a tuple here, because it accepts one parameter (the address) but the port
# and host are parts of it

# Finally, we need to open the port
socketObject.listen(5)  # This is the number of connections it can accept at once

# And now it is listening for connections!!!
# Yay!!!


# There is a bit more, though...
while True:
    # This loop is so that someone can always connect
    (connection, address) = socketObject.accept()
    # connection is the connection
    # address is the address
    connection.send(str.encode('This is a message!'))  # Sends the message, but must be encoded
    connection.close()  # Closes the connection
    # This is how you do this!
