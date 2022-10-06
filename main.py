import ctypes
import time

import pygame

from Resources.graphics import Graphics
from Scene.scenemanager import SceneManager
from Scene.mainmenu import MainMenu
from Utils.camera import Camera
from Data.constants import Constants

ctypes.windll.user32.SetProcessDPIAware()


class Game:
    def __init__(self):
        self.c = Constants()
        self.g = Graphics()
        self.sm = SceneManager()
        self.camera = Camera()

        pygame.init()
        pygame.mixer.pre_init(frequency=44100, size=16, channels=2, buffer=312)

        self.dt = 0

        self.screen = pygame.display.set_mode((self.c.screen_width, self.c.screen_height), pygame.DOUBLEBUF, vsync=1)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Hawking Radiation")
        self.window_icon = pygame.image.load(self.g.icon)
        pygame.display.set_icon(self.window_icon)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.last_time = time.time()

        self.mm = MainMenu(self)
        self.sm.push(self.mm)  # Pushing here makes sure the object types are consistent.

    def draw_screen(self):
        self.sm.draw(self)

    def check_events(self):
        self.sm.input(self)

    def update(self):
        self.sm.update(self)

    def run(self):
        while True:
            self.check_events()
            self.draw_screen()
            self.update()
            self.dt = self.clock.tick(60) / 1000


if __name__ == "__main__":
    g = Game()
    g.run()
