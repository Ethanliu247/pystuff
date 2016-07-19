from math import floor
from random import shuffle
def team(classList):
	shuffle(classList)
	print("Team 1:\n", (classList[i] + "\n" for i in range(0, floor(len(classList)/2)), "Team 2:\n", (classList[i] + "\n" for i in range(1 + floor(len(classList)/2)), len(classList)), "The", ("left" if (shuffle([0, 1])[0] == 0) else "right"), "team goes first.")