"""
Lab 13: ATM
"""


"""
call the add_to_log()
"""


class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1
        self.log = []
        
    def add_to_log(self,type_of_transaction,amount):
        if type_of_transaction == 'deposit':
            self.log.append(type_of_transaction)
            self.log.append(amount)
        elif type_of_transaction == 'withdraw':
            self.log += type_of_transaction,amount
        
    def check_balance(self):
        return round(self.balance, 2)

    def deposit(self, amount):
        self.balance += amount
        return round(amount, 2)
        
    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        return amount
        
    def calc_interest(self):
        calc_interest = (self.balance * 0.1) / 100
        return round(calc_interest, 4)
    
    def print_transaction(self):
        temp = ''
        for index in range(len(self.log)):
            if index % 2 == 1:
                temp += str(self.log[index]) + '\n'
            else: 
                temp += str(self.log[index]) + ' '
                
        return f'You have {temp}\n'
        
            

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
        atm.add_to_log(type_of_transaction='deposit',amount = amount)
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            atm.add_to_log(type_of_transaction='withdraw',amount= amount)
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
        receipt = input('Would you like a receipt?: ').lower()
        if receipt == 'yes':
            
            print(atm.print_transaction())
        elif receipt == 'no':
            print('Goodbye')
        break
    else:
        print('Command not recognized')
