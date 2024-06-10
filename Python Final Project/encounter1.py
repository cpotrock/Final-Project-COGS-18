def encounter1():

    """
    This function is run from the oregon_trail module.
    It has the same basic pygame components of the main module.
    Gives the player the first encounter of the game, for which they must choose what to do.

    Input Options (can only choose one):
    1. Player presses 'd' on their keyboard.
    2. Player presses 'e' on their keyboard.
    3. Player closes out the window.

    Associated Output Options:
    1. The encounter2 function is run.
    2. The end_lose_e1 function is run.
    3. The game loop ends and window closes.
    """

    #Note: All of the same code applies from the main module.
    #Please refer to the main module for more detailed notes on what each line of code does.

    #imports pygame and its system functions, the function for the second encounter, 
    #a way to talk to the operating system, and the function for the first loss screen.
    import pygame
    import sys
    import os
    from end_lose_e1 import end_lose_e1
    from encounter2 import encounter2

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

        #different text, but otherwise, the same code.
        text_surface1 = normal_font.render('After traveling for several days,', True, (0, 0, 0))
        screen.blit(text_surface1, (10, 50))
        text_surface2 = normal_font.render('your family encounters a pack of', True, (0, 0, 0))
        screen.blit(text_surface2, (10, 100))
        text_surface3 = normal_font.render('hungry wolves! You have two choices:', True, (0, 0, 0))
        screen.blit(text_surface3, (10, 150))
        text_surface4 = normal_font.render("Press 'd' to use your rifle and", True, (0, 0, 0))
        screen.blit(text_surface4, (10, 300))
        text_surface5 = normal_font.render('fight off the wolves.', True, (0, 0, 0))
        screen.blit(text_surface5, (10, 350))
        text_surface6 = normal_font.render("Press 'e' to outrun the wolves with", True, (0, 0, 0))
        screen.blit(text_surface6, (10, 450))
        text_surface7 = normal_font.render('your carriage.', True, (0, 0, 0))
        screen.blit(text_surface7, (10, 500))

        keys = pygame.key.get_pressed()

        #if the player presses 'd' on their keyboard, the encounter2 function is run.
        #if the player presses 'e' on their keyboard, the end_lose_e1 function is run.
        if keys[pygame.K_d]:
            encounter2()
        if keys[pygame.K_e]:
            end_lose_e1()
            
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()