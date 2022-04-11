import pygame
import os

from ._Collidable import _Collidable
from ... import _globals

class Ammo(_Collidable):
    """
    Represents an ammo pack.

    Inherits from Collidable abstract class.

    All collidables are stored in DescendUs._globals.Game.collidables
    """

    def __init__(self, position):
        image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'ammo.png'))
        super().__init__(image, position)