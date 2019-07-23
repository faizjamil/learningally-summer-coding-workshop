#!/usr/bin/python3


# Enter class signature here
class BankAccount:  
  def __init__(self):
    self.balance = 100

  def deposit(self):
    amount = float(input("Enter amount to deposit"))
    balance += amount
# Use this method to handle depositing into the account
# It should adjust the balance
    
    pass


  def withdraw(self):
    amount = float(input("Enter the amount to withdraw"))
    balance -= amount
# Use this method to handle a withdraw
# Be sure to make sure the amount that is being withdrawen does not exceed the available balance
# the balance should reflect the withdraw

    pass


def main():
  chk1 = BankAccount()
  
  choice = int(input("Enter 1 for deposit - or 2 for withdrawl"))
  if choice == 1:
    chk1.deposit()
  else:
    chk1.withdraw()


if __name__ == "__main__":
  main()