from time import localtime

SALES_TAX = 6
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
dis_days = days[1], days[2]

print(dis_days)

def main():
    
    def getDiscout(total, discount):
        discount = (total * discount)/100
        return discount
    
    cos_input = ""
    cos_input = input("Type Costumer's Subtotal: $")
    if cos_input == "0":
        return False
    
    cos_subtotal = float(cos_input)
    
    def getDay():
        day = localtime().tm_wday
        return day
    
    day = getDay()
    weekday = days[day]
    date = localtime().tm_mday    

    cos_tax = getDiscout(cos_subtotal, SALES_TAX)

    cos_discount = 0
    if weekday in dis_days:
        dis_valid = 1
        if cos_subtotal >= 50:
            dis_valid = 2
            cos_discount = getDiscout(cos_subtotal, 10)
    else:
        dis_valid = 0

            
    cos_total = cos_subtotal - cos_discount + cos_tax
    
    def printRecepit():
        
        print(f"""
{weekday} {date}
-------------------------------
Receipt:
  Subtotal  =   {cos_subtotal}
  Discount  =   {cos_discount}
  Sales_Tax =   {cos_tax}
                ---------------
    Total:      {cos_total}
    """)
    
    printRecepit()
    if dis_valid == 1:
        print(f"""
Today is discount day, get 10% offsale with a subtotal of $50 or above.
You still have ${50-cos_subtotal} to go.
""")
        
    return True
        
        
while main() == True:
    main()