class ATM:
    def __init__(self, balance=0, interest_rate=0.1, transactions=[]):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount
        self.transactions.append(f'user deposited: ${amount}')

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount
        self.transactions.append(f'user withdrew: ${amount}')
        return amount

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest = self.balance * self.interest_rate
        return interest

    def print_transations(self):
        """print transaction history"""
        print('\nHisotry:')
        print('\n'.join(self.transactions))