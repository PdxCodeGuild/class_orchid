#class created called atm
class ATM:
    #initialize each instance of the class 
    # while initializing each instance, you we are setting the atm's responsibilites
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate
    #function that checks balance and returns the balance
    def check_balance(self):
        return self.balance
    #function that handles deposits
    def deposit(self, amount):
        self.balance += amount
        
    #function that checks that compares the balance when there is a withdrawl amount and returns true if true
    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True 
    #function that sets the withdrawl responsibilities of the atm
    def withdraw(self, amount):
        self.balance -= amount
    #function that returns the calculated interest
    def calc_interest(self):
        return self.interest_rate * self.balance



atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')