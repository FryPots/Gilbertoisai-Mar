player_x = 4
player_y = 4
player = ["🟩",[player_x, player_y]]
player_coords = player[1]
player_skin = player[0]

levels = [["⬜⬜⬜⬜⬜⬜⬜",
           "⬜⬛⬛⬛⬛⬛⬜",
           "⬜⬛⬜⬛⬛⬛⬜",
           "⬜⬛⬛⬛⬜⬛⬜",
           "⬜⬜⬛⬛⬛⬛⬜",
           "⬜⬜⬛⬛⬛⬜⬜",
           "⬜⬜⬜⬜⬜⬜⬜"]]

level = levels[0]
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
    print(print_line)
        