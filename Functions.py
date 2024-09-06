import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def victory():
    print('Gives you his treasure!')

def history():
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

def checkCave(chosenCave):
    history()

    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        victory()
    else:
        print('Gobbles you down in one bite!')
            
        print("There's a different ending to this story...")
        time.sleep(2)
        print("Would you like to see it? (yes or no)")
        ending = input()
        if ending == "yes":
            history()
            victory()
    
playAgain = 'yes'
while True:
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        print('Do you want to play again? (yes or no)')
        playAgain = input()
    if playAgain == "no":
        break
