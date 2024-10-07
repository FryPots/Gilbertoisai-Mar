import random

def get_determiner(quantity = 1):
  if quantity == 1:
     words = ["a", "one", "the"]
  else:
       words = ["some", "many", "the"]
  return random.choice(words)

def get_noun(quantity = 1):
    if quantity == 1:
        words = ["girl", "boy", "cat", "dog", "baloon"]
    else:
        words = ["girls", "boys", "cats", "dogs", "baloons"]
    return random.choice(words)     

def get_verb(tense = 0):
    words = [["ate", "walked", "wrote"],["eat", "walk", "write"],["will eat", "will walk", "will write"]]
    words = words[tense]
    
    return random.choice(words)

def Main():
    
    for i in range(0,6):
        sentence_quantity = random.randint(1, 2)
        sentence_time     = random.randint(0,2)

        sen_preposition = (get_determiner(sentence_quantity))
        sen_obj         = (get_noun(sentence_quantity))
        sen_tense       = (get_verb(sentence_time))
    
        print(f"{sen_preposition.capitalize()} {sen_obj} {sen_tense}")
    
    user = input("generate more?: ")
    if user != "yes":
        return False
    else:
        print()
        return True


run = True
while run == True:
    run = Main()
    