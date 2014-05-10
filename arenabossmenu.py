#####################################
#                                   #
#          Arena Boss Code          #
#         By: Mateo Aguirre         #
#         and Calvin Adams          #
#                                   #
#####################################

#Starts up the game
import pygame
from pygame.locals import *
pygame.init()

#Sets the games icon/caption
icon = pygame.image.load('arenaboss_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Arena Boss")

#Loads the screen
screen_length = 1250
screen_width = 720
screen = pygame.display.set_mode([screen_length,screen_width])

#Sets everything on MENU screen
BLACK = 0,0,0
WHITE = 255,255,255

background_color = BLACK
screen.fill(background_color)

title = pygame.image.load('arenaboss_title.png')
screen.blit((title), [450,50])

singleplayer_button = pygame.image.load('arenaboss_singleplayer.png')
screen.blit((singleplayer_button), [100,400])

multiplayer_button = pygame.image.load('arenaboss_multiplayer.png')
screen.blit((multiplayer_button), [500,400])

options_button = pygame.image.load('arenaboss_options.png')
screen.blit((options_button), [900,400])

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
