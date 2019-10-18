from pico2d import *
import game_framework
import main_state

name = "PauseState"
image = None


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
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300, 100, 100)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






