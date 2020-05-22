# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Ilya Panasevich

"""IPO
Inputs: total cost of transaction, amount tendered
Process: takes the amount tendered and the total transaction cost to 
return the amount of change in appropriate denominations. 
Outputs: summary line containing the total cost, amount tendered, and change
along with denominations of change.
"""

from math import *

# function definition
def cents(tendered, cost):
    change = round(tendered - cost, 2)
    changeDue = int(round(change * 100))
    print("cost:", cost, sep=" $")
    print("tendered:", tendered, sep=" $") 
    print("change due:", change, sep=" $")
    
    tens = changeDue // 1000
    changeDue = changeDue - (tens * 1000)
    if tens >= 1:
        print("tens:", tens)
        print("change due:", changeDue / 100, sep=" $")
    
    fives = changeDue // 500
    changeDue = changeDue - (fives * 500)
    if fives >= 1:
        print("fives:", fives)
        print("change due:", changeDue / 100, sep=" $")
    
    ones = changeDue // 100
    changeDue = changeDue - (ones * 100)
    if ones >= 1:
        print("ones:", ones)
        print("change due:", changeDue / 100, sep=" $")
    
    quarters = changeDue // 25
    changeDue = changeDue - (quarters * 25)
    if quarters >= 1:
        print("quarters:", quarters)
        print("change due:", changeDue / 100, sep=" $")
    
    dimes = changeDue // 10
    changeDue = changeDue - (dimes * 10)
    if dimes >= 1:
        print("dimes:", dimes)
        print("change due:", changeDue / 100, sep=" $")
    
    nickels = changeDue // 5
    changeDue = changeDue - (nickels * 5)
    if nickels >= 1:
        print("nickels:", nickels)
        print("change due:", changeDue / 100, sep=" $")
    
    pennies = changeDue // 1
    if pennies >= 1:
        print("pennies:", pennies)
    changeDue = changeDue - (pennies * 1)    
    print("change due:", changeDue / 100, sep=" $")
    

# main function definition
def main():
    cost = eval(input("Please enter the amount that you needed to pay:"))
    tendered = eval(input("Please enter the amount that you paid:"))
    cents(tendered, cost)

main()
