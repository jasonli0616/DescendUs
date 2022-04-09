import pygame
import os

from ._Collidable import _Collidable
from ... import _globals

class Asteroid(_Collidable):

    def __init__(self, position):
        image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'asteroid.png'))
        super().__init__(image, position)


    def has_been_shot(self):
        """
        Check whether the asteroid has been shot.

        Checks the global list of lasers, and
        detects collision with the rect.

        If the asteroid has been shot, return the laser.
        Else, return None.
        """

        for laser in _globals.Game.lasers:
            if self.rect.colliderect(laser.rect):
                return laser