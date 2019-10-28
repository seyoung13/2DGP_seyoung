import random
import json
import os

from pico2d import *

import game_framework

from player import Player
from ground import Ground
from background import Background

name = "MainState"

background = None
ground = None
player = None
font = None


def enter():
    global player, ground, background
    player = Player()
    ground = Ground()
    background = Background()


def exit():
    global player, ground, background
    del player
    del ground
    del background


def pause():
    pass


def resume():
    pass


def handle_events():
    evnets = get_events()
    for event in evnets:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)


def update():
    player.update()


def draw():
    clear_canvas()
    background.draw()
    ground.draw()
    player.draw()
    update_canvas()
