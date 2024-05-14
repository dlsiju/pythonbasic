import decimal

floatValue=float(input("Enter a float: "))
DecimalValue=decimal.Decimal(floatValue)
print('The Decimal value is: ',floatValue)
print('decimal.Decimal(4.5)=',decimal.Decimal(4.5))

stringValue=input("Enter a number as string: ")
decimalFromString=decimal.Decimal(stringValue)
print('The Decimal value is: ',decimalFromString)

tup=(DecimalValue,decimalFromString)
print('The tuple is: ',tup)
tupleVlaues=decimal.DecimalTuple(125,890,2)
print('The tupleVlaues is: ',tupleVlaues)

decimalv=decimal.Decimal('12.55656')
print('The decimal value is: ',decimalv)
decimalROundedValue=decimalv.__round__();
print('The decimal value is: ',decimalROundedValue)
#Rund up to 3 decimal places
print('RoundedValue  upto 3 decimal is: ',decimalv.__round__(3))
roundedNum=round(decimalv,3)
print('The rnum is: ',roundedNum)
