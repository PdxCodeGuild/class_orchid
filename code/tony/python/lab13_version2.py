from classes.lab13version2 import ATM

atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
command = ''
while True:
    if command in ['', 'h', 'help']:
        print('Available commands:')
        print('b|balance  - get the current balance')
        print('d|deposit  - deposit money')
        print('w|withdraw - withdraw money')
        print('i|interest - accumulate interest')
        print('p|print - print transactions')
        print('q|quit     - quit the program')
    command = input('Enter a command: ')
    if command in ['b', 'balance']:
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command in ['d', 'deposit']:
        amount = float(input('How much would you like to deposit? '))
        amount = atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command in ['w', 'withdraw']:
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command in ['i', 'interest']:
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command in ['p', 'print']:
        for line in atm.print_transactions():
            print(line)
    elif command in ['q', 'quit']:
        break
    elif not command in ['', 'h']:
        print('Command not recognized')
