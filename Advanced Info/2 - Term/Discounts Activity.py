from time import localtime

SALES_TAX = 6
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]

def main():
    

    
    def getDiscout(total, discount):
        discount = (total * discount)/100
        return discount
    
    cos_subtotal = float(input("Type Costumer's Subtotal: $"))
    
    def getDay():
        time = localtime()
        weekday = time.tm_wday
        return weekday
    
    day = getDay()
    weekday = days[day]
    date = localtime().tm_mday    

    cos_tax = getDiscout(cos_subtotal, SALES_TAX)
    
    if weekday in days[1:3]:
        if cos_subtotal >= 50:
            cos_discount = getDiscout(cos_subtotal, 10)
    else:
        cos_discount = 0
            
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
        
        
while True:
    main()