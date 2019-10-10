from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 762

def handle_events():
    global running
    global mouse_x, mouse_y
    global char_x, char_y
    global now_x, now_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            now_x, now_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def MakeList(x1, y1, x2, y2):
    global points
    for i in range(0, 10+1, ):
        t=i/10
        x = (1-t)*x1+t*x2
        y = (1-t)*y1+t*y2
        points=[(x, y) for i in range(10)]
        
def character_move(p1, p2):
    for i in range(0, 50+1, ):
        t=i/50
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        character.clip_draw(frame * 100, 100 * face, 100, 100, x, y)


#이미지 로드
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mycursor = load_image('hand_arrow.png')

#변수 초기화
running = True
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
char_x, char_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
now_x, now_y =KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
face=1
n=1
hide_cursor()

#실행
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if abs(mouse_x)-abs(char_x)>0:
        face=1
    else:
        face=0

    MakeList(char_x, char_y, now_x, now_y)
    character_move(points[n-1], points[n])
    delay(0.01)
    n = (n + 1) % 10
    mycursor.clip_draw(0, 0, 60, 60, mouse_x+30, mouse_y-30)  
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()
