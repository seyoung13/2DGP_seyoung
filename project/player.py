from pico2d import *
import game_world
import main_state
from pistol import Pistol

# Boy Event
# enum 이랑 비슷 0, 1, 2, 3
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, A_DOWN, S_DOWN, D_DOWN = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_s): S_DOWN,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,
}


# Boy States
class IdleState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
            player.direction = 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
            player.direction = -1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1

    @staticmethod
    def exit(player, event):
        if event == A_DOWN:
            player.shoot()
        if event == S_DOWN and player.jumping == 0:
            player.jumping = 1

    @staticmethod
    def do(player):
        player.jump_y = -(player.jump_count ** 2) + (20 * player.jump_count)
        if player.jumping == 1 and player.jump_count < 20:
            player.jump_count += 0.1
            player.frame = (player.frame + 1) % 8
            player.fy = 0

        if player.jump_count > 20:
            player.jumping = 0
            player.jump_count = 0
            player.fy = 2

    @staticmethod
    def draw(player):
        if player.direction > 0:
            player.image.clip_draw(player.frame * 100, 100 * (player.fy+1), 100, 100, player.x, player.y + player.jump_y)
        elif player.direction < 0:
            player.image.clip_draw(player.frame * 100, 100 * player.fy, 100, 100, player.x, player.y + player.jump_y)


class RunState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
            player.direction = 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
            player.direction = -1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1

    @staticmethod
    def exit(player, event):
        if event == A_DOWN:
            player.shoot()
        if event == S_DOWN and player.jumping == 0:
            player.jumping = 1

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8
        player.x += 2 * player.velocity
        player.x = clamp(25, player.x, 1200 - 25)

        player.jump_y = -(player.jump_count ** 2) + (20 * player.jump_count)
        if player.jumping == 1 and player.jump_count < 20:
            player.jump_count += 0.1

        if player.jump_count > 20:
            player.jumping = 0
            player.jump_count = 0

    @staticmethod
    def draw(player):
        if player.direction > 0:
            player.image.clip_draw(player.frame * 100, 100 * 1, 100, 100, player.x, player.y + player.jump_y)
        elif player.direction < 0:
            player.image.clip_draw(player.frame * 100, 100 * 0, 100, 100, player.x, player.y + player.jump_y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                A_DOWN: IdleState, S_DOWN: IdleState
                },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               A_DOWN: RunState, S_DOWN: RunState
               }
}


class Player:

    def __init__(self):
        self.x, self.y = 200, 90
        self.image = load_image('animation_sheet.png')
        self.frame = 0
        self.fy = 2
        self.direction = 1
        self.velocity = 0
        self.jumping, self.jump_y, self.jump_count = 0, 0, 0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update_state(self):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def shoot(self):
        if Pistol.max_pistol < 4:
            bullet = Pistol(self.x, self.y + self.jump_y, self.direction)
            game_world.add_object(bullet, 1)
            Pistol.max_pistol += 1

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
