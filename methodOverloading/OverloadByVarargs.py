class OverLoadByVarargs:

    def findArea(self, *varargs):
        if len(varargs) == 1 and isinstance(varargs[0], int):
            return varargs[0] * varargs[0]
        if len(varargs) == 2 and isinstance(varargs[0], int):
            return varargs[0] * varargs[1]
        if len(varargs) == 2 and isinstance(varargs[0], float):
            return (varargs[0] * varargs[1]) / 2;


overload = OverLoadByVarargs()
squareSize = int(input('Enter the square size:'))
print('area of square=', overload.findArea(squareSize))
rectangleLength = int(input('Enter the length of rectangle:'))
rectangleWidth = int(input('Enter the length of rectangle:'))
print('area of rectangle=', overload.findArea(rectangleLength, rectangleWidth))
triangleHeight = float(input('Enter the height of triangle:'))
triangleBase = float(input('Enter the base of triangle:'))
print('area of triangle=', overload.findArea(triangleHeight, triangleBase))
