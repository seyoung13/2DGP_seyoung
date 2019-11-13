import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
BRICK_VELOCITY_KMPH = 30.0  # Km / Hour
BRICK_VELOCITY_MPM = (BRICK_VELOCITY_KMPH * 1000.0 / 60.0)
BRICK_VELOCITY_MPS = (BRICK_VELOCITY_MPM / 60.0)
BRICK_VELOCITY_PPS = (BRICK_VELOCITY_MPS * PIXEL_PER_METER)

LEFT, RIGHT = 1, -1


class Brick:
    image = None

    def __init__(self):
        if Brick.image is None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = random.randint(400, 1200-1), 200
        self.direction = LEFT

    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.x > 1600-100:
            self.direction = RIGHT
        elif self.x < 100:
            self.direction = LEFT

        self.x += self.direction * BRICK_VELOCITY_PPS * game_framework.frame_time
