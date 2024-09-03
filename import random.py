import random
# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
# Randomly select a word from the list
def start():
    global selected_word
    selected_word = random.choice(word_list)
# Initialize the user's guess
start()
print(selected_word)
user_guess = ""
while True:
    while user_guess != selected_word:
        user_guess = ""
        user_guess = input("Write your guess: ")

    print("YOU WIN!")        
    user_guess = input("Try again? ")
    if user_guess.casefold() == "yes" or user_guess.casefold() == "y":
        start()
    else:
        break