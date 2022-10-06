import pygame


class health_bar(object):
    """A health bar class to represent an entities health."""

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.padding = 10

    def draw(self, game):
        pygame.draw.rect(game.screen, (255, 255, 255), pygame.Rect(166, 491, 618, 38))
        pygame.draw.rect(game.screen, (0, 0, 0), pygame.Rect(self.x - self.padding, self.y - self.padding / 2, 300 + self.padding, self.height + self.padding))
        pygame.draw.rect(game.screen, (0, 0, 0), pygame.Rect(self.x - 300 - self.padding, self.y - self.padding / 2, 300 + self.padding, self.height + self.padding))
        pygame.draw.rect(game.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(game.screen, self.colour, pygame.Rect(self.x - self.width + 1, self.y, self.width, self.height))

    def update(self, player):
        self.width = player.health / 10
