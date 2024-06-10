"""
This is the main module for the oregon trail game.
Only requires startup via a terminal.
Opens a new window in which the game is run.
There are a total of 8 scripts, each containing a function that it uses to run.
This module acts as the starting screen from which the game can begin the sequence
of associated functions, based on what the player chooses.

Input Options (can only choose one):
1. Player presses 'a' on their keyboard.
2. Player closes out the window.

Associated Output Options:
1. The start_journey function is run.
2. The game loop ends and window closes.
"""


#imports pygame and its system functions, a way to talk to the operating system, 
#and the start_journey function.
import pygame
import sys
import os
from start_journey import start_journey
from test_functions import test_oregon_trail, test_start_journey, test_encounter1, \
    test_end_lose_e1, test_win_screen

#initializes the game window and tick rate, specifying the window size.
pygame.init()
screen_width = 800
screen_height = 600
clock = pygame.time.Clock()

#creates the game window and the caption that appears at the top.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Oregon Trail")

#imports a custom font (I wanted something pixelated to fit with the theme).
#also creates font size variables that I later use when creating text.
pygame.font.init()
font_path = os.path.join(os.path.dirname(__file__), 'PixelCowboy.ttf')
title_font_size = 100
title_font = pygame.font.Font(font_path, title_font_size)
normal_font_size = 50
normal_font = pygame.font.Font(font_path, normal_font_size)

#creates a variable with the boolean True which is later used to keep the game running.
run = True

#the main loop for the game that allows it to run.
while run:
    
    #an internal loop to end the main game loop when the player closes the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #makes a white background for the game        
    screen.fill("white")
    
    #creates text in the window
    #multiple text surfaces for multiple lines of text, different spacing, and different sizes.
    text_surface1 = title_font.render('Welcome to the', True, (0, 0, 0))
    screen.blit(text_surface1, (10, 100))
    text_surface2 = title_font.render('Oregon Trail!', True, (0, 0, 0))
    screen.blit(text_surface2, (10, 200))
    text_surface3 = normal_font.render("Press 'a' to Start", True, (0, 0, 0))
    screen.blit(text_surface3, (10, 400))
    
    #a pygame method that allows for keyboard or mouse inputs from the player.
    keys = pygame.key.get_pressed()
    
    #if the player presses 'a' on their keyboard, the start_journey function is run
    if keys[pygame.K_a]:
        start_journey()
    
    #updates the game as the player performs inputs (necessary for pygame to run)
    #sets the tick rate at 60 frames per second
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

#quits the game when the player closes the window
pygame.quit()
sys.exit()