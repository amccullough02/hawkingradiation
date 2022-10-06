from Scene.scene import Scene
from Data.constants import Constants
import pygame


class TransitionScene(Scene):
    def __init__(self, fromScene, toScene, game):
        super().__init__(game)
        self.c = Constants()
        self.currentPercentage = 0
        self.fromScene = fromScene
        self.toScene = toScene

    def update(self, sm, game):
        self.currentPercentage += 4
        if self.currentPercentage >= 100:
            sm.pop()  # Pops itself when the transition is finished.
            if self.toScene is not None:
                sm.push(self.toScene)  # Pushes the next scene onto the stack and displays it.

    def exit(self):
        print("Leaving Transition.")

    def enter(self):
        print("Entering Transition.")

    def input(self, sm, game):
        pass


class FadeTransitionScene(TransitionScene):
    def draw(self, sm, game):
        if self.currentPercentage < 50:
            self.fromScene.draw(sm, game)  # Draw the old scene while transition is only half way complete.
        else:
            if self.toScene is None:
                sm.scenes[-2].draw(sm, game) 
            else:
                self.toScene.draw(sm, game)

        alpha = 255 - int(abs((255 - (255 / 50) * self.currentPercentage)))  # Subtact 510 from 255, and then return an abs value.
        overlay = pygame.Surface((game.screen.get_width(), game.screen.get_height()))
        overlay.set_alpha(alpha)
        overlay.fill(self.c.black)
        game.screen.blit(overlay, (0, 0))
