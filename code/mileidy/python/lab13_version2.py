
class ATM:
    def __init__(self):
        self.balance = 0
        #starting balance
        self.interest_rate = 0.1
        #starting interest rate
        self.log = []
        #where everything is stored
        
    def __reciept__(self,type_of_transaction,amount):
        if type_of_transaction == 'deposit':
            self.log.append(type_of_transaction)
            self.log.append(amount)
        elif type_of_transaction == 'withdraw':
            self.log += type_of_transaction, amount
        elif type_of_transaction == 'interest':
            self.log.append(type_of_transaction)
            self.log.append(amount)
        else:
            print('this code block doesnt work')

    def check_balance(self):
        #where i return account balance
        return round(self.balance, 2)

    def deposit(self, amount):
        #i added amount user inputs to the balance and returned the amount
        self.balance += amount
        return amount
        
    def check_withdrawal(self, amount):
        if self.balance >= amount:
        #i did if amount is less then or equal to balance allow withdrawl
            return True
        else:
            return False

    def withdraw(self, amount):
        #where i minus amount from balance
        self.balance -= amount
        return amount
        
    def calc_interest(self):
        #this is where i multiplied balanc by 0.1 then divided it by 100
        calc_interest = (self.balance * 0.1) / 100
        return calc_interest

    def print_transaction(self):
        trans = ''
        for index in range(len(self.log)):
            if index % 2 == 1:
                trans += str(self.log[index]) + '\n'
            else: 
                trans += str(self.log[index]) + ' '
                
        return f'You have successfully \n{trans}'

atm = ATM()  
print('Hello and Welcome to the ATM! \n')
print(f"-balance\n-deposit\n-withdraw\n-interest\n-help\n-exit\n")

while True:
    command = input('Enter a command: ').lower()
    # i .lowered the input so that the strings would match
    if command == 'balance':
        balance = atm.check_balance() 
        print(f'Your current balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? \n: '))
        atm.deposit(amount)
        atm.__reciept__(type_of_transaction ='deposit',amount = amount)
        print(f'You have Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? \n: '))
        if atm.check_withdrawal(amount):
            atm.withdraw(amount) 
            atm.__reciept__(type_of_transaction ='withdraw',amount = amount)
            print(f'You have successfully withdrawn ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() 
        atm.deposit(amount)
        atm.__reciept__(type_of_transaction ='interest',amount = amount)
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
            print('Goodbye!')
        break
    else:
        print('command not recognized.')