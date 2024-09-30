import os

def clear_terminal():
    os.system("cls")

tiles = ["　","🌳","🟩"]

export = []

scenes_name=[]
scenes_data=[]

player_sprite = "🧝"
player_x = 1
player_y = 1  

editor = 0
        
def create_scene(name, size):
    global level_name
    level_name = name
    level_string = ""
    
    def add(tile_id = 0,amount = 1):
        out = ""
        tile_id = str(tile_id)
        for times in range(amount):
            out += tile_id
        return out
    
    level_string += add(1,size)
    for times in range(size - 2):
        level_string += add(1)
        level_string += add(2,size - 2)
        level_string += add(1)
    level_string += add(1,size)
    
    scenes_name.append(name)
    scenes_data.append([size,level_string])

def drawlevel(name):
    clear_terminal()
    level_id = scenes_name.index(name)
    grid_data = scenes_data[level_id]
    grid_size = grid_data[0]
    
    grid_string = (grid_data[1])
    
    line = 0
    cycle = 0
    out = ""
    for c in grid_string:
        if cycle == (grid_size):
            out += "\n"
            line += 1
            cycle = 0
            
        if player_y == line and player_x == cycle:
            out += player_sprite
        else:
            out += tiles[int(c)]
        cycle += 1
        
    print(out)
    print(name)
    
def player_tick():
    global player_sprite,editor,level_name
    level_id = scenes_name.index(level_name)
    grid_data = scenes_data[level_id]
    grid_string = (grid_data[1])
    grid_size = int(grid_data[0])
    
    
    key = input()
                
    
    def collition():
        global player_x, player_y
        
        player_string_y = (player_y * grid_size)
        player_in_string = player_string_y + player_x 

        
        if key == "d":    
            if grid_string[player_in_string + 1] == "2":
                return True
        if key == "a":
            if grid_string[player_in_string - 1] == "2":
                return True
        if key == "w":
            if grid_string[player_in_string - grid_size] == "2":
                return True
        if key == "s":
            if grid_string[player_in_string + grid_size] == "2":
                return True
        return False
    
    def movement():
        global player_x, player_y, player_sprite
        if key == "w":
            player_y -= 1
        if key == "a":
            player_x -= 1
        if key == "s":
            player_y += 1
        if key == "d":
            player_x += 1
        if editor == 0:
            player_sprite = "🧝"
            
        else:
            player_sprite = "✏️"
            
    def edit(key):
        global player_sprite
        level_id = scenes_name.index(level_name)
        grid_data = scenes_data[level_id]
        grid_string = (grid_data[1])
        grid_size = int(grid_data[0])
        
        player_string_y = (player_y * grid_size)
        player_in_string = player_string_y + player_x
                
        if key.isnumeric() == True and key.isdigit() == True:
            key = int(key)
            if key in range(len(tiles)):
                old_grid = grid_string
                grid_string = old_grid[:(player_in_string)]
                grid_string += str(tiles.index(tiles[key]))
                grid_string += old_grid[(player_in_string + 1): ]
                
                scenes_data[level_id] = [grid_size, grid_string]
                
    if key == "warp":
        key = input("Scene_name: ")
        if key in scenes_name:
            level_name = key
        else:
            create_scene(key,13)
        
    if key == "editor":
        editor += 1
        editor = editor % 2
        
    if key == "save":
        f = open("scenes.txt", "w")
        for index in range(len(scenes_name)):
            out = f"{scenes_name[index]}\n"
            print(out)
            input()
            f.write(out)
            f.write(f"{str(scenes_data[index])}\n")       
                
    
    walkable = collition()
    
    if editor > 0:
        walkable = True
        edit(key)
        
    if walkable == True:
        movement()
    
f = open("scenes.txt", "a")
f = open("scenes.txt", "r")
read = (f.read()).splitlines()
if len(read) > 1:
    print(read)
    for val in range(0, (len(read)), 2):
        scenes_name.append(read[val])
        scenes_data.append(list(read[val + 1]))
    level_name = scenes_name[0]
else:
    create_scene("overworld:0:0", 13)


while True:
    drawlevel(level_name)
    print(editor)
    print(player_x, player_y)
    player_tick()
    
    
