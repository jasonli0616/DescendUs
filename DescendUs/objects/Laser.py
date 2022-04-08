import pygame
import os
import math

from .. import _globals

class Laser:

    def __init__(self, start_position, mouse_position):
        """
        Create a laser.

        Determine the shooting angle using mouse angle.
        """

        self.mouse_position = mouse_position
        self.position = ( mouse_position[0], start_position[1] )
        self.size = (100, 3)


    def draw(self, surface: pygame.Surface):
        """
        Draw the laser to the screen.

        Move the laser closer to the mouse point every frame.
        """

        self.position = (self.mouse_position[0], self.position[1] + 10)

        if (self.position[1] > _globals.Window.HEIGHT):
            _globals.Laser.lasers.remove(self)

        rect_surface = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'laser.png'))

        surface.blit(rect_surface, self.position)