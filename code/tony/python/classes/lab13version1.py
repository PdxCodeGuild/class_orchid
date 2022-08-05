class ATM:
    def __init__(self, balance=.0, interest_rate=.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        """return the account balance"""
        return round(self.balance, 2)

    def deposit(self, amount):
        """deposit a given amount into account"""
        amount = round(amount, 2)
        self.balance += amount
        return amount

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        return self.balance >= amount

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        amount = round(amount, 2)
        self.balance -= amount
        return amount

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest = round(self.interest_rate * self.balance, 2)
        return interest
