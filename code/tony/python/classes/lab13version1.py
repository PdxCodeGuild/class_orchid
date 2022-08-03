from decimal import Decimal, DefaultContext
DefaultContext.rounding = 'ROUND_DOWN'
round_exp = Decimal('.00')

class ATM:
    def __init__(self, balance=0, interest_rate=.01):
        self.balance = Decimal(balance)
        self.interest_rate = Decimal(interest_rate)

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        amount = Decimal(amount).quantize(round_exp)
        self.balance += amount
        return amount

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        return self.balance >= amount

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= Decimal(amount).quantize(round_exp)
        return amount

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest = Decimal(self.interest_rate * self.balance).quantize(round_exp)
        return interest
