# Create a package called bank which simulates a simple banking system.
# Inside the package, create two modules: account and transaction.
# The account module defines a base class Account with common attributes
# like account_number, holder_name and balance.
# After this create two subclasses SavingsAccount and CheckingAccount with their own methods.
# The transaction module should provide functions for deposit and withdrawal.

import transaction as t

class account:

    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def tbalance(self):
        return self.balance



class SavingAccount(account):

    def __init__(self,number,name,balance,interestrate):
        super().__init__(number,name,balance)
        self.interestrate =interestrate


    def interest(self,months):

       self.balance =self.balance+ self.balance*0.75*months

savingaccount = SavingAccount(123,"Garisha", 500000,0.75)
t.deposit(savingaccount,10000)
t.withdrawal(savingaccount,1000)
print(f"Account balance:{savingaccount.tbalance()}")

# class CheckingAccount(account):
#     def __init__(self, number, name, balance):
#         super().__init__(number, name, balance)
# #         self.balance = balance

