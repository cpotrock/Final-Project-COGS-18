"""
Several test functions to ensure the game is running properly.
Will pass silently if found true.
"""

#tests the main module.
def test_oregon_trail():

    #imports the oregon_trail module.
    import oregon_trail
    
    #ensures that it is callable
    #ensures pressing 'a' runs the start_journey function.
    #ensures the game loop ends when the player quits the game.
    assert callable(oregon_trail())
    assert keys[pygame.K_a]
    start_journey()
    assert run == False
    pygame.quit()

#tests the start_journey function.
def test_start_journey():

    #imports the script containing the function.
    import start_journey
    
    #ensures that it is callable.
    #ensures pressing 'c' runs the encounter1 function.
    #ensures the game loop ends when the player quits the game.
    assert callable(start_journey())
    assert keys[pygame.K_c]
    encounter1()
    assert run == False
    pygame.quit()

#tests the encounter1 function.
def test_encounter1():

    #imports the script containing encounter1.
    import encounter1

    #ensures that it is callable.
    #ensures pressing 'd' runs the encounter2 function.
    #ensures pressing 'e' runs the end_lose_e1 function.
    #ensures the game loop ends when the player quits the game.
    assert callable(encounter1())
    assert keys[pygame.K_d]
    encounter2()
    assert keys[pygame.K_e]
    end_lose_e1()
    assert run == False
    pygame.quit()

#tests the end_lose_e1 function.
def test_end_lose_e1():
    
    #imports the script containing end_lose_e1.
    import end_lose_e1

    #ensures that it is callable.
    #ensures the game loop ends when the player quits the game.
    assert callable(end_lose_e1())
    assert run == False
    pygame.quit()

#tests the win_screen function.
def test_win_screen():

    #imports the script containing win_screen.
    import win_screen

    #ensures that it is callable.
    #ensures the game loop ends when the player quits the game.
    assert callable(win_screen())
    assert run == False
    pygame.quit()
