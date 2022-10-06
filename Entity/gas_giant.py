import pygame

from Entity.entity import Entity


class GasGiant(Entity):
    def __init__(self, x, y, animation):
        super().__init__()
        self.x = x
        self.y = y
        self.animation = animation
        self.rect = self.animation.sprite_array[0].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.height = self.rect.height / 2
        self.rect.width = self.rect.width / 2

    def draw(self, game):
        self.animation.draw(game.screen, self.x + game.camera.offsetX - 60, self.y + game.camera.offsetY - 60)

    def draw_collider(self, game):
        pygame.draw.rect(game.screen, (255, 255, 255), self.rect)

    def update(self, game):
        self.animation.update()
        self.rect.x = self.x + game.camera.offsetX
        self.rect.y = self.y + game.camera.offsetY
