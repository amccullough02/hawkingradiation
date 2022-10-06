from Resources.animation_player import AnimationPlayer
from Resources.graphics import PlayerAssets, Bodies


class Animations:
    def __init__(self):

        self.playerassets = PlayerAssets()
        self.bodies = Bodies()

        self.player_animation = AnimationPlayer(self.playerassets.player_frames, 10, 0)
        self.terra_animation = AnimationPlayer(self.bodies.terra_planet_frames, 10, 0)
        self.blue_star_animation = AnimationPlayer(self.bodies.blue_star_frames, 10, 0)
        self.ice_planet_animation = AnimationPlayer(self.bodies.ice_planet_frames, 10, 0)
        self.lava_planet_animation = AnimationPlayer(self.bodies.lava_planet_frames, 10, 0)
        self.gas_giant_animation = AnimationPlayer(self.bodies.gas_giant_frames, 10, 0)
