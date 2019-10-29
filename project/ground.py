from pico2d import *


class Ground:
    def __init__(self):
        self.x, self.y = 600, 30
        self.w, self.h = 1200, 60
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)

    def update(self):
        pass
    
# ground = [Ground() for i in range(2)]
# ground[0].x, ground[0].y, ground[0].w, ground[0].h = 400, 30, 800, 60
# ground[1].x, ground[1].y, ground[1].w, ground[1].h = 1000, 90, 400, 60
