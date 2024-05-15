from inheritance.Account import Account


class SavingsAccount(Account):

    def __init__(self, name):
        self.name = name
        self.interestRate = 6.5

    def interestAmount(self):
        print('Interest for ', self.name, ' is ', self.interestRate, '%')


customerList = []
selectedAccount = None
slNo = -1


def displayAllSavingsAccounts():
    if len(customerList) == 0:
        print('There are no customers')
    for i in range(0, len(customerList)):
        print(i, '.', customerList[i].name)


while True:
    print("Welcome to Savings Account,Select an option")
    print(
        '1.create account\n2.select account\n3.deposit\n4.getBalance\n5.getInterest.\n6.withdraw\n7.close currnet account transaction\n8.list all accounts\n9.exit')
    option = input('Enter your option: ')
    if option == '1':
        if selectedAccount is not None:
            print('Account with name ', selectedAccount.name, ' already in processing, please complete it by enter 6', )
        else:
            customerName = input('Enter the customer name: ')
            savingsAccount = SavingsAccount(customerName)
            customerList.append(savingsAccount)
            print('Account created successfully')
    elif option == '2':
        displayAllSavingsAccounts()
        slNo = int(input('Enter customer serial number from list'))
        try:
            selectedAccount = customerList[slNo]
        except IndexError:
            print('Invalid customer number')
    elif option == '3':
        if selectedAccount is None:
            print('No account selected!')
        else:
            selectedAccount.deposit()
            print('Successfully deposited')
    elif option == '4':
        if selectedAccount is None:
            print('No account selected!')
        else:
            print('The balance for ', selectedAccount.name, ' is ', selectedAccount.getBalance())
    elif option == '5':
        if selectedAccount is None:
            print('No account selected!')
        else:
            selectedAccount.interestAmount()
    elif option == '6':
        if selectedAccount is None:
            print('No account selected!')
        else:
            selectedAccount.withDraw()
    elif option == '7':
        sl = -1
        selectedAccount = None
    elif option == '8':
        displayAllSavingsAccounts()
    elif option == '9':
        break
