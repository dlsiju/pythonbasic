try:
    number = int(input("Enter the number for generating multiplication table: "))
    for index in range(1, 13):
        print(str(index), ' * ', str(number), '=', str(index * number))
except:
    print("Please enter a valid number")
