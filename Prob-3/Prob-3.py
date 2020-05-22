# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Ilya Panasevich

"""IPO
Input: square feet of wall space
Process: determines the costs from the amount of square feet of wall 
we desire to paint.
Output: number of gallons of paint required, hours of labor required, 
cost of the paint, the labor cost, and the total cost of the paint job.
"""
from math import *

# function definition
def paintReq(feet, paint):
    gallons = ceil(feet / 112)
    print("\nThe gallons of paint required to paint your walls:", gallons)
    # rounds up for hours (only outputs whole hours)
    laborHours = ceil(feet / (112 / 8)) 
    print("The hours of labor required:", laborHours)
    paintCost = gallons * paint
    print("The total cost of paint:", paintCost, sep=" $")
    laborCost = (laborHours * 35.00) + 99.00
    print("The total labor cost:", laborCost, sep=" $")
    totalCost = laborCost + paintCost
    print("The total cost of the paint job:", totalCost, sep=" $")

# main function definition
def main():
    feet = eval(input("Please enter the number of square feet of wall to paint:"))
    paint = eval(input("Please enter the cost of paint per gallon:"))
    paintReq(feet, paint)

main()
