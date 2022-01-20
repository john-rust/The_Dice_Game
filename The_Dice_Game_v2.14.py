# Import
from random import randint
import os
import time
import sys
import random
from dialogOptFun import *

typing_speed = 200 #wpm
charNum = 0

ruleSet() #Explains Rules For First Timers


typing_speed = 80
slow_type("Good Luck!\n\n")
# Giving time to read.
time.sleep(1)
sepBar()
time.sleep(1)

# Defining our variables
gameSetDice = 4
game = 0
diceRoll = 0
gameSet = 0

typing_speed = 120
# The game
while game == 0:
    dialogOptN = 0
    dialogOptN = randint(1,4)
    slow_type("Press r to roll!\n")
    if input().lower() == 'r':
        slow_type("\nNow rolling the d{}...\n".format(gameSetDice))
        time.sleep(1.25)
        diceRoll = randint(1,gameSetDice)
        slow_type("You rolled a {}\n".format(diceRoll))
        time.sleep(1)
        if diceRoll != gameSetDice:
            slow_type("YOU HAVE FAILED THE DICE GAME!\n")
            dialogOpt(dialogOptN)
            time.sleep(.5)
            sepBar()
            time.sleep(1)
            gameSetDice = 4
        else:
            slow_type("Congratulations! You've made it to the next dice!\n")
            time.sleep(.5)
            sepBar()
            time.sleep(1)
            gameSetDice = gameSetDice + 2
    elif input().lower() == 'q':
        time.sleep(1)
        game = 1
    else :
        slow_type("Invalid input try again!\n")
