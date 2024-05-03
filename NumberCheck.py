try:
    numberTOCheck = float(input("Enter a number to check: "))
    if numberTOCheck > 0:
        print("The given number is positive")
    elif numberTOCheck < 0:
        print('The given number is negative')
    else:
        print("The given number is zero")
except:
    print("Please enter a valid number")
