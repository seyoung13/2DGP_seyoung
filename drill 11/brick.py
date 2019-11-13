import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
MUZZLE_VELOCITY_KMPH = 30.0  # Km / Hour
MUZZLE_VELOCITY_MPM = (MUZZLE_VELOCITY_KMPH * 1000.0 / 60.0)
MUZZLE_VELOCITY_MPS = (MUZZLE_VELOCITY_MPM / 60.0)
MUZZLE_VELOCITY_PPS = (MUZZLE_VELOCITY_MPS * PIXEL_PER_METER)

LEFT, RIGHT = 1, -1


class Brick:
    image = None

    def __init__(self):
        if Brick.image is None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = random.randint(400, 1200-1), 200
        self.direction = LEFT

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.x > 1600-50:
            self.direction = RIGHT
        elif self.x < 50:
            self.direction = LEFT

        self.x += self.direction * MUZZLE_VELOCITY_PPS * game_framework.frame_time
