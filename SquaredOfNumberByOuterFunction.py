def squaredOfNumbers(numb1, num2):
    def squareOfSecondNumber(num2):
        return num2 * num2

    return squareOfSecondNumber(num2) + (numb1 * numb1)


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sumOfSquares = squaredOfNumbers(number1, number2)
print("sum of squares", sumOfSquares)
