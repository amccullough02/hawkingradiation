class Scene:  # This is the abstract class we base all other scenes upon.
    def __init__(self, game):
        pass

    def update(self, sm, game):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def input(self, sm, game):
        pass

    def draw(self, sm, game):
        pass
