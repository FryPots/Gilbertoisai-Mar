import random

def game():
    global guess
    guess = False
    global value
    value = random.randint(1, 10)

def game_over():
    reset = ""
    reset = input("Try again? Y/N: ")
    if reset == "Y":
        game()
    elif reset == "y":
        game()
    else:
        global guess
        guess = True

game()

while guess == False:
    #print(value)
    num = input("Enter a Number between 1 - 10: ")
    valid = num.isdigit()
    if valid == True:
        inter = int(num)
        if inter > 10:
            print("Number " + num + " Is not a valid Number. Try Again")
        elif inter < value:
            print ("You guessed too low. Try Again")
        elif inter > value:
            print ("You guessed too high. Try Again")
        else:
            print("You WON!")
            game_over()
    else:
        print("Please enter a valid value")
        guess = True
        guess = False