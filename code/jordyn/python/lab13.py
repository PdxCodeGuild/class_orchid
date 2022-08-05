import sys

class ATM:
    def __init__(self, balance=0, interest_rate=0.001, name='admin'):
        self.balance = balance
        self.interest_rate = interest_rate
        self.name = name

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        """calculate and return interest gained on account"""
        accumulated_interest = self.balance * self.interest_rate
        self.balance += accumulated_interest
        return accumulated_interest
    
    def transactions(self, transacts, current_user, action, amount):
        '''Makes a list of actions taken, by who, and how much'''
        new_list = f'{current_user} {action} ${round(amount, 2)}.'
        transacts.append(new_list)

    def print_transactions(self, transacts):
        '''prints recorded user transactions line by line'''
        for trans in transacts:
            print(trans)

def main():
    command = input("\nPlease enter a command, type help for available commands.\n> ").lower()
    if command == 'balance':
        balance = admin.check_balance()  # call the check_balance() method
        print(f'Your balance is ${round(balance, 2)}')
        main()
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        admin.deposit(amount)  # call the deposit(amount) method
        admin.transactions(transacts, admin.name, 'deposited', amount)
        print(f'Deposited ${amount}')
        main()
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if admin.check_withdrawal(amount):
            admin.withdraw(amount)  # call the withdraw(amount) method
            admin.transactions(transacts, admin.name, 'withdrew', amount)
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
        main()
    elif command == 'interest':
        amount = admin.calc_interest()  # call the calc_interest() method
        print(f'Accumulated ${round(amount, 2)} in interest')
        main()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        main()
    elif command == 'exit':
        sys.exit()
    elif command == 'transactions':
        admin.print_transactions(transacts)
        ...
    else:
        print('Command not recognized')
        main()

transacts = []

admin = ATM()
print("Welcome to the ATM")
main()