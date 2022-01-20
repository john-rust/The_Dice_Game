import pygame, time, os, random, pygame.freetype
from random import randint
from Functions import *
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('The Dice Game')
GAME_FONT = pygame.freetype.Font("Dice.ttf", 24)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    # You can use `render` and then blit the text surface ...
    text_surface, rect = GAME_FONT.render("Hello World!", (0, 0, 0))
    screen.blit(text_surface, (40, 250))
    # or just `render_to` the target surface.
    GAME_FONT.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))

    pygame.display.flip()

pygame.quit()
