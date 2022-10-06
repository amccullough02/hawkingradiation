import sys

import pygame

from Resources.animation_player import AnimationPlayer
from Resources.graphics import Graphics, MainMenuAssets
from Scene.game import Game
from Scene.scene import Scene
from Scene.settingsmenu import SettingsMenu
from Scene.transition_scene import FadeTransitionScene
from UI.button import Button
from Data.constants import Constants


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.c = Constants()
        self.g = Graphics()
        self.mmg = MainMenuAssets()
        self.pos = (0, 0)

        self.black_hole = AnimationPlayer(self.mmg.bh_frames, 3)
        self.twinkle_star = AnimationPlayer(self.mmg.tstar_frames, 20, 5)

        self.play_button = Button(200, 75, self.mmg.play)
        self.settings_button = Button(200, 75, self.mmg.settings)
        self.exit_button = Button(200, 75, self.mmg.exit)

    # Helper Methods

    def draw_UI(self, game):
        if self.play_button.isOver(self.pos, game.screen.get_width() / 2 - 100, game.screen.get_height() / 3):
            self.play_button.draw_activated(game.screen, game.screen.get_width() / 2 - 100, game.screen.get_height() / 3)
        else:
            self.play_button.draw(game.screen, game.screen.get_width() / 2 - 100, game.screen.get_height() / 3)

        if self.settings_button.isOver(self.pos, game.screen.get_width() / 2 - 100, game.screen.get_height() / 2):
            self.settings_button.draw_activated(game.screen, game.screen.get_width() / 2 - 100, game.screen.get_height() / 2)
        else:
            self.settings_button.draw(game.screen, game.screen.get_width() / 2 - 100, game.screen.get_height() / 2)

        if self.exit_button.isOver(self.pos, game.screen.get_width() / 2 - 100, game.screen.get_height() / 1.5):
            self.exit_button.draw_activated(game.screen, game.screen.get_width() / 2 - 100, game.screen.get_height() / 1.5)
        else:
            self.exit_button.draw(game.screen, game.screen.get_width() / 2 - 100, game.screen.get_height() / 1.5)

    def draw(self, sm, game):  # We pass in sm to refer to the scene manager instance we pass this class through.
        game.screen.fill(self.c.black)
        game.screen.blit(self.mmg.background, (0, 0))
        self.black_hole.draw(game.screen, game.screen.get_width() / 2 - self.mmg.bh_frames[0].get_width() / 2, game.screen.get_height() / 2 - self.mmg.bh_frames[0].get_height() / 2)
        self.twinkle_star.draw(game.screen, 40, 40)
        game.screen.blit(self.mmg.title, (game.screen.get_width() / 2 - 450, game.screen.get_height() / 24))
        self.draw_UI(game)

    def update(self, sm, game):
        self.black_hole.update()
        self.twinkle_star.update()

    def input(self, sm, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    sm.push(FadeTransitionScene(self, Game(game), game))
                if event.key == pygame.K_s:
                    sm.push(FadeTransitionScene(self, SettingsMenu(game), game))
                if event.key == pygame.K_q:
                    sys.exit(0)
            if event.type == pygame.MOUSEMOTION:
                self.pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.play_button.isOver(self.pos, game.screen.get_width() / 2 - 100, game.screen.get_height() / 3):
                    sm.push(FadeTransitionScene(self, Game(game), game))
                if self.settings_button.isOver(self.pos, game.screen.get_width() / 2 - 100, game.screen.get_height() / 2):
                    sm.push(FadeTransitionScene(self, SettingsMenu(game), game))
                if self.exit_button.isOver(self.pos, game.screen.get_width() / 2 - 100, game.screen.get_height() / 1.5):
                    sys.exit(0)
            if event.type == pygame.VIDEORESIZE:
                game.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE, pygame.DOUBLEBUF, vsync=1)

    def exit(self):
        print("Leaving Main Menu.")

    def enter(self):
        print("Entering Main Menu.")
