from Resources.sprite_sheet import SpriteSheet
import pygame


class Graphics:
    def __init__(self):
        self.player = "Assets/player.png"
        self.icon = "Assets/icon.png"
        self.stats = "Assets/stats.png"


class MainMenuAssets:
    # Class variables (we don't need to access them outside of this class (kinda like static variables in Java))
    b_width = 200
    b_height = 75

    def __init__(self):
        self.title = pygame.image.load("Assets/title.png")
        self.mmss = SpriteSheet(pygame.image.load("Assets/menu-atlas.png"))

        self.play = []
        self.play.insert(0, self.mmss.get_image(x=0, y=0, width=MainMenuAssets.b_width, height=MainMenuAssets.b_height))
        self.play.insert(1, self.mmss.get_image(x=0, y=MainMenuAssets.b_height, width=MainMenuAssets.b_width, height=MainMenuAssets.b_height))

        self.settings = []
        self.settings.insert(0, self.mmss.get_image(x=0, y=MainMenuAssets.b_height * 2, width=MainMenuAssets.b_width, height=MainMenuAssets.b_height))
        self.settings.insert(1, self.mmss.get_image(x=0, y=MainMenuAssets.b_height * 3, width=MainMenuAssets.b_width, height=MainMenuAssets.b_height))

        self.exit = []
        self.exit.insert(0, self.mmss.get_image(x=0, y=MainMenuAssets.b_height * 4, width=MainMenuAssets.b_width, height=MainMenuAssets.b_height))
        self.exit.insert(1, self.mmss.get_image(x=0, y=MainMenuAssets.b_height * 5, width=MainMenuAssets.b_width, height=MainMenuAssets.b_height))

        self.background = pygame.image.load("Assets/main-menu-bg.png")

        self.black_hole_ss = SpriteSheet(pygame.image.load("Assets/black-hole-sheet.png"))
        self.bh_frames = []

        for i in range(50):
            self.bh_frames.insert(i - 1, self.black_hole_ss.get_image(x=i * 200, y=0, width=200, height=200, scale=4))

        self.twinkling_star_ss = SpriteSheet(pygame.image.load("Assets/main-menu-star-sheet.png"))
        self.tstar_frames = []

        for i in range(int(self.twinkling_star_ss.get_width() / self.twinkling_star_ss.get_height())):
            self.tstar_frames.insert(i - 1, self.twinkling_star_ss.get_image(x=i * 32, y=0, width=32, height=32, scale=5))


class BackgroundAssets:
    def __init__(self):
        self.background = pygame.image.load("Assets/game-background.png")


class PlayerAssets:
    def __init__(self):
        self.player_ss = SpriteSheet(pygame.image.load("Assets/player-sheet.png"))
        self.player_frames = []

        for i in range(int(self.player_ss.get_width() / self.player_ss.get_height())):
            self.player_frames.insert(i - 1, self.player_ss.get_image(x=i * 64, y=0, width=64, height=64, scale=1))


class Bodies:
    def __init__(self):
        self.asteroid_ss = SpriteSheet(pygame.image.load("Assets/asteroids.png"))
        self.asteroid1 = self.asteroid_ss.get_image(0, 0, 64, 64)
        self.asteroid2 = self.asteroid_ss.get_image(64, 0, 64, 64)
        self.asteroid3 = self.asteroid_ss.get_image(128, 0, 64, 64)
        self.asteroid4 = self.asteroid_ss.get_image(0, 64, 64, 64)
        self.asteroid5 = self.asteroid_ss.get_image(64, 64, 64, 64)
        self.asteroid6 = self.asteroid_ss.get_image(128, 64, 64, 64)

        self.terra_planet_ss = SpriteSheet(pygame.image.load("Assets/terra_planet.png"))
        self.terra_planet_frames = []

        for i in range(int(self.terra_planet_ss.get_width() / self.terra_planet_ss.get_height())):
            self.terra_planet_frames.insert(i - 1, self.terra_planet_ss.get_image(x=i * 80, y=0, width=80, height=80, scale=1))

        self.blue_star_ss = SpriteSheet(pygame.image.load("Assets/blue_star.png"))
        self.blue_star_frames = []

        for i in range(int(self.blue_star_ss.get_width() / self.blue_star_ss.get_height())):
            self.blue_star_frames.insert(i - 1, self.blue_star_ss.get_image(x=i * 160, y=0, width=160, height=160, scale=1))

        self.lava_planet_ss = SpriteSheet(pygame.image.load("Assets/lava_planet.png"))
        self.lava_planet_frames = []

        for i in range(int(self.lava_planet_ss.get_width() / self.lava_planet_ss.get_height())):
            self.lava_planet_frames.insert(i - 1, self.lava_planet_ss.get_image(x=i * 80, y=0, width=80, height=80, scale=1))

        self.ice_planet_ss = SpriteSheet(pygame.image.load("Assets/ice_planet.png"))
        self.ice_planet_frames = []

        for i in range(int(self.ice_planet_ss.get_width() / self.ice_planet_ss.get_height())):
            self.ice_planet_frames.insert(i - 1, self.ice_planet_ss.get_image(x=i * 80, y=0, width=80, height=80, scale=1))

        self.gas_giant_ss = SpriteSheet(pygame.image.load("Assets/gas_giant.png"))
        self.gas_giant_frames = []

        for i in range(int(self.gas_giant_ss.get_width() / self.gas_giant_ss.get_height())):
            self.gas_giant_frames.insert(i - 1, self.gas_giant_ss.get_image(x=i * 240, y=0, width=240, height=240, scale=1))
