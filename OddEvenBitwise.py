def isEvenOdd(num):
    if (num ^ 1 == num + 1):
        return True
    else:
        return False
    
number = int(input("Enter your number: "))

if isEvenOdd(number):
    print(number , "is even")
else:
    print(number , "is odd")