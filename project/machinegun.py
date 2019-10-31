from pico2d import *
import game_world
import main_state
import random

class Machine_gun:
    image = None
    image2 = None

    def __init__(self, x=0, y=0, direction=-1, delay=0):
        self.x, self.y = x, y
        self.direction = direction
        self.hit = 0
        self.delay = delay
        self.rand = random.randint(-10, 10)
        if Machine_gun.image is None:
            Machine_gun.image = load_image('machine_gun_bullet.png')
        if Machine_gun.image2 is None:
            Machine_gun.image2 = load_image('machine_gun_bullet2.png')

    def update(self):
        # 이동
        if self.delay > 0:
            self.delay -= 1

        if self.delay == 0:
            self.x += self.direction * 4

        # 화면 밖으로 넘어감
        if self.x < 0 or self.x > 1200:
            game_world.remove_object(self)
        # 적을 맞힘
        elif main_state.inRect(main_state.enemy.x - 10, main_state.enemy.y + 50,
                               main_state.enemy.x + 10, main_state.enemy.y - 50, self.x, self.y+self.rand):
            main_state.enemy.hp -= 1
            main_state.enemy.hit = 1
            game_world.remove_object(self)

    def draw(self):
        if self.direction > 0 and self.delay == 0:
            self.image.clip_draw(0, 0, 100, 100, self.x, self.y+self.rand, 70, 35)
        elif self.direction < 0 and self.delay == 0:
            self.image2.clip_draw(0, 0, 100, 100, self.x, self.y+self.rand, 70, 35)
