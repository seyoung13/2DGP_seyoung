from pico2d import *
import game_framework
import main_state

name = "PauseState"
image = None
counter = 300

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del image


def handle_events():
    evnets = get_events()
    for event in evnets:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    clear_canvas()
    if counter > 100:
        image.draw(400, 300, 100, 100)
    main_state.boy.draw()
    main_state.grass.draw()
    update_canvas()


def update():
    global counter
    counter -= 1
    if counter == 0:
        counter = 300


def pause():
    pass


def resume():
    pass






