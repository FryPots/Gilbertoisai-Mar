#Problem Statement

#The size of a car tire in the United States is represented with three numbers like this: 205/60R15.
#The first number is the width of the tire in millimeters. The second number is the aspect ratio.
#The third number is the diameter in inches of the wheel that the tire fits.
#The volume of space inside a tire can be approximated with this formula:
pi = 3.1416
def main():
    W =    int(input("Enter the width of the tire in mm (ex 205):"))
    A =    int(input("Enter de aspect ratio of the tire (ex 60):"))
    D =    int(input("Enter the diameter of the wheel in inches (ex 15):"))
    
    a = (W * A) + (2540 * D)
    W = W ** 2
    b = pi * W *A
    
    a *= b
    
    result =     a/10000000000
    print(f"The approximate volume is {result} liters")

while True:
    main()