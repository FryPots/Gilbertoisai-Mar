import os

cursor_sprite = "✏️"
cursor_x = 0
cursor_y = 0

store_scene_data = []
store_scene_name = []

f = open("scenes_data.txt", "a")

def loadscenedata():
    f = open("scenes_data.txt", "r")
    text = f.read()
    raw_data = text.splitlines()
    for 
        

loadscenedata()

tiles = ("　","🌳","🟩")

def clear_terminal():
    os.system("cls")

def printPallete():
    out = ""
    for tile_idx in range(len(tiles)):
        tile = tiles[tile_idx]
        out += f"{tile_idx}.- {tile} "
    print(out)


def createScene(grid_l, name):
    ##creates the level string
    level   =   ""
    level   =   tiles[1] * (grid_l - 1)
    level   +=  tiles[0]
    
    row = 0
    while row < grid_l - 2:
        level   +=  tiles[1]
        level   +=   tiles[2] * (grid_l - 2)
        level   +=  tiles[1]
        row     +=  1
        
    level       +=   tiles[1] * grid_l
    
    ##transforms the string into a list
    tmp_list    =      []
    tile        =      ""
    for tile_idx in range(len(level)):
        
        tile    +=      level[tile_idx]
        if len(tile)    ==     grid_l:
            tmp_list.append(tile)
            tile    =   ""  

    tmp_list = [tmp_list, name]
    store_scene_data.append(tmp_list[0])
    store_scene_name.append(tmp_list[1])

if len(store_scene_name) == 0:
    createScene(9, "overworld:0:0")
    level_name = store_scene_name[0]


def replace(string, string_dir, replacement):
    out = ""
    for char in range(len(string)):
        if char == string_dir:
            out += replacement
        else:    
            out += string[char]
        #print(char, string[string_dir], out)
    return out

        
def printhelp():
    clear_terminal()
    print("""WASD to move cursor. 
    (if a number is typed after wasd, the movement is multiplied my that ammount)\n""")
    
    print("0 - 9 replace a Tile.\n")
    
    print('''type "level" to change scene 
    (creates a new scene if it didnt exist previously).\n''')
    
    print('type "save" to save & exit.\n')
    
    input("Press Enter to continue...")     
        
        
def cursor(key):
    global cursor_y, cursor_x, cursor_sprite, level_name
    speed = 1
    
    if key == "":
        return
    
    if key.isdigit() == True and key.isnumeric() == True:
        key = int(key)
        if key in range(len(tiles)):
            key = tiles[int(key)]
            cursor_sprite = key
            
    elif key == "help":
        printhelp()
        
    elif key == "scene":
        key = (input("Enter the scene name: "))
        
        if key in store_scene_name:
            pass
        
        else:    
            createScene(9, key)
        level_name = key
        
    elif key == "save":
        f = open("scenes_data.txt", "w")
        for i in store_scene_name:
            data_idx = store_scene_name.index(i)
            f.write(f"{i}\n")
            line = ""
            for data_row in store_scene_data[data_idx]:
                for data in data_row:
                    c = tiles.index(data)
                    line += str(c)
            f.write(f"{line}\n")
            
        input()
    else:    
        print(key[0])
        if len(key) == 2:
            if key[1].isdigit() == True and key[1].isnumeric() == True:
                speed = int(key[1])
                key = key[0]
        if key == "w":
            cursor_y += speed
        if key == "s":
            cursor_y -= speed
        if key == "d":
            cursor_x += speed
        if key == "a":
            cursor_x -= speed
        cursor_sprite = "✏️"

def drawlevel(name):

    level_id    =    store_scene_name.index(name)
    level_data  =    store_scene_data[level_id]
    
    line_idx = len(level_data) - 1
    line_order = 0
    
    for line in level_data:
        out_line = line
        if line_idx == cursor_y:
            out_line = replace(line, cursor_x, cursor_sprite)
            if cursor_sprite != "✏️":
                level_data[line_order] = out_line
        
        line_order += 1        
        line_idx -= 1
        print(out_line)
        
        
    print(name)
        
        
def draweditor():
    clear_terminal()
    drawlevel(level_name)
    printPallete()
    print(f"Cursor x:{cursor_x} y:{cursor_y}")


while True:
    draweditor()
    cursor(input("type help for controls: "))