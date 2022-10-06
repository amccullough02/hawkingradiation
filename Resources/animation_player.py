import pygame


class AnimationPlayer:
    def __init__(self, sprite_array, anim_speed, animation_index=0):
        self.sprite_array = sprite_array
        self.animation_index = animation_index
        self.animation_delay_counter = 0
        self.animation_speed = anim_speed
        self.frame_num = len(self.sprite_array) - 1

    def draw(self, screen, x, y):
        screen.blit(self.sprite_array[self.animation_index], (x, y))

    def update(self):
        if self.animation_delay_counter < self.animation_speed:
            self.animation_delay_counter += 1
        else:
            if self.animation_index < self.frame_num:
                self.animation_index += 1
            else:
                self.animation_index = 0
            self.animation_delay_counter = 0
