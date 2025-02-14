from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Krish =  BankAccount(2000, "Krish")

Dave.getBalance()
Krish.getBalance()

Krish.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Krish)
Dave.transfer(100,  Krish)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Krish)
Blaze.transfer(1000, Krish)