import pygame


class Button:
    def __init__(self, width, height, sprites):
        self.width = width
        self.height = height
        self.sprites = sprites

    def isOver(self, pos, x, y):
        if x < pos[0] < x + self.width:
            if y < pos[1] < y + self.height:
                return True

        return False

    def draw(self, screen, x, y):
        screen.blit(self.sprites[0], (x, y))  # Drawing the button.

    def draw_activated(self, screen, x, y):
        screen.blit(self.sprites[1], (x, y))  # Drawing the activated version of the button.
