import random
import json
import os

from pico2d import *
import game_framework
import game_world

#heart 오류뜸
#from chracter_life import Heart
from coin import Coin
from boycharacter import Boy
from ground import Grass
from monster_wolf import Wolf
from BackGround import backGround
from tile_1 import Tile
from ball import Ball

name = "MainState"

boy = None
grass = None
back_ground = None
heart = None
balls = None
wolfs = []
tiles = []
coins = []

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a, = a.get_bb()
    left_b, bottom_b, right_b, top_b, = b.get_bb()

    if left_a > right_b : return False
    if right_a > left_b : return False
    if top_a < bottom_b: return False
    if bottom_a > top_b :return False
    return True




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global back_ground
    back_ground = backGround()
    game_world.add_object(back_ground, 0)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global tiles
    tiles = [Tile() for i in range(5)]
    game_world.add_objects(tiles, 0)

    global wolfs
    wolfs = [Wolf() for i in range(random.randint(3, 5))]
    game_world.add_objects(wolfs, 1)

    global coins
    coins = [Coin() for i in range(random.randint(10, 20))]
    game_world.add_objects(coins, 1)
    """
    global balls
    balls = Ball()
    game_world.add_objects(balls, 0)
    
    global birds
    birds = [Bird() for i in range(5)]
    game_world.add_objects(birds, 1)
"""



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    """
    for monster_wolf in wolfs:
         if collide(boy, monster_wolf):
            wolfs.remove(monster_wolf)
            game_world.remove_object(monster_wolf)
    
    # fill here for collision check
    """
    for monster_wolf in wolfs:
        if collide(boy, monster_wolf):
            #print("COLLISION")
            monster_wolf.stop()

    for coin in coins:
        if collide(boy, coin):
            print("COLLISION")
            game_world.remove_object(coin)
"""
        elif collide(balls, monster_wolf):
            print("COLLISION")
            game_world.remove(balls)
            game_world.remove(monster_wolf)
"""
def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






