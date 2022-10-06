import pygame


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image
        self.width = image.get_width()
        self.height = image.get_height()

    def get_image(self, x, y, width, height, scale=1, colour=(0, 0, 0)):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
