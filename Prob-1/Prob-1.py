# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Ilya Panasevich

"""IPO
Input: number between 1 and 10
Process: converts the number to a roman numeral
Output: roman numeral between I and X
"""

# function definition

def translate(num):
    if num == 1:
        return "I"
    elif num == 2:
        return "II"
    elif num == 3:
        return "III"
    elif num == 4:
        return "IV"
    elif num == 5:
        return "V" 
    elif num == 6:
        return "VI"
    elif num == 7:
        return "VII"
    elif num == 8:
        return "VIII"
    elif num == 9:
        return "IX"
    elif num == 10:
        return "X"
    else:
        return "Out of range, please choose a number between 1 and 10"   

# unit test function
def unitTest():
    print("1 is equvalent to the roman numeral:", translate(1))
    print("2 is equvalent to the roman numeral:", translate(2))
    print("3 is equvalent to the roman numeral:", translate(3))
    print("4 is equvalent to the roman numeral:", translate(4))
    print("5 is equvalent to the roman numeral:", translate(5))
    print("6 is equvalent to the roman numeral:", translate(6))
    print("7 is equvalent to the roman numeral:", translate(7))
    print("8 is equvalent to the roman numeral:", translate(8))
    print("9 is equvalent to the roman numeral:", translate(9))
    print("10 is equvalent to the roman numeral:", translate(10))
    print("12 is equvalent to the roman numeral:", translate(12))
    print("-1 is equvalent to the roman numeral:", translate(-1))

def main():
    num = eval(input("Please enter a number between 1 and 10:"))
    print(num, "translates to the roman numeral", translate(num))

unitTest()
main()
