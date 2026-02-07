# Program to find the number of bits needed to be swapped to make 2 numbers equal
def totalFlips(number1 , number2):

    flips = 0

    while number1 > 0 or number2 > 0 :
        t1 = number1 & 1
        t2 = number2 & 2

        if t1 != t2:
            flips = flips + 1
            #Right shift both numbers
            number1 = number1 >> 1
            number2 = number2 >> 1
        return flips
    
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print("\nNumber of flips needed: " , totalFlips(number1 , number2))