from random import randint
import os
import time
import sys
import random
from os import remove
from sys import argv

typing_speed = 40
charNum = 0

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        charNum += 1
        typing_speed = charNum * 5 + typing_speed
        time.sleep(random.random()*10.0/typing_speed)
    print('')


def ruleSet():
    print("Do you know the rules of The Dice Game? (y/n)\n")
    if input().lower() == 'n':
        # Print game explanation
        slow_type("\nHere are the rules.\n")
        time.sleep(1)
        slow_type("The goal of this game is to roll the maximum number on each dice.\n")
        time.sleep(1)
        slow_type("Starting with the d4, if you do roll the max you moveup to the next dice.\n")
        time.sleep(1)
        slow_type("If you roll anything other than the max you start from the beginning.\n")
        time.sleep(1)
        slow_type("If youre on anything other than the d4 you automaticaly go back to said d4.\n")
        time.sleep(1)
        slow_type("Press q to quit at any time, and dont forget to press enter after each input.\n")
        time.sleep(.75)
    else:
        slow_type ("\nWelcome Back!\n")


def sepBar():
    #Prints Seperations Between Rolls
    print("__________________________________________________________________________________________________________________")
    print("__________________________________________________________________________________________________________________\n")


def dialogOpt(dialogOptN):
    if dialogOptN == 1:
        slow_type("Better Luck Next Time!\n")
    elif dialogOptN == 2:
        slow_type("Were you even trying?\n")
    elif dialogOptN == 3:
        slow_type("Don't worry, you'll get it this time for sure!\n")
    elif dialogOptN == 4:
        slow_type("Has anyone told you they belived in you?\n")
        slow_type("they lied....\n")
