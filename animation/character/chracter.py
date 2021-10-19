from pico2d import *

def handle_events():
    global running
    global running_right
    # global x    # x가 뒤에 나와도 상관 없음. 정의만 되어있으면 위치 상관 없다.
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:     # 어떤 키가 눌렸는지 확인
            if event.key == SDLK_RIGHT:
                dir += 1        # dir = 1 접근은 안됨
            elif event.key == SDLK_LEFT:
                dir -= 1        # dir = -1 접근은 안됨
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:       # dir 값이 0이 되도록 해주기
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

    pass
open_canvas()
character = load_image('boyanimation.png')
running = True
running_right = True
x = 800 // 2
frame = 0
dir = 0
chage = 0

while running:
    clear_canvas()

    if dir > 0:
        character.clip_draw(frame * 100, 100 * 14, 100, 100, x, 90)
    else :
        character.clip_draw(frame * 100, 100 * 6, 100, 100, x, 90)

    update_canvas()

    handle_events()     # 여기서 호출해서 위의 함수가 실행
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.01)

close_canvas()
"""
while (x > 30):
    character.clip_draw(frame*100, 600, 100, 100, x, 90)
    update_canvas()
    clear_canvas()
    frame = (frame + 1) % 8
    x -= 5
    delay(0.05)
    get_events()

close_canvas()
"""