def setOrNot(number , n):
    mask = 1 << (n - 1)

    if number & mask:
        print("\nSET")
    else:
        print("\nNOT SET")

number = int(input("Enter number: "))
n = int(input("Enter Bit number: "))

setOrNot(number , n)