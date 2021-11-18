import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
Monster_RUN_SPEED_KMPH = 20.0  # Km / Hour
Monster_RUN_SPEED_MPM = (Monster_RUN_SPEED_KMPH * 1000.0 / 60.0)
Monster_RUN_SPEED_MPS = (Monster_RUN_SPEED_MPM / 60.0)
Monster_RUN_SPEED_PPS = (Monster_RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

Run = range(1)

class RunState:

    def enter(Wolf, event):
        if Wolf.x < 25:
            Wolf.dir = 1
            if Wolf.dir == 1:
                Wolf.velocity += Monster_RUN_SPEED_PPS

        elif Wolf.x > 1500:
            Wolf.dir = -1
            if Wolf.dir == -1:
                Wolf.velocity -= Monster_RUN_SPEED_PPS

        Wolf.dir = clamp(-1, Wolf.velocity, 1)

    def exit(Wolf, event):
        pass

    def do(Wolf):
        #boy.frame = (boy.frame + 1) % 8
        Wolf.frame = (Wolf.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        Wolf.x += Wolf.velocity * game_framework.frame_time
        Wolf.x = clamp(25, Wolf.x, 1600 - 25)

    def draw(Wolf):
        if Wolf.dir == 1:
            Wolf.image.clip_draw(int(Wolf.frame) * 100, 100, 100, 100, Wolf.x, Wolf.y)
        else:
            Wolf.image.clip_draw(int(Wolf.frame) * 100, 0, 100, 100, Wolf.x, Wolf.y)

next_state_table = {
    RunState: { Run: RunState }
}

class Wolf:
    image = None

    def __init__(self):
        self.velocity = 0
        self.frame = 0
        self.cur_state = RunState
        Wolf.dir = 0
        if Wolf.image == None:
            Wolf.image = load_image('left_wolf_1_walk.png')
        self.x, self.y, self.run_speed = random.randint(0, 1600-1), 100, 0
        self.run_speed = Monster_RUN_SPEED_PPS

    def get_bb(self):
        # fill here
        return self.x -10, self.y - 10, self.x + 10, self.y + 10

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    def draw(self):
        self.cur_state.draw(self)
        #self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.run_speed * game_framework.frame_time

    #fill here for def stop
    def stop(self):
        self.run_speed = 0

