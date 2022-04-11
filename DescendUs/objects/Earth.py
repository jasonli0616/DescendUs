import pygame
import os

from .. import _globals

class Earth:
    """
    Represents the Earth.
    """

    def __init__(self):
        """
        Create an instance of Earth.
        """

        self.image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'earth.png'))
        self.position = _globals.Earth.REGULAR_POSITION


    def draw(self, surface: pygame.Surface):
        """
        Draw Earth to the screen.

        Automatically detect if the game has been won,
        to plae in correct position on screen.
        """

        # If won, smoothly move Earth to won position
        if _globals.Game.won:
            self._won_position()

        surface.blit(self.image, self.position)


    def _won_position(self):
        """
        If the game is won, move Earth towards the center smoothly.
        """

        speed = 1
        if self.position[1] > _globals.Earth.WON_POSITION[1]:
            self.position = ( self.position[0], self.position[1] - speed )