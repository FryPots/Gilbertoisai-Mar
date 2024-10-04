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

def get_verb(quantity = 1):
    