def encounter2():

    """
    This function is run from the oregon_trail module.
    It has the same basic pygame components of the main module.
    Gives the player the second encounter of the game.
    Only run after the player chooses the correct option from encounter1.

    Input Options (can only choose one):
    1. Player presses 'f' on their keyboard.
    2. Player presses 'g' on their keyboard.
    3. Player closes out the window.

    Associated Output Options:
    1. The end_lose_e2 function is run.
    2. The encounter3 function is run.
    3. The game loop ends and window closes.
    """

    #Note: All of the same code applies from the main module.
    #Please refer to the main module for more detailed notes on what each line of code does.

    #imports pygame and its system functions, end_lose_e2 function, encounter3 function,
    #and a way to talk to the operating system.
    import pygame
    import sys
    import os
    from end_lose_e2 import end_lose_e2
    from encounter3 import encounter3

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

        #same code as before but different text.
        text_surface1 = normal_font.render('You successfully fought off the', True, (0, 0, 0))
        screen.blit(text_surface1, (10, 10))
        text_surface2 = normal_font.render('wolves and protected your family!', True, (0, 0, 0))
        screen.blit(text_surface2, (10, 60))
        text_surface3 = normal_font.render('As you continue along your journey,', True, (0, 0, 0))
        screen.blit(text_surface3, (10, 110))
        text_surface4 = normal_font.render("however, one of your family members", True, (0, 0, 0))
        screen.blit(text_surface4, (10, 160))
        text_surface5 = normal_font.render('falls violently ill.', True, (0, 0, 0))
        screen.blit(text_surface5, (10, 210))
        text_surface6 = normal_font.render("Press 'f' to continue to the nearest", True, (0, 0, 0))
        screen.blit(text_surface6, (10, 310))
        text_surface7 = normal_font.render('town to buy medicine.', True, (0, 0, 0))
        screen.blit(text_surface7, (10, 360))
        text_surface8 = normal_font.render("Press 'g' to trade supplies with the", True, (0, 0, 0))
        screen.blit(text_surface8, (10, 460))
        text_surface9 = normal_font.render('natives now for their medicine.', True, (0, 0, 0))
        screen.blit(text_surface9, (10, 510))

        keys = pygame.key.get_pressed()

        #if the player presses 'f' on their keyboard, the end_lose_e2 function is run.
        #if the player presses 'g' on their keyboard, the encounter3 function is run.
        if keys[pygame.K_f]:
            end_lose_e2()
        if keys[pygame.K_g]:
            encounter3()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()