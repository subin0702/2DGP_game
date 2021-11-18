import game_framework
from pico2d import *

import title_state


name = "StartState"
image = None
logo_time = 0.0


def enter():    # image 로드해줌
    global image
    image = load_image('kpu_credit.png')
    pass


def exit():     # 끝날때 image를 날림
    global image
    del(image)
    pass


def update():   # logo play time 쌓이다가 1.0이 지나면 종료
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)    # title과 start를 연결해줘야함
    delay(0.01)
    logo_time += 0.01
    pass


def draw():
    global image
    clear_canvas()
    image.draw(1600 // 2, 800 //2)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




