import pygame

from Entity.entity import Entity
import math


class Player(Entity):
    def __init__(self, x, y, speed, animation):
        super().__init__()
        self.x = x
        self.y = y
        self.animation = animation

        self.points = 0
        self.health = 1000

        self.rect = self.animation.sprite_array[0].get_rect(center=(self.x + 32, self.y + 32))

        self.mur_check_1 = False
        self.mur_check_2 = False
        self.mul_check_1 = False
        self.mul_check_2 = False
        self.mdr_check_1 = False
        self.mdr_check_2 = False
        self.mdl_check_1 = False
        self.mdl_check_2 = False

        self.moving_up = False
        self.moving_left = False
        self.moving_right = False
        self.moving_down = False

        self.speed = speed
        self.speed_correction = (self.speed - (math.cos(math.radians(45)) * self.speed))

    def draw(self, game):
        self.animation.draw(game.screen, self.x, self.y)

    def draw_collider(self, game):
        pygame.draw.rect(game.screen, (255, 255, 255), self.rect)

    def update(self, game, collideables):
        self.rect = self.animation.sprite_array[0].get_rect(center=(self.x + 32, self.y + 32))
        if self.moving_up:
            game.camera.offsetY += self.speed * game.dt
        if self.moving_down:
            game.camera.offsetY -= self.speed * game.dt
        if self.moving_left:
            game.camera.offsetX += self.speed * game.dt
        if self.moving_right:
            game.camera.offsetX -= self.speed * game.dt
        if self.mul_check_1 and self.mul_check_2:  # Here we subtract some speed when we're moving diagnally, so we don't move faster than if we moved normally.
            game.camera.offsetY += -self.speed_correction * game.dt
            game.camera.offsetX += -self.speed_correction * game.dt
        if self.mur_check_1 and self.mur_check_2:
            game.camera.offsetY += -self.speed_correction * game.dt
            game.camera.offsetX -= -self.speed_correction * game.dt
        if self.mdl_check_1 and self.mdl_check_2:
            game.camera.offsetY -= -self.speed_correction * game.dt
            game.camera.offsetX += -self.speed_correction * game.dt
        if self.mdr_check_1 and self.mdr_check_2:
            game.camera.offsetY -= -self.speed_correction * game.dt
            game.camera.offsetX -= -self.speed_correction * game.dt

        if self.health != 0:
            self.health -= 1
        print("Player Health = " + str(self.health))
        if self.health == 0:
            print("Game Over.")
            pass

        self.animation.update()

        for collideable in collideables:
            if self.rect.colliderect(collideable.rect):
                collideables.remove(collideable)
                self.health += 300


