from pico2d import *

class BoyCharacter:
    def __init__(self):
        self.x, self.y = 0, 30
        self.frame = 0
        self.image = load_image('boyanimation.png')

    def update(self):
        #walking
        self.frame = (self.frame + 1) % 8
        self.x += 5


    def draw(self):
        self.frame = (self.frame*100, 1400, 100, 100, self.x, self.y)
pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
#character = load_image('boyanimation.png')

#x = 0
#frame = 0

#running boy_character

# initializtiion code
open_canvas()

boy = BoyCharacter()

running = True
while (running) :
    handle_events()

    boy.update()

    clear_canvas()
    #character.clip_draw(frame*100, 1400, 100, 100, x, 90)
    #update_canvas()
    #frame = (frame + 1) % 8
    #x += 5
    boy.draw()
    update_canvas()
    delay(0.03)
    get_events()

close_canvas()
"""
class Character:
    def __init__(self):
        self.x, self.y = 0,90
        self.frame = 0
        self.image = load_image('boyanimation.png')

    def update(self):
        self.frame = (self.frame + 1) % 13
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*13, 0,100, 100, self.x, self.y)
    pass

def handle_eventes():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # z키 누르면 태그
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            pass
open_canvas()

character = Character()
running = True

while running:
    handle_eventes()
    clear_canvas()
    # grass.draw(400,30)
    character.draw()
    # x += 2
    update_canvas()

    delay(0.01)
    get_events()

close_canvas()
"""
