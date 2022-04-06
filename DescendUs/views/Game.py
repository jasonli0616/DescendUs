import pygame
import os

from .. import objects
from .. import _globals


class Game:

    def __init__(self):
        self.rect = pygame.Rect(0, 0, _globals.Window.WIDTH, _globals.Window.HEIGHT)
        self.background = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'background.png'))


    def show(self, surface: pygame.Surface):
        """
        Render the page to the screen.

        Parameters
        ----------

        surface: pygame.Surface
            the surface to render the page onto
        """

        # Set background
        surface.blit(self.background, (0, 0))

        self._draw(surface)
        self._handle_event()


    def _draw(self, surface: pygame.Surface):
        """
        Draw components to the screen.

        This method is private because it is automatically called in Homepage.show()

        Parameters
        ----------

        surface: pygame.Surface
            the surface to render the components onto
        """

        player = objects.Player(surface, self.rect)
        player.draw()


    def _handle_event(self):
        ev = pygame.event.poll()