import pygame, time, os, random, pygame.freetype
from random import randint
from pygameTest_Functions import *
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('The Dice Game')
GAME_FONT = pygame.freetype.Font("Dice.ttf", 24)
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN:
                startGame()

        if event.type == QUIT:
            running = False

    screen.fill((255,255,255))

    GAME_FONT.render_to(screen, (100, 180), "Welcome to The Dice Game", (0,0,0))
    GAME_FONT.render_to(screen, (140, 240), "Press Enter to Start", (0,0,0))

    pygame.display.flip()

print("quit")
pygame.quit()
