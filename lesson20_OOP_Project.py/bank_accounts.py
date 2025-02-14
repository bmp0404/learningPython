class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}\n")


    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.") 
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of {self.balance: .2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupated: {error}")

    def transfer(self, amount, account):
        try:
            print('\n************\n\nBeginning Transfer')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete")
        except BalanceException as error:
            print(f"\nTransfer Interrupted {error}")



class InterestRewardsAcct(BankAccount): ## inheritance
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interuptted: {error}")