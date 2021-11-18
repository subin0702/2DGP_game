from pico2d import *

class backGround:
    def __init__(self):
        self.image = load_image('deep_forest_2.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1600 // 2, 800 // 2)