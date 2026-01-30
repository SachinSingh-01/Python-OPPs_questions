# Create a class Calculator with a method add() that adds two numbers passed during object creation.
class Calculator():
    def __init__(self, n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
cal=Calculator(6,33)
result=cal.add()
print(result)
