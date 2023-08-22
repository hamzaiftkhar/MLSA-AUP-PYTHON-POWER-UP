print("\n\t\tBANK ACCOUNT SYSTEM:\n")

class Bank_Account:
    def __init__(self,number,name):
        self.name="hamza"
        self.number=6547
        self.balance=0
        print("Hello!\n Welcome to the Deposit & Withdrawal Machine\n")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n\t\tACCOUNT DETAILS\n account number",self.number)
        print("\n account holder name=",self.name)
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account('minahil',6754)
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()