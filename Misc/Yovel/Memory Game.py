#!/usr/bin/python3
import random
from time import sleep

def play():
    numbers = (0,1,2,3,4,5,6,7,8,9)
    playing = True
    plays = 1

    while playing:
        plays+=1
        number = ''
        for i in range(round(plays/2)):
            number = number + str(random.choice(numbers))
        sec = str(len(number)/3+1+(1*round(plays/5)))[:4]
        sleep(1)
        print('The number is '+number+'. Memorize this number. You have '+str(sec)+' seconds.')
        sleep(float(sec))
        print("\n"*100)
        guess = input("What was that number?\n")

        if guess == number:
            print("Correct!!!\n")
        elif guess == 'quit':
            playing = False
            break    
        else:
            print("\nWrong!!!\nThe number was "+number)
            sleep(0.5)
            break

    print("\nYou left with "+str(plays-1)+" points\n")

play()
