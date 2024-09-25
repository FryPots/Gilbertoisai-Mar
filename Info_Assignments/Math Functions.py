import math

def factorial(n):
    out = n
    for i in range(1,n):
        a = (n - i)
        #print(a)
        out = a * out
    if len(str(out)) <= 9:        
        print(out)
    else:
        print("{:e}".format(out))

def factorialof():
    num = input("enter a number: ")
    if num.casefold() != "quit":
        if num.isdigit() == True and num.isnumeric() == True:
            num = int(num)
            factorial(num)
        else:
            print("use a valid digit")
        return True
    else:
        return False

def div_remain(a, b):
    a = int(a)
    b = int(b)

    print(f"Remainder: {a - (b * math.floor(a/b))}")
    print()
    return True    

def main():
    op = input("""-MENU--------
factorial:  1
div_remain: 2

Operation: """)
    if op == "1":
        return factorialof()
    if op == "2":
        a = input("Divisor: ")
        b = input("Dividend: ")
        print()
        return div_remain(a, b)
    
    
    
while main() == True:
    main()

