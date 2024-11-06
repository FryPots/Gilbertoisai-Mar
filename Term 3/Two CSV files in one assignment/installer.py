super = r'''
import csv, os, datetime




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_csv(filename) -> dict:
    
    ## Uses keys to store "list names"
    dicctionary: dict = {}
    
    with open(file=filename, mode="r", newline="") as file:
        
        csvfile = csv.reader(file)     
        headers = next(csvfile)
        
        for name in headers:
            dicctionary[name] = []
            
        for row in csvfile:
            tmp = []
            for i in row:
                key = headers[row.index(i)]
                tmp = dicctionary[key]
                tmp = tmp.append(i)
        file.close()
        
    return dicctionary   

def inventory_setup(file) -> dict:
                
    inventory   =       (load_csv(file))
    products: dict = {}

    item_id    =  inventory["Product #"]
    item_name  =  inventory["Name"]
    item_price =  inventory["Price"]

    for i in item_id:
        idx = item_id.index(i)
        products[i] = [item_name[idx], item_price[idx]]
    
    return products

def load_request(file) -> list:  
              
    request     =      (load_csv(file))

    item_ids    =  request["Product #"]
    quantities  =   request["Quantity"]
    
    return [item_ids, quantities]
    

def main():
    
        date = datetime.datetime.now()
        print(f"\nDate: {date}\n")
        
        products    =     inventory_setup(r"products.csv")
        request     =     load_request(r"request.csv")

        item_ids    =     request[0]
        quantities  =     request[1]
        
        subtotal = 0
        for i in item_ids:
            item_desc = products[i]
            name = item_desc[0]
            price = float(item_desc[1])
            out_price = "$" + str(price)
            quant = int(quantities[item_ids.index(i)])
            
            subtotal += price * quant
            
            out = (f"{name : <25}{out_price : ^20}{quant : <25}")
            print(out)
        subtotal = round(subtotal, 2)
        print("-" * len(out))
        print(f"{"Subtotal: " : <25}{subtotal : ^20}{"" : <25}")
        total = round(((subtotal * 6)/100), 2)
        print(f"{"IVA: " : <25}{total : ^20}{"" : <25}")
        total = round(total + subtotal ,2)
        print(f"{"Total: " : <25}{total : ^20}{"" : <25}")
        
        input("Type your Credit Card Number: ")
        input("Thank you for your purchase!")
        clear()
        main()

if __name__ == "__main__":
    main()'''
    
request = """Product #,Quantity
W112,2
D083,4
W231,1
C013,2
D083,3"""

products = """Product #,Name,Price
D150,1 gallon milk,2.85
D083,1 cup yogurt,0.75
D215,1 lb cheddar cheese,3.35
P019,iceberg lettuce,1.15
P020,green leaf lettuce,1.79
P021,butterhead lettuce,1.83
P025,8 oz arugula,2.19
P143,1 lb baby carrots,1.39
W231,32 oz granola,3.21
W112,wheat bread,2.55
C013,twix candy bar,0.85
H001,8 rolls toilet tissue,6.45
H014,facial tissue,2.49
H020,aluminum foil,2.39
H021,12 oz dish soap,3.19
H025,toilet cleaner,4.50
"""

def install(filename, str):
    f = open(file=filename, mode="w", newline="")
    f.write(str)
    f.close()
    
install("supermarket.py", super)
install("products.csv", products)
install("request.csv", request)