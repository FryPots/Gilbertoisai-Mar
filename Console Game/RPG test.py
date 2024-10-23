import os
from Colors import reset, bg_blue, bg_gray, bg_green, bg_red

def clear():
    print(reset)
    os.system('cls' if os.name == 'nt' else 'clear')

GRID_SIZE = 17
cheat = 0
brush = 0
player_pos = 18
tileset = [f"{bg_red}🟫", f"{bg_green}  ", "🌳", f"{bg_gray}  ", "⛺", f"{bg_blue}🟦"]

def add(tile = 1, times = GRID_SIZE):
    out = [[tile, times]]
    return out

def make_scene():
    grid = []
    grid += add(2)
    for i in range(GRID_SIZE - 2):
        grid += add(2, 1)
        grid += add(1, GRID_SIZE - 2)
        grid += add(2, 1)
    grid += add(2)
    return grid

def player_tick():
    global player_pos, cheat, brush, player_sprite
    key = input()
    match cheat:
        case 0:
            player_sprite = " i"
        case 1:
            player_sprite = tileset[brush]
    
    def isChar(string, position, c = "2"):
        if position > len(string):
            return False
        if string[position] == c:
            return True
        return False
        
    match key:
        case "w":
                act = (player_pos - GRID_SIZE)
        case "a":
                act = (player_pos - 1)
        case "s":
                act = (player_pos + GRID_SIZE)
        case "d":
                act = (player_pos + 1)
        case "cheat":
            cheat = (cheat + 1) % 2
            input(cheat)
        case _:
            return None
        
    if key in "wasd":
        match isChar(level_data, act):
            case True:
                if cheat == 1:
                    player_pos = act
            case False:
                player_pos = act
        
    
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
    level_data = read_data()
    out = ""
    tile_idx = 0
    for c in level_data:
        if (tile_idx % GRID_SIZE) == 0:
            out += "\n"
        if c.isnumeric():
            out += tileset[int(c)]
        if c == "p":
            out += player_sprite
        out += reset
        tile_idx += 1
    print(out)
            
level = make_scene()

while True:
    player_tick()   
    draw_scene()
    