from pico2d import *
import random

class Tile:
    def __init__(self):
        self.image = load_image('grass_block_change.png')
        self.x, self.y = random.randint(60, 1550), random.randint(50, 500)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return 0, 0, 1600 - 1, 50
