"""
-----------------------------------------------------------------------------
Name:        Descend Us
Purpose:     A description of your program goes here.

Author:      Jason Li
Created:     4-Apr-2022
Completed:   10-Apr-2022
---------------------------------------------------------------------------------------

See README.md for writeup.
See CHANGELOG.md for features added.

---------------------------------------------------------------------------------------
"""


import pygame

from . import views
from . import _globals


def setup():
    """
    Initialize the PyGame application.


    Returns
    ----------

    pygame.Surface
        the surface of the application

    pygame.time.Clock
        the application clock

    """
    pygame.init()

    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((_globals.Window.WIDTH, _globals.Window.HEIGHT))

    pygame.display.set_caption('Descend Us')

    return surface, clock


def game_loop(surface: pygame.Surface, clock: pygame.time.Clock):
    """
    Main game loop.

    Parameters
    ----------

    surface: pygame.Surface
        the surface of the application

    clock: pygame.time.Clock
        the application clock

    """

    # Define game loop
    while True:

        # Event handling
        # --------------------

        ev = pygame.event.poll()

        # On close event, end game loop
        if ev.type == pygame.QUIT:
            break


        # Display view
        # --------------------

        if not _globals.Game.view:
            _globals.Game.view = views.Homepage()

        _globals.Game.view.show(surface)

        # Refresh/frame rate
        # --------------------
        pygame.display.flip()
        clock.tick(_globals.Window.FPS)


    # Quit on game loop end
    pygame.quit()



def main():
    surface, clock = setup()
    game_loop(surface, clock)


if __name__ == '__main__':
    main()