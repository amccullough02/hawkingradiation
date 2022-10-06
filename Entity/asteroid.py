import pygame

from Entity.entity import Entity


class Asteroid(Entity):
    def __init__(self, x, y, sprite):
        super().__init__()
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, game):
        game.screen.blit(self.sprite, (self.x + game.camera.offsetX, self.y + game.camera.offsetY))

    def draw_collider(self, game):
        pygame.draw.rect(game.screen, (255, 255, 255), self.rect)

    def update(self, game):
        self.rect.x = self.x + game.camera.offsetX
        self.rect.y = self.y + game.camera.offsetY
