def performArithmaticOperation(num1, num2):
    total = num1 + num2
    diff = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return total, diff, product, quotient


print('Enter two numbers:')
num1 = int(input())
num2 = int(input())
tuple = performArithmaticOperation(num1, num2);
print('all result is=', tuple)
print('Total of', num1, ' & ', num2, ' =', tuple[0])
print('Difference of', num1, ' & ', num2, ' =', tuple[1])
print('Product of', num1, ' & ', num2, ' =', tuple[2])
print('quotient of', num1, ' by ', num2, ' =', tuple[3])
