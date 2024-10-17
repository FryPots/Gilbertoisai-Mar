import os
from Colors import reset, bg_blue, bg_gray, bg_green, bg_red

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

GRID_SIZE = 17
player_pos = 18
tileset = [f"{bg_red}🟫", f"{bg_green}  ", "🌳", f"{bg_gray}  ", "⛺", f"{bg_blue}🟦"]

def add(tile = 1, times = GRID_SIZE):
    tile = str(tile)
    out = ""
    for i in range(times):
        out += tile
    return out

def make_scene():
    grid = ""
    grid += add(2)
    for i in range(GRID_SIZE - 2):
        grid += add(2, 1)
        grid += add(1, GRID_SIZE - 2)
        grid += add(2, 1)
    grid += add(2)
    return grid

def player_tick():
    global player_pos
    key = input()
    
    match key:
        case "w":
            if level[player_pos - GRID_SIZE] != "2":
                player_pos -= GRID_SIZE
        case "a":
            if level[player_pos - 1] != "2":
                player_pos -= 1
        case "s":
            if level[player_pos + GRID_SIZE] != "2":
                player_pos += GRID_SIZE
        case "d":
            if level[player_pos + 1] != "2":
                player_pos += 1
            
    
def draw_scene():
    clear()
    out = reset
    for index in range(len(level)):
        tile_idx = int(level[index])
        if index != 0:
            if index % GRID_SIZE == 0:
                out += "\n"            
        if index != player_pos:
            out += f"{tileset[tile_idx]}{reset}"
            continue
        out += " i"
    print(out)

level = make_scene()

while True:    
    draw_scene()
    player_tick()