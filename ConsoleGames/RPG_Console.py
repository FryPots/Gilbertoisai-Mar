import os

player_skin = "🧒"
player_x = 3
player_y = 3
player_coords = [player_x, player_y]
player_inv = []



def clear_terminal():
    os.system("cls")

def drawlevel(n):
    clear_terminal()
    global scene, highline, midline, lowline
    level_info = map
    scene = level_info[1]
    tile_y = len(scene) - 1
    for y in scene:
        row = ""
        tile_x = 0
        for x in y:
            if player_y + 1 == tile_y:
                highline = y
            if player_y - 1 == tile_y:
                lowline = y
            if player_x == tile_x and player_y == tile_y:
                row += player_skin
                midline = y
            else:
                row += x
            tile_x += 1
        print(row)
        tile_y -= 1
    print("Player coordinates: ",player_coords, "\n")
    #print(highline) print(midline) print(lowline)

def inbounds(key):
    max_x = len(midline) - 1
    max_y = (len(scene)-1)
    if player_x == 0:
        if key == "a":
            return False
    if player_x == max_x:
        if key == "d":
            return False
    if player_y == 0:
        if key == "s":
            return False
    if player_y == max_y:
        if key == "w":
            return False
    return True

def check_collition(key):
    if key == "d":
        if midline[player_x + 1] == "🌳":
            return False
    if key == "a":
        if midline[player_x - 1] == "🌳":
            return False
    if key == "w":
        if highline[player_x] == "🌳":
            return False
    if key == "s":
        if lowline[player_x] == "🌳":
            return False
    return True
 
def player_tick():
    global player_x, player_y
    key = input()
    if inbounds(key) == True:
        if check_collition(key) == True:
            if key == "w":
                player_y += 1
            if key == "a":
                player_x -= 1
            if key == "s":
                player_y -= 1
            if key == "d":
                player_x += 1
        player_coords[0] = player_x
        player_coords[1] = player_y

def main():
    drawlevel(0)
    player_tick()
    
while True:
    main()