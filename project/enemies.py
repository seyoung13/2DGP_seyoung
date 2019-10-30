from pico2d import *
import game_world
import random
from enemy import Enemy


class Enemies:

    enemy = [0, 0]

    def __init__(self):
        self.x, self.y = 0, 0

    def update(self):
        for i in range(2):
            if Enemies.enemy[i] == 0:
                self.x, self.y = random.randint(100, 1100), random.randint(60, 90)
                Enemies.enemy[i] = Enemy(self.x, self.y, 5)
                Enemies.enemy[i] = 1

    def draw(self):
        pass


