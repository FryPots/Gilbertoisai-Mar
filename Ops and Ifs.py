guess = False

while guess == False:
    num = input("Enter a Number between 1 - 10: ")
    inter = int(num)
    if inter > 10:
        print("Warning! Number " + num + " Is not a valid Number. Try Again")
    elif inter < 3:
        print ("You guessed too low. Try Again")
    elif inter > 3:
        print ("You guessed too high. Try Again")
    else:
        print("You WON!")
        break
    