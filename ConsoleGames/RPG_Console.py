import os
import subprocess


player_x = 4
player_y = 4
player = ["🧒",[player_x, player_y]]
player_coords = player[1]
player_skin = player[0]

levels = [["🌳🌳🌳🌳🌳🌳🌳",
           "🌳🟩🟩🟩🟩🟩🌳",
           "🌳🟩🌳🟩🟩🟩🌳",
           "🌳🟩🟩🟩🌳🟩🌳",
           "🌳🌳🟩🟩🟩🟩🌳",
           "🌳🌳🟩🟩🟩🌳🌳",
           "🌳🌳🌳🌳🌳🌳🌳"]]

def draw(n):
    os.system("cls")
    level = levels[n]
    screen = ""
    tile_y = 0
    for line in level:
        print_line = ""
        tile_x = 0
        for l in range(len(line)):
            if tile_y == player_coords[1] and tile_x == player_coords[0]:
                print_line += player_skin
            else:
                print_line += line[l]
            tile_x += 1
        tile_y += 1
        screen += print_line + "\n"
    print(screen)
        
def player_tick(move):
    global player_x, player_y, player_skin
    if move == "w":
        player_y -= 1
    if move == "a":
        player_x -= 1
    if move == "s":
        player_y += 1
    if move == "d":
        player_x += 1
    player_coords[0] = player_x
    player_coords[1] = player_y
        
def main():
    draw(0)
    player_tick(input())
    
while True:
    main()