import pygame
import os

from .. import _globals

class Laser:
    """
    Represents a laser.

    All lasers are stored in DescendUs._globals.Game.lasers
    """

    def __init__(self, start_position, mouse_position):
        """
        Create a laser.

        Determine the shooting angle using mouse angle.

        Parameters
        ----------

        start_position: list[int | float, int | float]
            the position that the laser starts at

        mouse_position: list[int | float, int | float]
            the position that the mouse is at, aka where the
            laser will move to
        """

        self.mouse_position = mouse_position
        self.position = ( mouse_position[0], start_position[1] )
        self.size = (100, 3)
        self.speed = 10
        self.image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'laser.png'))

        self.rect = pygame.Rect(self.position, (self.get_width(), self.get_height()))


    def draw(self, surface: pygame.Surface):
        """
        Draw the laser to the screen.

        Move the laser closer to the mouse point every frame.

        Parameters
        ----------

        surface: pygame.Surface
            the surface to draw the laser onto
        """

        self.position = (self.mouse_position[0], self.position[1] + self.speed)

        # Adjust rect to new position
        self.rect = pygame.Rect(self.position, (self.get_width(), self.get_height()))

        if (self.position[1] > _globals.Window.HEIGHT):
            _globals.Game.lasers.remove(self)

        surface.blit(self.image, self.position)


    def get_width(self):
        return self.image.get_width()


    def get_height(self):
        return self.image.get_height()