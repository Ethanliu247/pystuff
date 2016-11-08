from tkinter import *
from time import sleep
import random
import threading
import sys

money=1
#Starting Money


shares=0
multiplyer=0
managercount=0
dayTicker=None

root=Tk()
root.geometry('900x700')
root.lift()

def tickerUpdate():
    global moneyTicker
    global shopTicker
    global dayTicker
    global multTicker
    global managerTicker
        try:
                del moneyTicker,dayTicker,shopTicker,multTicker,managerTicker
        except:
                pass
        try:
                moneyTicker=Label(root,text='$'+str(money)+' '*50).place(x=10,y=10)
#               dayTicker=Label(root,text='Days Past: '+str(days)).place(x=10,y=200)
                shopTicker=Label(root,text='Shares: '+str(shares)+' '*50).place(x=10,y=100)
                multTicker=Label(root,text='''Increase: %'''+str(multiplyer*5)+' '*50).place(x=500,y=250)
                managerTicker=Label(root,text='Managers: '+str(managercount)+' '*50).place(x=500,y=450)
        except:
                print('Application exited on tickerUpdate() and an error ocurred.')
                sys.exit(-1)
                
def color():
    return random.choice(['red','green','blue','purple','brown','dark grey'])
def buyMax():
    global money
    global shares
    global days
    shares+=float(str(money/10))*100
    money=0
    tickerUpdate()
    if shares>10**3:
            achievment=Label(root,text='You have passed a thousand shares!       ',fg=color()).place(x=100,y=300)
    elif shares>10**6:
            achievment=Label(root,text='You have passed a million shares!        ',fg=color()).place(x=100,y=300)
    elif shares>10**9:
           achievment=Label(root,text='You have passed a billion shares!         ',fg=color()).place(x=100,y=300)
    elif shares>10**12:
            achievment=Label(root,text='You have passed a trillion shares!       ',fg=color()).place(x=100,y=300)
    elif shares>10**15:
            achievment=Label(root,text='You have passed a quadrillion shares!    ',fg=color()).place(x=100,y=300)
    elif shares>10**18:
            achievment=Label(root,text='You have passed a quintillion shares!    ',fg=color()).place(x=100,y=300)
    elif shares>10**21:
            achievment=Label(root,text='You have passed a sextillion shares!     ',fg=color()).place(x=100,y=300)
def getmultiplyer(cost=10):
    global multiplyer
    global money
    if money>=cost:
            multiplyer+=1
            money-=cost
    tickerUpdate()
def use(usedays=True):
    global money
    global shares
    global days
    global multiplyer
    
    money+=0.001*shares*(1+(multiplyer/20))
    if usedays:
            days+=1
    tickerUpdate()
def useManager():
        while True:
            use(usedays=False)
            # Manager Timer
            sleep(0.5)
def buyManager(cost=100):
        global managercount
        global money
        if money >=cost:
                managercount+=1
                money-=cost
                threading.Thread(target=useManager).start()


tickerUpdate()
buyManager(cost=0)

#usebutton=Button(root,text='Another Day',command=use).place(x=500,y=100)
buybuttonMax=Button(root,text='Buy Maximum Shares',command=buyMax).place(x=500,y=10)
buyMulti=Button(root,text='Buy A Multiplyer: $10 for 5% Increase',command=getmultiplyer).place(x=500,y=200)
buyManager=Button(root,text='Buy a Manager: $100 for 2 Clicks/Second',command=buyManager).place(x=500,y=400)

root.mainloop()
