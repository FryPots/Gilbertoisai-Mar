reset = "\x1b[0m"

bg_red = "\x1b[41m"
bg_gray = "\x1b[47m"
bg_blue = "\x1b[44m"
bg_green = "\x1b[42m"

if __name__ == "__main__":
    prefix = "\x1b["
    for color in range(49):
        out = prefix + str(color) + "m" + " " + str(color)
        print(out)
input()