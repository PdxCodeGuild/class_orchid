# this lab has both versions included

class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1
        self.log = []
        
    def __reciept__(self,type_of_transaction,amount):
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
#part 2 of lab
    def print_transaction(self):
        trans = ''
        for index in range(len(self.log)):
            if index % 2 == 1:
                trans += str(self.log[index]) + '\n'
            else: 
                trans += str(self.log[index]) + ' '
                
        return f'You have successfully \n{trans}'
        
            

atm = ATM()  # create an instance of our class
print('Hello and Welcome to the ATM! \n')
print(f"-balance\n-deposit\n-withdraw\n-interest\n-help\n-exit\n")
while True:
    command = input('Enter a command: ').lower()
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your current balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? \n: '))
        atm.deposit(amount)  # call the deposit(amount) method
        atm.__reciept__(type_of_transaction ='deposit',amount = amount)
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? \n: '))
            # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            atm.__reciept__(type_of_transaction ='withdraw',amount = amount)
            print(f'You have successfully withdrawn ${amount}')
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
        copy_of_transaction = input('Would you like a reciept for your transaction? (yes/no)\n: ').lower()
        if copy_of_transaction == 'yes':
            print(atm.print_transaction())
        elif copy_of_transaction == 'no':
            print('Thank you! Come again!')
        break
    else:
        print('Not a valid command.')