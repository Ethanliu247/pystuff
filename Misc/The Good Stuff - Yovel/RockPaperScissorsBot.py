from time import sleep
import random
rock="rock"
paper="paper"
scissors="scissors"
c=0
lwin=False
rounds = input("How many rounds are there?\n")
choices=[scissors, paper, rock]
rounds = int(rounds)
for i in range(0, rounds):
    ai = input("What is your choice?\n")
    if i == 0:
        choice=rock
    if i == 1 and lwin==False:
        choice=rock
    if i == 1 and lwin==True:
        choice=paper
    if i > 1:
        c+=1
        choice=choices[c-1]
    if c>3:
        c=1
    print("\nRock")
    sleep(1)
    print("Paper")
    sleep(1)
    print("Scissors")
    sleep(1)
    print("Shoot!")
    sleep(0.5)
    print("\nThe StrategyBot chose "+choice)
    print("\nThe LearnMachine chose "+ai)
    sleep(1)
    print("\n")
    if choice==ai:
        print("Tie!")
        lwin=False
    if choice==rock and ai==scissors:
        print("StrategyBot wins!")
        lwin=False
    if choice==paper and ai==scissors:
        print("LearnMachine wins!")
        lwin=True
    if choice==scissors and ai==paper:
        print("StrategyBot wins!")
        lwin=False
    if choice==scissors and ai==rock:
        print("LearnMachine wins!")
        lwin=True
    if ai!=rock and ai!=scissors and ai!=paper:
        print("Choice was not accepted.")
    print("\n")
