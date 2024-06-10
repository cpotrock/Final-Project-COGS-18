def end_lose_e1():

    """
    This function is run from the oregon_trail module.
    It has the same basic pygame components of the main module.
    Gives the player the first loss screen of the game.
    This is run when the player chooses the wrong option from the encounter1 function.

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

        #same text code as before, but it describes the losing scenario from encounter1.
        text_surface1 = title_font.render('YOU LOSE', True, (0, 0, 0))
        screen.blit(text_surface1, (10, 50))
        text_surface2 = normal_font.render('Though your attempt to outrun the', True, (0, 0, 0))
        screen.blit(text_surface2, (10, 200))
        text_surface3 = normal_font.render('wolves was valiant, they ultimately', True, (0, 0, 0))
        screen.blit(text_surface3, (10, 250))
        text_surface4 = normal_font.render("caught up to your slow carriage", True, (0, 0, 0))
        screen.blit(text_surface4, (10, 300))
        text_surface5 = normal_font.render('and feasted on you for dinner!', True, (0, 0, 0))
        screen.blit(text_surface5, (10, 350))
        text_surface6 = normal_font.render('Restart and try again!', True, (0, 0, 0))
        screen.blit(text_surface6, (10, 450))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()