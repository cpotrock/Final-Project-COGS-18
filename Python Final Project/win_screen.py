def win_screen():

    """
    This function is run from the oregon_trail module.
    It has the same basic pygame components of the main module.
    Gives the player the win screen!
    This is run when the player chooses the correct option from the encounter3 function.

    Input:
        Player closes out the window.

    Output:
        The game loop ends and window closes.
    """

    #Note: All of the same code applies from the main module.
    #Please refer to the main module for more detailed notes on what each line of code does.

    import pygame
    import sys
    import os

    pygame.init()
    screen_width = 800
    screen_height = 600
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Oregon Trail")

    pygame.font.init()
    font_path = os.path.join(os.path.dirname(__file__), 'PixelCowboy.ttf')
    title_font_size = 100
    title_font = pygame.font.Font(font_path, title_font_size)
    normal_font_size = 50
    normal_font = pygame.font.Font(font_path, normal_font_size)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill("white")

        #same code - different text
        text_surface1 = title_font.render('YOU WIN!', True, (0, 0, 0))
        screen.blit(text_surface1, (10, 50))
        text_surface2 = normal_font.render('Though you lost some supplies while', True, (0, 0, 0))
        screen.blit(text_surface2, (10, 200))
        text_surface3 = normal_font.render('crossing the river, you made it with', True, (0, 0, 0))
        screen.blit(text_surface3, (10, 250))
        text_surface4 = normal_font.render("enough to settle with. Well done!", True, (0, 0, 0))
        screen.blit(text_surface4, (10, 300))
        text_surface5 = normal_font.render('Thank you for playing!', True, (0, 0, 0))
        screen.blit(text_surface5, (10, 450))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()