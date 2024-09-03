import time as t
from math import sqrt

def c():
    input("press enter to continue...")

def Number1():
    for greet in range(10):
        print("Hello!")
    
    c()
        
def Number2():
    for i in range(15):
        print("Hello! i is set to: " + str(i))

    c()
    
def Number3():
    f = open("million.txt", "w")
    
    start_t = t.time()
    
    for i in range(1,1000001):
        f.write(str(i)+"\n")
    end_t = t.time()
    f.close()
    
    f = open("million.txt", "r")
    p_start = t.time()
    print(f.read())
    p_end = t.time()
    print("File creation took " + str(end_t - start_t) + " seconds")
    print("Print took " + str(p_end - p_start) + " seconds")
    
    c()
    
def Number4():
    n = 0
    start_t = t.time()
    for i in range(1,1000001):
        n = i + n
    end_t = t.time()
    print("the sum of all previous numbers equals to " + str(n))
    print("Sum took " + str(end_t - start_t) +  " seconds")

    c()

    
def Number5():
    a = int(input("Insert the first integer: "))
    b = int(input("Insert the second integer: "))
    r = (b + 1)
    print(r)
    for num in range(a , r ):
        print(str(num) + " ^2 = " +  str(num**2))
    c()


def Number6():
    n = int(input("Insert an Integer: "))
    prime = False
    if(n <= 1):
        return False
        for index in range(2, int(sqrt(n)) + 1):
            if n % index == 0:
                return False
        return True
    print("Is " + str(n) + " prime?" + str(prime))
    c()

Number1()
Number2()
Number3()
Number4()
Number5()
Number6()