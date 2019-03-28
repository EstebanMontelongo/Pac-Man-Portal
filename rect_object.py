from pygame.sprite import Sprite
from pygame import Rect
import pygame


class PacRects(Sprite):
    """General rect object used to create eveything in the game"""
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.image = image
        self.object = pygame.image.load(self.image)

    def scale_image(self, x, y):
        scaled = pygame.transform.scale(self.object, (x, y))
        self.object = scaled
