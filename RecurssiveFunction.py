def findSumOfFirstTenDigits(count):
    if count == 0:
        return count;
    else:
        return count + findSumOfFirstTenDigits(count - 1)


totalSum = findSumOfFirstTenDigits(10)
print("total=", totalSum)
