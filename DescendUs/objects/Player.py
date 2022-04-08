import pygame
import os

from .. import _globals
from .. import objects

class Player:

    def __init__(self, surface: pygame.Surface, page: pygame.Rect):
        """
        Create a player.

        Parameters
        ----------

        text: str
            the text that is displayed
        """

        self.ammo = _globals.Game.ammo

        self.image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'player.png'))

        self.page = page
        self.surface = surface
        self.position = ((_globals.Window.WIDTH / 2) - (self.get_width() / 2), 0)

        self.rect = pygame.Rect(self.position, (self.get_width(), self.get_height()))

        self.gun = _Gun()


    def draw(self):
        """
        Draw the button to the screen.

        Parameters
        ----------

        surface: pygame.Surface
            the surface to draw the button onto

        position: list[int | float, int | float]
            the position that the button is at
        """

        mouse_x = pygame.mouse.get_pos()[0]

        self.position = (mouse_x if mouse_x > 0 else 1, self.position[1])

        self.surface.blit(self.image, self.position)
        self.gun.draw(self.surface, (self.position[0], self.get_height() / 3))


    def get_width(self):
        return self.image.get_width()


    def get_height(self):
        return self.image.get_height()


class _Gun:

    def __init__(self):
        """
        Create a gun.

        Automatically load in the image.
        """
        self.image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'gun.png'))


    def draw(self, surface: pygame.Surface, position):
        """
        Draw in the laser gun.
        """
        self.position = position

        surface.blit(self.image, position)


    def shoot_laser(self):
        """
        Shoot the laser towards the mouse position.
        """

        mouse_position = pygame.mouse.get_pos()
        
        laser = objects.Laser(self.position, mouse_position)

        _globals.Game.lasers.append(laser)