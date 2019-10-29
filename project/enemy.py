from pico2d import *
import random
from pistol import Pistol


class Enemy:
    def __init__(self):
        self.x, self.y = random.randint(600, 1100), random.randint(50, 150)
        self.hp = 5
        self.direction, self.face_direction = 0, 1
        self.jumping, self.jump_y, self.jump_count = 0, 0, 0
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        # 이동

        # 판정
        #if self.hp > 0 and \
                #self.x - 10 < pistol.x < self.x + 10 and self.y - 50 < pistol.y < self.y + 50:
            #self.hp -= 1
        if self.hp <= 0:
            self.x = random.randint(600, 1100)
            self.y = random.randint(50, 150)
            self.hp = 5

    def draw(self):
        self.image.clip_draw(0, 100 * 2, 100, 100, self.x, self.y + self.jump_y)

        self.x = clamp(25, self.x, 1200 - 25)
