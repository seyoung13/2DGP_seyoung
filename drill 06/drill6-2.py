import random
from pico2d import*


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

            
def draw_curve_3_points(p1, p2, p3):
    for i in range(0, 1000, 4):
        t = i / 1000      
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)


def draw_curve_5_points(p1, p2, p3, p4 ,p5):

    # draw p1-p2
    for i in range(0, 50, 3):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p2-p3
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2


    # draw p3-p4
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2)*p3[0] + (-3*t**3 + 4*t**2 + t)*p4[0] + (t**3 - t**2)*p5[0])/2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2)*p3[1] + (-3*t**3 + 4*t**2 + t)*p4[1] + (t**3 - t**2)*p5[1])/2


    # draw p4-p5
    for i in range(50, 100, 3):
        t = i / 100
        x = (2*t**2-3*t+1)*p3[0]+(-4*t**2+4*t)*p4[0]+(2*t**2-t)*p5[0]
        y = (2*t**2-3*t+1)*p3[1]+(-4*t**2+4*t)*p4[1]+(2*t**2-t)*p5[1]



#변수 초기화
running=True
KPU_WIDTH, KPU_HEIGHT = 1280, 762
frame=0
x,y=300, 300
n=0
count=100
size = 10
points = [(random.randint(0, 1000), random.randint(0, 1000)) for
i in range(size)]

#이미지 로드
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


#실행
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    while(n<8):
        draw_curve_3_points(points[n], points[n+1], points[n+2])
        n+=1
    n=0
    

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()

