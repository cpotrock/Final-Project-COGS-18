def start_journey():

    """
    This function is run from the oregon_trail module.
    It has the same basic pygame components of the main module.
    Gives the player a list of instructions on how to play the game.

    Input Options (can only choose one):
    1. Player presses 'c' on their keyboard.
    2. Player closes out the window.

    Associated Output Options:
    1. The encounter1 function is run.
    2. The game loop ends and window closes.
    """

    #Note: All of the same code applies from the main module.
    #Please refer to the main module for more detailed notes on what each line of code does.

    #imports pygame and its system functions, encounter1 function,
    #and a way to talk to the operating system.
    import pygame
    import sys
    import os
    from encounter1 import encounter1

    pygame.init()
    screen_width = 800
    screen_height = 600
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Oregon Trail")

    pygame.font.init()
    font_path = os.path.join(os.path.dirname(__file__), 'PixelCowboy.ttf')
    normal_font_size = 50
    normal_font = pygame.font.Font(font_path, normal_font_size)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill("white")

        #more text surfaces for more text in the window.
        text_surface1 = normal_font.render('Your journey begins on the American', True, (0, 0, 0))
        screen.blit(text_surface1, (10, 50))
        text_surface2 = normal_font.render('frontier. You are journeying with your', True, (0, 0, 0))
        screen.blit(text_surface2, (10, 100))
        text_surface3 = normal_font.render('family to settle out West. On your', True, (0, 0, 0))
        screen.blit(text_surface3, (10, 150))
        text_surface4 = normal_font.render('journey, you will come across various', True, (0, 0, 0))
        screen.blit(text_surface4, (10, 200))
        text_surface5 = normal_font.render('encounters in which you will have to', True, (0, 0, 0))
        screen.blit(text_surface5, (10, 250))
        text_surface6 = normal_font.render('decide what to do.', True, (0, 0, 0))
        screen.blit(text_surface6, (10, 300))
        text_surface7 = normal_font.render("Press 'c' to begin!", True, (0, 0, 0))
        screen.blit(text_surface7, (10, 500))

        keys = pygame.key.get_pressed()
        
        #if the player presses 'c' on their keyboard, the encounter1 function is run
        if keys[pygame.K_c]:
            encounter1()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()