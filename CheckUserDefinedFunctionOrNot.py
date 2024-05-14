import types


def commonFunction():
    print("It is common function")


class UserDefinedFunctionOrNot:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def displayDetails(self):
        print(self.name, self.place)


result = lambda x: True if x % 2 == 0 else False
userDefinedFunction = UserDefinedFunctionOrNot('John', 'Smith')
userDefinedFunction.displayDetails()
print('10 is even? ', result(11))
print('type(userDefinedFunction.displayDetails)=', type(userDefinedFunction.displayDetails))

# check type of displayDetails  using type() method
typ = type(userDefinedFunction.displayDetails)

if typ is types.FunctionType or types.MethodType:
    if typ is types.FunctionType:
        print('type of display details is function')
    elif typ is types.MethodType:
        print('type of display details is method')

# check type of commonFunction  using isinstance method
if isinstance(commonFunction, types.FunctionType):
    print('type of commonFunction is function')
else:
    print('type of commonFunction is method')

# check type of result using isinstance method
if isinstance(result, types.LambdaType):
    print('The result is lambda type')

if isinstance(len, types.BuiltinFunctionType):
    print('The len is built in function')
