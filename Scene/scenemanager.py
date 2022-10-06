import pygame


class SceneManager:
    def __init__(self):
        self.scenes = []

    def input(self, game):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self, game)  # Refers to the instance of the game class we create in the main folder.

    def update(self, game):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self, game)

    def draw(self, game):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, game)
        pygame.display.update()

    def sceneExit(self):
        if len(self.scenes) > 0:
            self.scenes[-1].exit()

    def sceneEnter(self):
        if len(self.scenes) > 0:
            self.scenes[-1].enter()

    def pop(self):
        self.sceneExit()
        self.scenes.pop()
        self.sceneEnter()
        print(self.scenes)

    def push(self, scene):
        self.sceneExit()
        self.scenes.append(scene)
        self.sceneEnter()
        print(self.scenes)

    def set(self, scene):
        while len(self.scenes) > 0:
            self.pop()
        for s in self.scenes:
            self.push(s)
