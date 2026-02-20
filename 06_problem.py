# Create a class BankAccount with methods deposit() and withdraw().
class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amt=int(input("Enter money to deposit:"))
        self.balance+=amt
        print("Total Balance=",self.balance)
    def withdraw(self):
        withdrawl=int(input("Enter money to withdrawl:"))
        self.balance-=withdrawl
        print("Total Balance=",self.balance)
atm=BankAccount()
atm.deposit()
atm.withdraw()