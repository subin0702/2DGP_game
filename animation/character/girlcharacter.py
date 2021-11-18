from pico2d import *
import game_framework
#from monster import Monster

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

class Ground:
    def __init__(self):
        self.image = load_image('ground.png')
    def draw(self):
        self.image.draw(640, 250)

class BackGround:
    def __init__(self):
        self.image = load_image('deep_forest_2.jpg')
    def draw(self):
        self.image.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

class Wolf_Monster:
    def __init__(self):
        self.a, self.b = 1200, 150
        self.frame = 0
        self.image = load_image('left_wolf_1_walk.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.a -= 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 100 * 0,100, 100, self.a, self.b)

def handle_events():
    global girl_running
    global girl_running_right
    # global x    # x가 뒤에 나와도 상관 없음. 정의만 되어있으면 위치 상관 없다.
    global dir
    global jump
    global char_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            girl_running = False
        elif event.type == SDL_KEYDOWN:     # 어떤 키가 눌렸는지 확인
            if event.key == SDLK_RIGHT:
                dir += 1        # dir = 1 접근은 안됨
            elif event.key == SDLK_LEFT:
                dir -= 1        # dir = -1 접근은 안됨
            #jump 구현
            elif event.key == SDLK_SPACE:
                jump += 1
                char_y += 100
            elif event.key == SDLK_ESCAPE:
                girl_running = False

        elif event.type == SDL_KEYUP:       # dir 값이 0이 되도록 해주기
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_SPACE:
                jump -= 1
                char_y -= 100

    pass
open_canvas(KPU_WIDTH, KPU_HEIGHT)
ground = Ground()
background = BackGround()
wolf_monster = Wolf_Monster()

girl_character = load_image('girlanimation.png')
girl_running = True
girl_running_right = True
char_x = 0
char_y = 150
frame = 0
dir = 0
jump = 0

while girl_running:
    wolf_monster.update()
    clear_canvas()

    background.draw()
    ground.draw()
    wolf_monster.draw()

    if dir > 0:
        girl_character.clip_draw(frame * 100, 100 * 9, 100, 100, char_x, 150)
    elif dir < 0:
        girl_character.clip_draw(frame * 100, 100 * 11, 100, 100, char_x, 150)
    # 캐릭터가 움직이지 않을 때 (키보드 손에서 땠을 때 구현)
    elif dir == 0:
        girl_character.clip_draw(frame * 100, 100 * 10, 100, 100, char_x, 150)
        delay(0.3)
    #jump
    if jump == 1:
        clear_canvas()
        background.draw()
        ground.draw()
        girl_character.clip_draw(frame * 100, 100 * 1, 100, 100, char_x, char_y)
        frame = (frame + 1) % 13
        delay(0.03)


    update_canvas()

    handle_events()     # 여기서 호출해서 위의 함수가 실행
    frame = (frame + 1) % 9
    char_x += dir * 5
    delay(0.01)

close_canvas()