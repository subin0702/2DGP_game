from pico2d import *

open_canvas()
character = load_image('boyanimation.png')

x = 0
frame = 0

while (x > 30):
    character.clip_draw(frame*100, 1400, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.03)
    get_events()

close_canvas()