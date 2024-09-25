#Problem Statement

#The size of a car tire in the United States is represented with three numbers like this: 205/60R15.
#The first number is the width of the tire in millimeters. The second number is the aspect ratio.
#The third number is the diameter in inches of the wheel that the tire fits.
#The volume of space inside a tire can be approximated with this formula:
from math import pi
from datetime import datetime

    
Michelin = ["Michelin",245,70,19.5,"$55,210.93"]
Vittos  = ["Starfire",245,65,17,"$4,399.00"]
Goodrich = ["Bfgoodrich",235,80,17,"$13,275.04"]
Blackhawk = ["Blackhawk",245,45,17,"$1,781.00"]

tires = [Michelin, Vittos, Goodrich, Blackhawk]
print(tires)

def main():
    time = datetime.now()
    f = open("volumes.txt","a")
    f.write("\n")
    W =    float(input("Enter the width of the tire in mm (ex 205): "))
    f.write(f"width of tire:            {W}\n")
    A =    float(input("Enter the aspect ratio of the tire (ex 60): "))
    f.write(f"aspect ratio of tire:     {A}\n")
    D =    float(input("Enter the diameter of the wheel in inches (ex 15): "))
    f.write(f"diameter of the wheel:    {D}\n")
    
    choice = [W,A,D]
    
    a = (W * A) + (2540 * D)
    W = W ** 2
    b = pi * W *A
    a *= b
    result =     a/1000000000
    result = round(result, 2)
    
    f.write(f"volume of the tire:       {result}\n")
    
    def checkDimentions():
        for brand in tires:
            matches = 0
            i = 0
            for index in brand[1:4]:
                if choice[i] == float(index):
                    matches += 1
                i += 1
                if matches == 3:
                    return brand
        return False
            
    tire_match = checkDimentions()
    
    def printmatch():
        print(f"""
Brand = {tire_match[0]}
Width = {tire_match[1]}
Ratio = {tire_match[2]}
Dimtr = {tire_match[3]}

Price = {tire_match[-1]}""")
    
    if tire_match != False:
        printmatch()
        number = input("Would you like to buy it? (yes or no): ")
        if number == "yes":
            number = input("Type your Phone number: ")
            f.write(f"Phone: {number}\n")
    f.write(f"{time}\n")
        
        
    print(f"The approximate volume is {result} liters")

while True:
    main()