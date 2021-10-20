from pico2d import *

class Wolf_Monster:
    def __init__(self):
        self.x, self.y = 800, 150
        self.frame = 0
        self.image = load_image('left_wolf_1_walk.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x -= 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 100 * 0,100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(1280, 1024)
wolf_monster = Wolf_Monster()

running = True

while running:
    handle_events()
    wolf_monster.update()

    clear_canvas()
    wolf_monster.draw()
    update_canvas()

    delay(0.05)
"""
x = 800
y = 150
frame = 0
wolf_1_monster = load_image('right_wolf_1_walk.png')
wolf_1_monster_left = load_image('left_wolf_1_walk.png')

while(x > 0):
    clear_canvas()

    wolf_1_monster_left.clip_draw(frame*100, 100 * 0, 100, 100, x, y)
    frame = (frame + 1) % 5
    x -= 5

    update_canvas()

    delay(0.05)

"""
close_canvas()