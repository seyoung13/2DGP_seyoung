from pico2d import *


def handle_events():
    global running
    global dir
    global direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                direction = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                direction = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
frame = 0
dir = 0
direction = 1

while running:
    clear_canvas()
    grass.draw(400, 30)
    if dir == 0:
        if direction > 0:
            character.clip_draw(0, 100 * 3, 100, 100, x, y)
        elif direction < 0:
            character.clip_draw(0, 100 * 2, 100, 100, x, y)
    elif dir > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir < 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if 800 < x:
        x = 800
    elif x < 0:
        x = 0
    x += dir * 0.5

close_canvas()
