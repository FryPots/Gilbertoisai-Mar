import random as rand
import math

##Now i know why people use comments

## Resets the game variables

player = 0
computer = 0
atk = ""
com = 0
rounds = 0

## filter for input
def valid(msg):
    out = input(f"{msg}: ")
    if out.isdigit() == True:
        out = int(out)
        if out in range(1,4):
#            print ("valid")
            return (out)
        else: 
#            print ("unvalid")
            return(False)
    elif out == "quit":
        return("quit")
    else:
        return(False)
    
## Asks for the player input
def turn():
    global com
    print("""Choose your weapon:
1- Rock     🗿
2- Paper    📝
3- Scissors ✂️""")
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
    
##SANDJKNJKGNSRKJFNJES

## Increases the Score by 1

def victory(tag):
    global player
    global computer
    if tag == "player":
        spaced(f"PLAYER WON USING {icon(atk)} AGAINST {icon(com)}")
        player += 1
    if tag == "cpu":
        spaced(f"COM WON USING {icon(com)} AGAINST {icon(atk)}")
        computer += 1
    if tag == "draw":
        spaced(f"DRAW BOTH USED {icon(com)}")
        player   += 1
        computer += 1

## Icon converter
def icon(num):
    if num == 3:
        return("✂️")
    if num == 2:
        return("📝")
    if num == 1:
        return("🗿")

## Main Game Loop



def game():
    global com
    global atk
    global rounds
    rounds += 1
    spaced(f"ROUND -[{rounds:03}]- !!!")
    com = cpu()
    atk = turn()




game()
while True:
#    print(atk)
    

    if str(atk).casefold != "quit":
        
        if atk != False: 
             
            if atk != com:
                if abs(atk - com) == 1:
                    print(abs(atk - com))
                    if atk < com:
                        victory("cpu")
                    else:
                        victory("player")
                        
                elif abs(atk - com) == 2:
                    print(abs(atk - com))
                    if atk > com:
                        victory("cpu")
                    else:
                        victory("player")
                        
            else:
                victory("draw")
            game()
            
            continue
        atk = valid("\nuse a valid number (1 - 3)")
    else:
        spaced(f"""PLAYER VICTORIES: {player}
COMPUTER VICTORIES: {computer}""")
        input("Press any key to exit")
        break