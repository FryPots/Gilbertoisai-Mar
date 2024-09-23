import random as rand
import math

import time

##Now i know why people use comments

## Resets the game variables

player = 0
computer = 0
atk = ""
com = 0
rounds = 0


def inRange(n, m, M):
    if (m <= int(n) < M):
        return True
    else:
        return False

## filter for input
def valid(msg):
    out = input(f"{msg}: ")
    if out.isnumeric() == False:
        #print("no numeric")
        if out.casefold() == "quit":
            return (out.casefold())
        else:
            return (False)
    else:
        #print("numeric")
        if inRange(out, 1, 4) == True:
            return(int(out))
        else:
            return(False)

def star(message):
    a = "*" * 10
    b = "*" * 5
    return(f"{a}{message} {b}")
## Asks for the player input
def turn():
    global com
    print(color(star("""
Choose your weapon:
1- Rock     🗿
2- Paper    📝
3- Scissors ✂️
"""), ""))
#    print (com)
    return valid("\nOption")

## COM turns
def cpu():
    out = rand.randint(1,3)
    return(out)

## Vertically Centered Text
def spaced(text):
    print(f"""
{text}          
          """)

## Main Game Loop
def game():
    global com
    global atk
    global rounds
    rounds += 1
    spaced(f"ROUND -[{rounds:03}]- !!!")
    com = cpu()
    atk = turn()
## Increases the Score by 1

def color(text, color):
    if color == "red":
        out = u"\u001b[31m"
    if color == "green":
        out = u"\u001b[32m"
    if color == "yellow":
        out = u"\u001b[33m"
    if color == "":
        out = u"\u001b[0m"
    return out + text + u"\u001b[0m"

def victory(tag):
    global player
    global computer
    if tag == "player":
        spaced(color(star(f"PLAYER WON USING {icon(atk)} AGAINST {icon(com)}"), "green"))
        player += 1
    if tag == "cpu":
        spaced(color(star(f"COM WON USING {icon(com)} AGAINST {icon(atk)}"), "red"))
        computer += 1
    if tag == "draw":
        spaced(color(star(f"DRAW BOTH USED {icon(com)}"), "yellow"))
        player   += 1
        computer += 1
    time.sleep(0.75)
    game()

## Icon converter
def icon(num):
    if num == 3:
        return("✂️ ")
    if num == 2:
        return("📝")
    if num == 1:
        return("🗿")
    
    
    

game()
while True:
    #print(atk)


    if str(atk) != "quit":

        if atk != False:

            if atk != com:
                if abs(atk - com) == 1:
                    #print(abs(atk - com))
                    if atk < com:
                        victory("cpu")
                    else:
                        victory("player")

                elif abs(atk - com) == 2:
                    #print(abs(atk - com))
                    if atk > com:
                        victory("cpu")
                    else:
                        victory("player")

            else:
                victory("draw")

            continue
        atk = valid("\nuse a valid number (1 - 3)")
    else:
        spaced(f"""PLAYER VICTORIES: {player}
COMPUTER VICTORIES: {computer}""")
        input("Press any key to exit")
        break