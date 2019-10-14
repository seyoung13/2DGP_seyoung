from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 400), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class LargeBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= random.randint(5, 20)

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= random.randint(5, 20)

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()
team = [Boy() for i in range(11)]
num = random.randint(5, 15)
Lballs = [LargeBall() for i in range(num)]
Sballs = [SmallBall() for i in range(20-num)]
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in Lballs:
        if ball.y > 70:
            ball.update()
    for ball in Sballs:
        if ball.y > 70:
            ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in Lballs:
        ball.draw()
    for ball in Sballs:
        ball.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
