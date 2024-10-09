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

def get_preposition():
    words = ["above","across","against","along","among","around","at","before","behind","below","beneath","beside","between","beyond","by","for","from","in","inside","into","near","of","off","on","out","over","through","to","toward","under","until","with","within","without"]
    return random.choice(words)

def create_sentence(sentence_quantity = 1, sentence_time = 0):

    sen_determiner      =         (get_determiner(sentence_quantity))
    sen_obj             =               (get_noun(sentence_quantity))
    sen_tense           =                   (get_verb(sentence_time))
            
    sen_preposition     =   (f"{get_preposition()} {get_determiner()} {get_noun()}")
        
    print(f"{sen_determiner.capitalize()} {sen_obj} {sen_tense} {sen_preposition}")

def Main():
    for i in range(0,3):
        create_sentence(1,i)
    for i in range(0,3):
        create_sentence(2,i)

        
        
    user = input("generate more?: ")
    
    if user != "yes":
        return False
    else:
        print()
        return True


run = True
while run == True:
    run = Main()
    
