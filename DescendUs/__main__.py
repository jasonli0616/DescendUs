"""
-----------------------------------------------------------------------------
Name:        Descend Us
Purpose:     A description of your program goes here.

Author:      Jason Li
Created:     4-Apr-2022
Completed:     
---------------------------------------------------------------------------------------
I think this project deserves a level XXXXXX because ...

Features Added:
See CHANGELOG.md for features.
---------------------------------------------------------------------------------------
"""


import pygame


def setup():
    """
    Initialize the PyGame application.


    Returns
    ----------

    pygame.Surface
        the surface of the application

    pygame.time.Clock
        the application clock

    int
        frames per second

    """
    pygame.init()
    WIDTH, HEIGHT = 400, 400
    FPS = 60

    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    return surface, clock, FPS


def game_loop(surface: pygame.Surface, clock: pygame.time.Clock, FPS: int):
    """
    Main game loop.

    Parameters
    ----------

    surface: pygame.Surface
        the surface of the application

    clock: pygame.time.Clock
        the application clock

    FPS: int
        frames per second

    """

    # Define game loop
    while True:

        # Event handling
        # --------------------

        ev = pygame.event.poll()

        # On close event, end game loop
        if ev.type == pygame.QUIT:
            break


        # Game logic
        # --------------------


        # Draw components to screen
        # --------------------


        # Refresh/frame rate
        # --------------------
        pygame.display.flip()
        clock.tick(FPS)


    # Quit on game loop end
    pygame.quit()



def main():
    surface, clock, FPS = setup()
    game_loop(surface, clock, FPS)


if __name__ == '__main__':
    main()