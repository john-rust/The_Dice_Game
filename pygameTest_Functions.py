import pygame, time, os, random, pygame.freetype
from random import randint
from pygameTest_Functions import *
from pygame.locals import *

def startGame():
    print("start game test complete")





"""
# Typing function
def slow_type(t):
    # Defines typing_speed by amount of letters in text
    if 20 < len(t) < 30:
        typing_speed = 150
    elif len(t) > 30:
        typing_speed = 200
    else:
        typing_speed = 80

    # debug print
    #print("**\nDEBUG:")
    #print("len of slow_type string = {}".format(len(t)))
    #print("typing_speed = {}".format(typing_speed))
    #print("**\n")

    # Writes out each letter at the speed definined by typing_speed
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

# Prints ruleset if called
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
        sepBar()
    else:
        slow_type ("\nWelcome Back!\n")
        sepBar()

# Prints seperation bar
def sepBar():
    time.sleep(.5)
    print("__________________________________________________________________________________________________________________")
    print("__________________________________________________________________________________________________________________\n")
    time.sleep(.5)

# Variable dialog options for responses
dialogOptN = 0
def dialogOpt(dialogOptN):
    dialogOptN = randint(1,4)
    if dialogOptN == 1:
        slow_type("Better Luck Next Time!\n")
    elif dialogOptN == 2:
        slow_type("Were you even trying?\n")
    elif dialogOptN == 3:
        slow_type("Don't worry, you'll get it this time for sure!\n")
    elif dialogOptN == 4:
        slow_type("Has anyone told you they belived in you?\n")
        time.sleep(1)
        slow_type("they lied....\n")
"""
