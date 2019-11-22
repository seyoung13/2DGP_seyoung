import game_framework
from pico2d import *
import game_world

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 30.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.75
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:

    def __init__(self):
        self.x, self.y = 100, 500
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = 0
        self.frame, self.frame_x, self.frame_y = 0, 0, 0

    def update(self):
        self.frame = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frame_x = int(self.frame % 5)
        self.frame_y = int(self.frame / 5)

        if self.x < 100:
            self.dir = 1
        elif self.x > 1500:
            self.dir = -1
        self.velocity = self.dir * FLY_SPEED_PPS

        self.x += self.velocity * game_framework.frame_time

    def draw(self):
        self.image.clip_draw(self.frame_x*180, self.frame_y * 160, 180, 160, self.x, self.y, 100, 100)

