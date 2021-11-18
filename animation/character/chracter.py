from pico2d import *


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

class BoyCharacter:
    def __init__(self):
        self.x = 10
        self.y = 150
        self.frame = 0
        self.image = load_image('boyanimation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
            self.image.clip_draw(self.frame*100, 1400, 100, 100, self.x, self.y)
            #self.image.clip_draw(self.frame*100, 600, 100, 100, self.x, self.y)

class Wolf_Monster:
    def __init__(self):
        self.a, self.b = 1200, 150
        self.frame = 0
        self.image = load_image('left_wolf_1_walk.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.a -= 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 100 * 0,100, 100, self.a, self.b)

"""
class Quit:
    def stop(self):
        global  running
        self.events =  get_events()
        for self.event in self.events:
            if self.event.type ==  SDL_QUIT:
                running = False
            elif self.event.type == SDLK_ESCAPE:
                running = False
"""

def handle_events():
    global running
    global running_right
    global jump
    # global x    # x가 뒤에 나와도 상관 없음. 정의만 되어있으면 위치 상관 없다.
    global dir
    global y
    global cy
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:     # 어떤 키가 눌렸는지 확인
            if event.key == SDLK_RIGHT:
                dir += 1        # dir = 1 접근은 안됨
            elif event.key == SDLK_LEFT:
                dir -= 1        # dir = -1 접근은 안됨
            # jump구현
            elif event.key == SDLK_SPACE:
                jump += 1
                y += 100

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:       # dir 값이 0이 되도록 해주기
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_SPACE :
                jump -= 1
                y -= 100

    pass
"""
def update_character():
    global cx, cy
    global t
    global prev_cx, prev_cy

    cx = ((-t**2))*x
    cy = ((-t**2))*y
    pass
    """
open_canvas(KPU_WIDTH, KPU_HEIGHT)
ground = Ground()
background = BackGround()
boy = BoyCharacter()
wolf_monster = Wolf_Monster()
#quit = Quit()

character = load_image('boyanimation.png')
running = True
running_right = True
jumping = False
x = 0
y = 150
#prev_cx = cx
#prev_cy = cy
t= 0

frame = 0
dir = 0
jump = 0
girl_change = 0
boy_change = 0

while running:
    clear_canvas()

    background.draw()
    ground.draw()
    boy.update()
    wolf_monster.update()

    boy.draw()
    wolf_monster.draw()
    """
    if dir > 0:
        character.clip_draw(frame * 100, 100 * 14, 100, 100, x, 150)
    elif dir < 0:
        character.clip_draw(frame * 100, 100 * 6, 100, 100, x, 150)
    # 캐릭터가 움직이지 않을 때 (키보드 손에서 땠을 때 구현)
    elif dir == 0:
        character.clip_draw(frame * 100, 100 * 15, 100, 100, x, 150)
        delay(0.1)

    if jump == 1:
        clear_canvas()
        background.draw()
        ground.draw()
        character.clip_draw(frame * 100, 100 * 10, 100, 100, x, y)
"""
    update_canvas()

    handle_events()     # 여기서 호출해서 위의 함수가 실행
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.01)

# quit.stop()
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