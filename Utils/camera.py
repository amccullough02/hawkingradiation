import pygame
from Resources.graphics import BackgroundAssets
from Data.constants import Constants


class Camera:

    def __init__(self):
        self.c = Constants()
        self.g = BackgroundAssets()
        self.offsetX = 0
        self.offsetY = 0

    def check_boundaries(self):
        if self.offsetX > 0:
            self.offsetX = 0
        elif self.offsetX < -(self.g.background.get_width() - self.c.screen_width):
            self.offsetX = -(self.g.background.get_width() - self.c.screen_width)
        if self.offsetY > 0:
            self.offsetY = 0
        elif self.offsetY < -(self.g.background.get_height() - self.c.screen_height):
            self.offsetY = -(self.g.background.get_height() - self.c.screen_height)
