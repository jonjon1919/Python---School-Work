"""
OOP Bank Account
"""
import datetime as dt

class Account():
    """ Account Class"""

    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []


    def get_balance(self):
        """Return the balance of the account"""
        return self.balance


    def deposit(self, amount):
        """The deposit funtion of the account"""
        self.balance = self.balance + amount
        amount = abs(amount)
        self.transactions.append(+amount)
        return amount


    def withdraw(self, amount):
        """The withdraw function of the account"""
        self.balance = self.balance - amount
        self.transactions.append(-amount)
        return amount


class Transaction():
    """ Transaction Class"""

    def __init__(self, amount, timestamp=None):
        self.amount = amount
        self.timestamp = timestamp
        if timestamp is None:
            self.timestamp = dt.date.today()


    def __str__(self):
        return '{self.timestamp}: ${self.amount}'.format(self=self)



def main():
    """Main program"""
    bob_account = Account()
    bob_account.deposit(100)
    bob_account.withdraw(90)
    bob_account.deposit(10)
    print(bob_account.transactions)
    print(bob_account.get_balance())
    print(Transaction(100.56, dt.date(2019, 10, 31)))
    print(Transaction(-150))

main()
