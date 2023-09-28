# Create a package called bank which simulates a simple banking system.
# Inside the package, create two modules: account and transaction.
# The account module defines a base class Account with common attributes
# like account_number, holder_name and balance.
# After this create two subclasses SavingsAccount and CheckingAccount with their own methods.
# The transaction module should provide functions for deposit and withdrawal.
import account as a
def deposit(account,amount):
    if amount<0:
        print("Amount should not be negative")
    else:
         account.balance += amount

def withdrawal(account,amount):

    if(amount>0 and account.balance>=amount):
        account.balance-=amount
    else:
        print("Invalid withdrawal amount or insufficient balance")

