import os
from time import localtime

SALES_TAX = 6
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]

cos_subtotal = int(input("Type Costumer's Subtotal: $"))

def getDay():
    time = localtime()
    weekday = time.tm_wday
    return weekday

day = getDay()

def getDiscout(total, discount):
    discount = (total * discount)/100
    return discount

if cos_subtotal >= 50:
    cos_subtotal -= getDiscout(cos_subtotal, 10)


cos_tax = getDiscout(cos_subtotal, 6)
cos_total = cos_subtotal + cos_tax

print(f"""
${cos_total} {days[day]}
""")