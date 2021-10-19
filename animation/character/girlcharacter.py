from pico2d import *

def handle_events():
    global girl_running
    global girl_running_right
    # global x    # x가 뒤에 나와도 상관 없음. 정의만 되어있으면 위치 상관 없다.
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            girl_running = False
        elif event.type == SDL_KEYDOWN:     # 어떤 키가 눌렸는지 확인
            if event.key == SDLK_RIGHT:
                dir += 1        # dir = 1 접근은 안됨
            elif event.key == SDLK_LEFT:
                dir -= 1        # dir = -1 접근은 안됨
            elif event.key == SDLK_ESCAPE:
                girl_running = False

        elif event.type == SDL_KEYUP:       # dir 값이 0이 되도록 해주기
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

    pass
open_canvas()
girl_character = load_image('girlanimation.png')
girl_running = True
girl_running_right = True
x = 800 // 2
frame = 0
dir = 0
chage = 0

while girl_running:
    clear_canvas()

    if dir > 0:
        girl_character.clip_draw(frame * 100, 100 * 9, 100, 100, x, 90)
    else :
        girl_character.clip_draw(frame * 100, 100 * 11, 100, 100, x, 90)

    update_canvas()

    handle_events()     # 여기서 호출해서 위의 함수가 실행
    frame = (frame + 1) % 9
    x += dir * 5
    delay(0.01)

close_canvas()