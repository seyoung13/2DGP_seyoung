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


def draw_curve_10_points(p1, p2, p3, p4 ,p5, p6, p7, p8, p9, p10):

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
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p3-p4
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2)*p3[0] + (-3*t**3 + 4*t**2 + t)*p4[0] + (t**3 - t**2)*p5[0])/2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2)*p3[1] + (-3*t**3 + 4*t**2 + t)*p4[1] + (t**3 - t**2)*p5[1])/2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p4-p5
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2)*p4[0] + (-3*t**3 + 4*t**2 + t)*p5[0] + (t**3 - t**2)*p6[0])/2
        y = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2)*p4[1] + (-3*t**3 + 4*t**2 + t)*p5[1] + (t**3 - t**2)*p6[1])/2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p5-p6
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p4[0] + (3*t**3 - 5*t**2 + 2)*p5[0] + (-3*t**3 + 4*t**2 + t)*p6[0] + (t**3 - t**2)*p7[0])/2
        y = ((-t**3 + 2*t**2 - t)*p4[1] + (3*t**3 - 5*t**2 + 2)*p5[1] + (-3*t**3 + 4*t**2 + t)*p6[1] + (t**3 - t**2)*p7[1])/2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p6-p7
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p5[0] + (3*t**3 - 5*t**2 + 2)*p6[0] + (-3*t**3 + 4*t**2 + t)*p7[0] + (t**3 - t**2)*p8[0])/2
        y = ((-t**3 + 2*t**2 - t)*p5[1] + (3*t**3 - 5*t**2 + 2)*p6[1] + (-3*t**3 + 4*t**2 + t)*p7[1] + (t**3 - t**2)*p8[1])/2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p7-p8
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p6[0] + (3*t**3 - 5*t**2 + 2)*p7[0] + (-3*t**3 + 4*t**2 + t)*p8[0] + (t**3 - t**2)*p9[0])/2
        y = ((-t**3 + 2*t**2 - t)*p6[1] + (3*t**3 - 5*t**2 + 2)*p7[1] + (-3*t**3 + 4*t**2 + t)*p8[1] + (t**3 - t**2)*p9[1])/2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p8-p9
    for i in range(0, 100, 3):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p7[0] + (3*t**3 - 5*t**2 + 2)*p8[0] + (-3*t**3 + 4*t**2 + t)*p9[0] + (t**3 - t**2)*p10[0])/2
        y = ((-t**3 + 2*t**2 - t)*p7[1] + (3*t**3 - 5*t**2 + 2)*p8[1] + (-3*t**3 + 4*t**2 + t)*p9[1] + (t**3 - t**2)*p10[1])/2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # draw p9-p10
    for i in range(50, 100, 3):
        t = i / 100
        x = (2*t**2-3*t+1)*p8[0]+(-4*t**2+4*t)*p9[0]+(2*t**2-t)*p10[0]
        y = (2*t**2-3*t+1)*p8[1]+(-4*t**2+4*t)*p9[1]+(2*t**2-t)*p10[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        
#변수 초기화
running=True
KPU_WIDTH, KPU_HEIGHT = 1280, 762
frame=0
x,y=300, 300
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
    
    draw_curve_10_points(points[0], points[1], points[2],points[3], points[4], points[5],points[6], points[7], points[8], points[9])

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()

