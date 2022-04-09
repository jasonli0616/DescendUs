import pygame
from abc import ABC

from ... import _globals
from ... import objects

class _Collidable(ABC):
    """
    Abstract class of all collidable objects.

    Children:
        - DescendUs.objects.Collidable.Asteroid
        - DescendUs.objects.Collidable.Ammo
    """

    def __init__(self, image: pygame.Surface, position):
        """
        Create an collidable object.

        Parameters
        ----------

        image: pygame.Surface
            the image of the collidable

        position: list[int | float, int | float]
            the position of the collidable
        """

        self.position = position
        self.image = image
        self.speed = 5

        self.rect = pygame.Rect(self.position, (self.get_width(), self.get_height()))


    def draw(self, surface: pygame.Surface):
        """
        Draw the collidable onto the screen.

        surface: pygame.Surface
            the surface to draw the collidable onto
        """

        self.position = (self.position[0], self.position[1] - self.speed)

        # Adjust rect to new position
        self.rect = pygame.Rect(self.position, (self.get_width(), self.get_height()))

        # Remove when out of screen
        if self.position[1] < 0 - self.get_height():
            _globals.Game.collidables.remove(self)

        surface.blit(self.image, self.position)


    def get_width(self):
        return self.image.get_width()


    def get_height(self):
        return self.image.get_height()


    def has_collided(self, player: objects.Player):
        """
        Check if the player has collided with the player.

        Parameters
        ----------

        player: DescendUs.objects.Player
            the player that has collided with the collidable

        Returns
        ----------

        bool
            whether the player has collided with the collidable
        """

        return self.rect.colliderect(player.rect)