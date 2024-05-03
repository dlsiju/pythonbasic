try:
    number = int(input("Enter the number for generating multiplication table: "))
    for index in range(1, 13):
        print(index, ' * ', number, '=', index * number)
except:
    print("Please enter a valid number")
