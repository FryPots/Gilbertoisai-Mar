import os
from Colors import reset, bg_blue, bg_gray, bg_green, bg_red

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

GRID_SIZE = 15
player_pos = 18
tileset = [f"{bg_red}🟫", f"{bg_green}  ", "🌳", f"{bg_gray}  ", "⛺", f"{bg_blue}🟦"]
collidable = [tileset[2], tileset[3], tileset[5]]


def add(tile = 1, times = GRID_SIZE):
    out = [tile, times]
    return out

def make_scene():
    grid = []
    grid.append(add(2))
    for i in range(GRID_SIZE - 2):
        grid.append(add(2, 1))
        grid.append(add(1, GRID_SIZE - 2))
        grid.append(add(2, 1))
    grid.append(add(2))
    return grid

def player_tick():
    global player_pos
    key = input()
    
    def control(char):   
        if char in "wasd":
                match char:
                    case "w":
                        move_to = player_pos - GRID_SIZE
                    case "a":
                        move_to = player_pos - 1
                    case "s":
                        move_to = player_pos + GRID_SIZE
                    case "d":
                        move_to = player_pos + 1
                    case _:
                        move_to = player_pos
                return move_to
        
    def collition(enabled = 1):
        out = control(key)
        if enabled == 1:
            check_tile = int(level[out])
            if tileset[check_tile] in collidable:
                return player_pos
        return out
    
    # player_pos = collition()
            
    
def draw_scene():
    out = reset
    clear()
    for group in level:
        tile = group[0]
        times = group[1]
        for tile_idx in range(times):
            out += tileset[tile]
        
level = make_scene()

while True:    
    draw_scene()
    player_tick()