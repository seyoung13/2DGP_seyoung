import game_framework
from pico2d import *


class Ball:
    image = None

    def __init__(self):
        self.x, self.y = 400, 400
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.existing = True
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

    def get_bb(self):
        if self.existing:
            return self.x-20, self.y-20, self.x+20, self.y+20
        else:
            return -100, -100, -100, -100

    def update(self):
        pass

    def draw(self):
        self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bot
        self.image.clip_draw(0, 0, 21, 21, self.cx, self.cy)

    def set_background(self, bg):
        self.bg = bg

    def touched(self):
        self.existing = False

