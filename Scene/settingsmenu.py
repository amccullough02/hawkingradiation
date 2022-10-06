import sys
from win32api import GetSystemMetrics

import pygame

from Utils import utils
from Scene.scene import Scene
from Scene.transition_scene import FadeTransitionScene
from Data.constants import Constants
from Data.variables import Variables


class SettingsMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.c = Constants()
        self.v = Variables()
        self.width, self.height = GetSystemMetrics(0), GetSystemMetrics(1)

    def draw(self, sm, game):
        game.screen.fill(self.c.black)  # TODO Proper menu buttons + fps options.
        utils.debug_text(game.screen, "Game: [M] to Menu")
        utils.debug_text(game.screen, "Click [F] to toggle Fullscreen", pos=(20, 300))

    def input(self, sm, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    sm.pop()
                    sm.push(FadeTransitionScene(self, None, game))
                if event.key == pygame.K_f:
                    self.v.fullscreen = not self.v.fullscreen
                    if self.v.fullscreen:
                        game.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN, pygame.DOUBLEBUF, vsync=1)
                    else:
                        game.screen = pygame.display.set_mode((self.c.screen_width, self.c.screen_height))

    def exit(self):
        print("Leaving Settings.")

    def enter(self):
        print("Entering Settings.")
