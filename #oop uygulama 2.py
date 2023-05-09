#oop uygulama 2
class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance (self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
Hesap= BankAccount("Beyza")

print(Hesap.getBalance())
Hesap.deposit(1000)
print(Hesap.getBalance())
Hesap.withdraw(500)
print(Hesap.getBalance())