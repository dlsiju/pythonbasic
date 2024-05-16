from multipledispatch import dispatch


class FindArea:

    @dispatch(int)
    def area(self, x):
        return x * x

    @dispatch(int, int)
    def area(self, length, width):
        return length * width

    @dispatch(float, float)
    def area(self, h, b):
        return (h * b) / 2;


findArea = FindArea()
squareSize = int(input('Enter the square size:'))
print('area of square=', findArea.area(squareSize))
rectangleLength = int(input('Enter the length of rectangle:'))
rectangleWidth = int(input('Enter the length of rectangle:'))
print('area of rectangle=', findArea.area(rectangleLength, rectangleWidth))
triangleHeight = float(input('Enter the height of triangle:'))
triangleBase = float(input('Enter the base of triangle:'))
print('area of triangle=', findArea.area(triangleHeight, triangleBase))
