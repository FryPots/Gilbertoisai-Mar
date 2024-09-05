import random as rand
import math

def turn():
    global com
    print("""Choose your weapon:
1- Rock     🗿
2- Paper    📝
3- Scissors ✂️""")
    out = input("Option: ")
    return(out)

while True:
    atk = turn()
    if atk in range(0,4):
        print("""
valid
""")
    else:
        spaced(f"""PLAYER VICTORIES: {player}
COMPUTER VICTORIES: {computer}""")
        input("Press any key to exit")
        break