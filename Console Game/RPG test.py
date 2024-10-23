import os
from Colors import reset, bg_blue, bg_gray, bg_green, bg_red

def clear():
    print(reset)
    os.system('cls' if os.name == 'nt' else 'clear')

GRID_SIZE = 17
player_pos = 18
tileset = [f"{bg_red}🟫", f"{bg_green}  ", "🌳", f"{bg_gray}  ", "⛺", f"{bg_blue}🟦"]
collidable = [tileset[2], tileset[3], tileset[5]]


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
        grid.append(add(2, 1))
        grid.append(add(1, GRID_SIZE - 2))
        grid.append(add(2, 1))
    grid.append(add(2))
    return grid

def player_tick():
    global player_pos, cheat, brush, player_sprite
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
    global level_data
    def read_data():
        out = ""
        tile_idx = 0
        for group in level:
            tile = str(group[0])
            times = (group[1])
            added = ""
            for i in range(times):
                if tile_idx == player_pos:
                    added += "p"
                else:
                    added += tile
                tile_idx += 1
            out += added
        return(out)
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
    player_tick()   
    draw_scene()
    