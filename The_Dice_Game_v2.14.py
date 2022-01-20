# Import
from random import randint
import os
import time
import sys
import random
from functions import *

# Explains rules for first timers
ruleSet()

# Defining our variables
gameSetDice = 4
game = 0
diceRoll = 0
gameSet = 0

# The game
while game == 0:
    slow_type("Press r to roll!\n")
    if input().lower() == 'r':
        slow_type("\nNow rolling the d{}...\n".format(gameSetDice))
        time.sleep(1.25)
        diceRoll = randint(1,gameSetDice)
        slow_type("You rolled {}\n".format(diceRoll))
        time.sleep(1)
        if diceRoll != gameSetDice:
            slow_type("YOU HAVE FAILED THE DICE GAME!\n")
            dialogOpt(dialogOptN)
            sepBar()
            gameSetDice = 4
        else:
            slow_type("Congratulations! You've made it to the next dice!\n")
            sepBar()
            gameSetDice = gameSetDice + 2
    elif input().lower() == 'q':
        game = 1
    else:
        slow_type("Invalid input try again!\n")
