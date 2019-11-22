from pico2d import *
import random


class BigBall:

    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 950), random.randint(100, 950)
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-20, self.y-20, self.x+20, self.y+20


class SmallBall:

    image = None

    def __init__(self):
        self.x, self.y = random.randint(50, 950), random.randint(50, 950)
        if SmallBall.image is None:
            SmallBall.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10
