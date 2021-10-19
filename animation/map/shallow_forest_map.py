from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

class Ground:
    def __init__(self):
        self.image = load_image('ground.png')
    def draw(self):
        self.image.draw(640, 250)

class BackGround:
    def __init__(self):
        self.image = load_image('shallow_forest.png')
    def draw(self):
        self.image.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

def handle_events():
    global mapping
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            mapping = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            mapping = False

#open_canvas()
open_canvas(1280,1024)
#back_ground = load_image('deep_forest_2.jpg')

ground = Ground()
background = BackGround()

mapping = True

while mapping:
    handle_events()
    clear_canvas()
    background.draw()
    ground.draw()

    update_canvas()

    delay(0.05)

close_canvas()