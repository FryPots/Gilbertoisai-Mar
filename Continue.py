import random as rand
import math

def turn():
    print("""Choose your weapon:
1- Rock 🗿
2- Paper 📝
3- Scissors ✂️""")
    out = input("Option: ")
    return(out)

while True:
    atk = turn()
    if atk in range(0,4):
        print("""
valid
""")
    else:
        print("""  
unvalid
              """)