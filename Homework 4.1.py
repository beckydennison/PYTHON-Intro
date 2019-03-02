

class Account(object):
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def setId(self, id):
        self.id = id
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self.id, self.balance, self.annualInterestRate)
        print(s)

    def getMonthlyInterestRate(self):
        return self.annualInterestRate /12

    def getMonthlyInterest(self):
        return (self.annualInterestRate * self.balance) /12 

myAccount = Account(1122, 20000, .045)

myAccount.withdraw(2500)

myAccount.deposit(3000)

print(myAccount.getId(), myAccount.getBalance(), myAccount.getMonthlyInterestRate(), myAccount.getMonthlyInterest())
