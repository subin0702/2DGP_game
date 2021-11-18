import random
from pico2d import *
import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Coin:
    image = None

    def __init__(self):
        self.frame = 0
        if Coin.image == None:
            Coin.image = load_image('coin_gold.png')
        self.x, self.y = random.randint(0, 1600-1), 100

    def get_bb(self):
        # fill here
        return self.x -10, self.y - 10, self.x + 10, self.y + 10

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    #fill here for def stop
    def stop(self):
        self.fall_speed = 0
