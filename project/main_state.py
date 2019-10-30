import random
import json
import os

from pico2d import *

import game_framework
import game_world

from player import Player
from ground import Ground
from background import Background
from pistol import Pistol
from enemy import Enemy

name = "MainState"

background = None
ground = None
player = None
pistol = None
enemy = None
font = None


def enter():
    global player, ground, background, pistol, enemy
    player = Player()
    ground = Ground()
    enemy = Enemy()
    pistol = Pistol()
    background = Background()

    game_world.add_object(enemy, 1)
    game_world.add_object(player, 1)
    game_world.add_object(pistol, 1)
    game_world.add_object(background, 0)
    game_world.add_object(ground, 0)


def exit():
    game_world.clear()


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
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def inRect(left, top, right, bottom, x, y):
    if left < x < right and bottom < y < top:
        return True
    else:
        return False
