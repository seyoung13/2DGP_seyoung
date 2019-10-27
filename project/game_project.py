from pico2d import *
import random


class Grass:
    def __init__(self):
        self.w, self.h = 400, 30
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.w, self.h)
        self.image.draw(self.w + 800, self.h + 40)


class Background:
    def __init__(self):
        self.image = load_image('KPU_GROUND_FULL.png')

    def draw(self):
        self.image.draw(WinWidth / 2, WinHeight / 2, WinWidth, WinHeight)


class Player:
    def __init__(self):
        self.x, self.y = random.randint(0, 400), 90
        self.direction, self.face_direction = 0, 1
        self.jumping, self.jump_y, self.jump_count = 0, 0, 0
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        # 이동
        self.x += 0.1 * self.direction
        # 점프
        if self.jumping == 1 and self.jump_count <= 20:
            self.jump_count += 0.1
        if self.jump_count >= 20:
            self.jumping = 0
            self.jump_count = 0
        self.jump_y = -(self.jump_count ** 2) + (20 * self.jump_count)

    def draw(self):
        if self.direction == 0:
            if self.face_direction > 0:
                self.image.clip_draw(0, 100 * 3, 100, 100, self.x, self.y + self.jump_y)
            elif self.face_direction < 0:
                self.image.clip_draw(0, 100 * 2, 100, 100, self.x, self.y + self.jump_y)
        elif self.direction > 0:
            self.image.clip_draw(self.frame * 100, 100 * 1, 100, 100, self.x, self.y + self.jump_y)
        elif self.direction < 0:
            self.image.clip_draw(self.frame * 100, 100 * 0, 100, 100, self.x, self.y + self.jump_y)
        self.x = clamp(25, self.x, 1200 - 25)
        self.x += self.direction * 1.5


class Pistol:
    def __init__(self):
        self.x, self.y = 0, 0
        self.direction = 0
        self.remain = 0
        self.image = load_image('bullet.png')

    def update(self):
        if self.remain == 0:
            self.x, self.y = player.x, player.y + player.jump_y
            self.direction = player.face_direction
        elif self.remain > 0:
            self.x += self.direction * 5
            self.remain -= 0.5
        # 판정
        if enemy.hp > 0 and \
                enemy.x - 10 < self.x < enemy.x + 10 and enemy.y - 50 < self.y < enemy.y + 50:
            self.remain = 0

    def draw(self):
        self.image.clip_draw(0, 0, 60, 60, self.x, self.y, 30, 30)


class Enemy:
    def __init__(self):
        self.x, self.y = random.randint(800, 1100), 150
        self.hp = 5
        self.direction, self.face_direction = 0, 1
        self.jumping, self.jump_y, self.jump_count = 0, 0, 0
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        # 이동
        self.x += 0.1 * self.direction
        # 점프
        if self.jumping == 1 and self.jump_count <= 20:
            self.jump_count += 0.1
        if self.jump_count >= 20:
            self.jumping = 0
            self.jump_count = 0
        self.jump_y = -(self.jump_count ** 2) + (20 * self.jump_count)
        # 판정
        for i in range(pistol_max):
            if self.hp > 0 and \
                    self.x - 10 < pistol[i].x < self.x + 10 and self.y - 50 < pistol[i].y < self.y + 50:
                self.hp -= 1

    def draw(self):
        if self.direction == 0:
            if self.face_direction > 0:
                self.image.clip_draw(0, 100 * 3, 100, 100, self.x, self.y + self.jump_y)
            elif self.face_direction < 0:
                self.image.clip_draw(0, 100 * 2, 100, 100, self.x, self.y + self.jump_y)
        elif self.direction > 0:
            self.image.clip_draw(self.frame * 100, 100 * 1, 100, 100, self.x, self.y + self.jump_y)
        elif self.direction < 0:
            self.image.clip_draw(self.frame * 100, 100 * 0, 100, 100, self.x, self.y + self.jump_y)
        self.x = clamp(25, self.x, 1200 - 25)
        self.x += self.direction * 1.5


def BulletLimit(arr, size, num):
    for i in range(size):
        if arr[i].remain == 0:
            arr[i].remain = num
            return
    return


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            # 이동
            if event.key == SDLK_RIGHT:
                player.direction += 1
                player.face_direction = 1
            elif event.key == SDLK_LEFT:
                player.direction -= 1
                player.face_direction = -1
            # 공격
            elif event.key == SDLK_a:
                BulletLimit(pistol, pistol_max, 200)
            # 점프
            elif event.key == SDLK_s and player.jumping == 0:
                player.jumping = 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.direction -= 1
            elif event.key == SDLK_LEFT:
                player.direction += 1


WinWidth, WinHeight = 1200, 800
running = True

open_canvas(WinWidth, WinHeight)
grass = Grass()
background = Background()

player = Player()
pistol_max = 4
pistol = [Pistol() for i in range(pistol_max)]
enemy = Enemy()

while running:
    clear_canvas()
    handle_events()

    background.draw()
    grass.draw()
    player.draw()
    if enemy.hp > 0:
        enemy.draw()

    for i in range(pistol_max):
        if pistol[i].remain != 0:
            pistol[i].draw()

    player.update()
    if enemy.hp > 0:
        enemy.update()

    for i in range(pistol_max):
        pistol[i].update()

    update_canvas()

close_canvas()
