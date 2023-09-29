# # Create a package called bank which simulates a simple banking system.
# # Inside the package, create two modules: account and transaction.
# # The account module defines a base class Account with common attributes
# # like account_number, holder_name and balance.
# # After this create two subclasses SavingsAccount and CheckingAccount with their own methods.
# # The transaction module should provide functions for deposit and withdrawal.
import account as a
def deposit(amount):
    if amount<0:
        print("Amount should not be negative")
    else:
        a.self.balance += amount
        print(f"Your balance after deposit is {a.self.balance}")
def withdrawal(amount):

    if(amount>0 and a.balance>=amount):
        a.balance-=amount
        print(f"Your balance after withdrawal is {a.balance}")
    else:
        print("Invalid withdrawal amount or insufficient balance")
#
