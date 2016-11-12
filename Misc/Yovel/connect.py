#!/usr/bin/python3
import socket
import time

s = socket.socket()
HOST = input("IP: ")
PORT = int(input("PORT (recommend 80): "))
count = int(input("REPEAT (recommend 10): "))
buf = int(input("BUFFER (recommend 4096): "))
delay = int(input("DELAY (recommend 1): "))
msg = input("MESSAGE (recommend 'GET'):\n")
time.sleep(0.25)

print("Configuring...")
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Connecting...")
s.connect((HOST, PORT))

for i in range(count):
    print("Sending message...")
    s.send(str.encode(msg))
    print("Receiving response...")
    print(s.recv(buf).decode("UTF-8"))
    time.sleep(delay)
s.close()
print("\nDone!\n")
