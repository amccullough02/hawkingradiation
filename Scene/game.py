import sys

import pygame

from Entity.asteroid import Asteroid
from Entity.gas_giant import GasGiant
from Entity.planet import Planet
from Entity.star import Star
from Resources.graphics import Graphics, BackgroundAssets, Bodies
from Resources.animations import Animations
from Scene.scene import Scene
from Scene.transition_scene import FadeTransitionScene
from Utils.savestates import Savestates
from Data.constants import Constants
from Entity.player import Player
from UI.health_bar import health_bar


class Game(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.c = Constants()
        self.g = Graphics()
        self.bgassets = BackgroundAssets()
        self.bodies = Bodies()
        self.animations = Animations()

        self.save = Savestates()
        self.save.open_save()

        self.player = Player(self.c.screen_width / 2 - 25, self.c.screen_height / 2 - 25, 300, self.animations.player_animation)
        self.asteroid = Asteroid(500, 400, self.bodies.asteroid1)
        self.test_planet = Planet(1000, 1000, self.animations.terra_animation)
        self.test_star = Star(1000, 500, self.animations.blue_star_animation)
        self.lava_planet = Planet(11000, 1300, self.animations.lava_planet_animation)
        self.ice_planet = Planet(600, 1100, self.animations.ice_planet_animation)
        self.gas_giant = GasGiant(800, 1000, self.animations.gas_giant_animation)

        self.collideables = [self.asteroid, self.test_star, self.test_planet, self.lava_planet, self.ice_planet, self.gas_giant]
        self.player_hb = health_bar(self.c.screen_width / 2, self.c.screen_height - 40, self.player.health / 10, 20, (255, 255, 255))

    def draw(self, sm, game):
        game.screen.fill(self.c.black)
        game.screen.blit(self.bgassets.background, (0 + game.camera.offsetX, 0 + game.camera.offsetY))

        for i in range(len(self.collideables)):
            self.collideables[i].draw(game)

        self.player.draw(game)
        self.player_hb.draw(game)

    def input(self, sm, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save_data()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    sm.pop()
                    sm.push(FadeTransitionScene(self, None, game))  # We pass none as we are not transitiong to a *new* scene.
                    self.save_data()
                if event.key == pygame.K_w:
                    self.player.moving_up = True
                    self.player.mul_check_1 = True
                    self.player.mur_check_1 = True
                    pass
                if event.key == pygame.K_s:
                    self.player.moving_down = True
                    self.player.mdr_check_1 = True
                    self.player.mdl_check_1 = True
                    pass
                if event.key == pygame.K_a:
                    self.player.moving_left = True
                    self.player.mul_check_2 = True
                    self.player.mdl_check_2 = True
                    pass
                if event.key == pygame.K_d:
                    self.player.moving_right = True
                    self.player.mdr_check_2 = True
                    self.player.mur_check_2 = True
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.moving_up = False
                    self.player.mul_check_1 = False
                    self.player.mur_check_1 = False
                    pass
                if event.key == pygame.K_s:
                    self.player.moving_down = False
                    self.player.mdr_check_1 = False
                    self.player.mdl_check_1 = False
                    pass
                if event.key == pygame.K_a:
                    self.player.moving_left = False
                    self.player.mul_check_2 = False
                    self.player.mdl_check_2 = False
                    pass
                if event.key == pygame.K_d:
                    self.player.moving_right = False
                    self.player.mdr_check_2 = False
                    self.player.mur_check_2 = False
                    pass

    def update(self, sm, game):
        self.player.update(game, self.collideables)

        for i in range(len(self.collideables)):
            self.collideables[i].update(game)

        game.camera.check_boundaries()
        self.player_hb.update(self.player)

    def exit(self):
        print("Leaving Game.")

    def enter(self):
        print("Entering Game.")

    def save_data(self):
        self.save.close_save()  # Saving the player's position when we go back to the main menu.
