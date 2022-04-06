import pygame
import os

from .. import _globals

class Player:

    def __init__(self, surface: pygame.Surface, page: pygame.Rect):
        """
        Create a player.

        Parameters
        ----------

        text: str
            the text that is displayed
        """

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
        
        The angle of the gun is calculated in self._get_angle()
        """
        self.position = position

        self.image = pygame.transform.rotate(self.image, self._get_angle())

        surface.blit(self.image, position)


    def _get_angle(self):
        """
        Calculate the angle of the gun.

        It should follow the user's mouse, without being exact
        to increase difficulty.

        Formula:
        (mouse x axis / gun x axis) * 100
        """
        mouse_position = pygame.mouse.get_pos()

        return (mouse_position[0] / self.position[0]) * 100