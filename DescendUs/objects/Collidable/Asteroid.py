import pygame
import os
import random

from ._Collidable import _Collidable
from ... import _globals

class Asteroid(_Collidable):

    def __init__(self, position):

        image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'asteroid.png'))
        self.size = random.randint(50, 200)
        image = pygame.transform.scale(image, (self.size, self.size))

        super().__init__(image, position)

        self.can_collide = True


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


    def collided_image_change(self):
        """
        Change the asteroid image to explosion on collision.
        """

        self.can_collide = False
        self.image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'explosion.png'))
        self.image = pygame.transform.scale(self.image, (self.size, self.size))