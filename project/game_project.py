from pico2d import *

def attack(x, y):
    bullet.clip_draw(0, 0 , 50, 50, x, y)

def handle_events():
    global running
    global direction, face_direction
    global jump, jump_count
    global fire
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                direction += 1
                face_direction = 1
            elif event.key == SDLK_LEFT:
                direction -= 1
                face_direction = -1
            elif event.key == SDLK_a and fire==0:
                fire=1
            elif event.key == SDLK_s and jump_count==0:
                jump=1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                direction -= 1
            elif event.key == SDLK_LEFT:
                direction += 1


WinWidth, WinHeight=1200, 800
running = True
x = 800 // 2
y = 90
fire=0
frame = 0
direction = 0
face_direction = 1
jump, jump_count=0, 0
bullet_x, bullet_y=0, 0
bullet_delay=200

open_canvas(WinWidth, WinHeight)
grass = load_image('grass.png')
background=load_image('KPU_GROUND_FULL.png')
character = load_image('animation_sheet.png')
bullet=load_image('bullet.png')

while running:
    clear_canvas()
    background.draw(WinWidth, WinHeight)
    grass.draw(400, 30)
    grass.draw(1000, 60, 400, 120)

    if direction == 0:
        if face_direction > 0:
            character.clip_draw(0, 100 * 3, 100, 100, x, y+jump_count)
        elif face_direction < 0:
            character.clip_draw(0, 100 * 2, 100, 100, x, y+jump_count)
    elif direction > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y+jump_count)
    elif direction < 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y+jump_count)

        
    
    if jump==1 and jump_count<100:
        jump_count+=1.5
    if jump_count>=100:
        jump=0
    if jump_count>0 and jump==0:
        jump_count-=1.5

    if fire==0:
        bullet_delay=200
        bullet_direction=face_direction
        bullet_x, bullet_y=x, y+jump_count
    if fire==1:
        attack(bullet_x, bullet_y)
        bullet_x+=bullet_direction*5
        bullet_delay-=1

    if bullet_delay<0:
        fire=0
        
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if 800 < x:
        x = 800
    elif x < 0:
        x = 0
    x += direction * 1.5

close_canvas()
