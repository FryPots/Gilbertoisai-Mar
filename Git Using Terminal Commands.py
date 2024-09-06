import random
# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
# Randomly select a word from the list
selected_word = random.choice(word_list)
# Initialize the user's guess
while True:
    print(f"Word list: {word_list}")
    user_guess = input("guess: ")
    if user_guess.casefold() == selected_word:
        print("you WIN")
        input("Press any key to exit: ")
        break
    else:
        print("Try again... :(")