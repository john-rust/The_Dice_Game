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
game = 0

# The game
while game == 0:
    slow_type("Press r to roll!\n")
    inputLetter = input().lower()
    if inputLetter == 'r':
        rollfunct()
    elif inputLetter == 'q':
        game = 1
    else:
        slow_type("\nInvalid input!\n")
