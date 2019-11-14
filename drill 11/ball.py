import random
from pico2d import *
import game_world
import game_framework
import main_state

PIXEL_PER_METER = (10.0 / 0.3)
BRICK_VELOCITY_KMPH = 30.0  # Km / Hour
BRICK_VELOCITY_MPM = (BRICK_VELOCITY_KMPH * 1000.0 / 60.0)
BRICK_VELOCITY_MPS = (BRICK_VELOCITY_MPM / 60.0)
BRICK_VELOCITY_PPS = (BRICK_VELOCITY_MPS * PIXEL_PER_METER)

class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(600, 1600 - 1), 60, 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        if self.y < 70:
            self.y = 70

    def stop(self):
        self.fall_speed = 0

    def carrying(self):
        if self.y - 10 > main_state.brick.y:
            self.fall_speed = 0
            self.x += main_state.brick.direction * BRICK_VELOCITY_PPS * game_framework.frame_time


class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
