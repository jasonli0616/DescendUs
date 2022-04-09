import pygame
from abc import ABC

from ... import _globals
from ... import objects

class _Collidable(ABC):

    def __init__(self, image: pygame.Surface, position):

        self.position = position
        self.image = image
        self.speed = 5

        self.rect = pygame.Rect(self.position, (self.get_width(), self.get_height()))


    def draw(self, surface: pygame.Surface):

        self.position = (self.position[0], self.position[1] - self.speed)

        # Adjust rect to new position
        self.rect = pygame.Rect(self.position, (self.get_width(), self.get_height()))

        # Remove when out of screen
        if self.position[1] < 0:
            _globals.Game.collidables.remove(self)

        surface.blit(self.image, self.position)


    def get_width(self):
        return self.image.get_width()


    def get_height(self):
        return self.image.get_height()


    def has_collided(self, player: objects.Player):
        collided = self.rect.colliderect(player.rect)
        return collided