class Account:
    balance = 10

    def __init__(self, name, balance):
        self.name = name

    def withDraw(self):
        withdrawelAmount = int(input("Enter withdraw amount:"))
        self.balance -= withdrawelAmount
        print('successfully withdraw amount:', withdrawelAmount)

    def getBalance(self):
        return self.balance

    def deposit(self):
        amount = input('Please enter amount to deposit')
        self.balance += int(amount)
