def power(x, n):
    out = x ** n
    return out

def square_area():
    base = float(input("input the lenght of the square's base (in cm): "))

    result = power(base, 2)
    return result
    
def triangle_area():
    base = float(input("input the lenght of the triangle's base (in cm): "))
    height = float(input("input the lenght of the triangle's height (in cm): "))
    
    result = (base * height / 2)
    return result
    
def main():
    print("""
Enter which figure's area you want to calculate...

type 1 for Square's     area
type 2 for Triangle's   area
""")
    op = ""
    op = input()
    if op.casefold() != "quit":
        if op == "1" or op == "sqr":
            print(f"{square_area()} cm²")
        if op == "2" or op == "tri":
            print(f"{triangle_area()} cm²")
        return True
    else:
        return False
    

while main() == True:
    main()