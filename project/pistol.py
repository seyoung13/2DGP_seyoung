from pico2d import *
import game_world


class Pistol:
    image = None
    max_pistol = 1

    def __init__(self, x=0, y=0, direction=1):
        self.x, self.y = x, y
        self.direction = direction
        self.remain = 200
        if Pistol.image is None:
            Pistol.image = load_image('bullet.png')
        
    def update(self):
        # 이동
        self.x += self.direction * 4
        self.remain -= 0.5
        # 판정

        if self.x < 25 or self.x > 1200 - 25:
            game_world.remove_object(self)
            Pistol.max_pistol -= 1

    def draw(self):
        self.image.clip_draw(0, 0, 60, 60, self.x, self.y, 30, 30)
