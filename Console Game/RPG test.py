import os
from Colors import reset, bg_blue, bg_gray, bg_green, bg_red

def clear():
    print(reset)
    os.system('cls' if os.name == 'nt' else 'clear')

player: dict = {
    "sprite":       "i",       
    "position":       0,       
    "inventory":     [],     
    "health":       100,
    "editor":     False
    }

level: dict = {}

GRID_SIZE = 15

def create_scene(GRID_SIZE):