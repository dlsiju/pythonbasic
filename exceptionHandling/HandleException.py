from exceptionHandling.LessThanOneError import LesThanZeroError


class HandleException:

    def process(self):
        try:
            number = int(input("Enter a number: "))
            number2 = int(input("Enter another number: "))
            result = number / number2;
            print('result=', result)
            isvalid = self.validateResult(result)
        except ValueError as e:
            print('Error while reading input', e)
        except ZeroDivisionError as e:
            print('Error while dividing numbers', e)
        except LesThanZeroError as e:
            print('The result should be greater than or equal to one', e)
        else:
            print('is it valid result?', isvalid)
        finally:
            print('completed the execution')

    def validateResult(self, result):
        if result < 1:
            raise LesThanZeroError("The result',result < 1")
        return True


handle = HandleException()
handle.process()
