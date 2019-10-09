from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mouse_x, mouse_y
    global char_x, char_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            char_x, char_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def character_move(p1, p2):
    for i in range(0, 50+1, 2):
        t=i/50
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, p1, p2)

#이미지 로드
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mycursor = load_image('hand_arrow.png')

#변수 초기화
running = True
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
char_x, char_y =200, 200
frame = 0
size=5
points=[(char_x, char_y), (mouse_x, mouse_y)]
hide_cursor()

#실행
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    
    character_move(points[0],  points[1])
    mycursor.clip_draw(0, 0, 60, 60, mouse_x+30, mouse_y-30)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
