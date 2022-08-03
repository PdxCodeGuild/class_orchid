class ATM:
    def __init__(self, balance=0, interest_rate=0.1, print_transactions=[]):
        self.balance = balance
        self.interest_rate = interest_rate
        self.print_transactions = print_transactions

    def check_balance(self):
        """return the account balance"""
        print(self.balance)
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        #deposit_amount = input("Enter the amount you want to deposit: ")
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        #withdrawal_amount = input("Please enter the withdrawal amount: ")
        if amount > self.balance:
            print("Insufficent Funds")
            return False
        if amount <= self.balance:
            print("account has sufficent funds")
            return True

        

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        #withdrawal_amount = input("Please enter the withdrawal amount: ")
        self.balance = self.balance - amount
        return amount 

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interst_gained = (self.interest_rate * self.balance) / 12 
        return interst_gained

print_transactions = []
atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
print(f"Please Enter one of the following commands when prompted; balance, deposit, withdraw, interest, help, transactions, or exit")
while True:
    #print_transactions = []
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
        bal_str = str(balance)
        bal_log = f"checked balance"
        print_transactions.append(bal_log)
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        str_dep = str(amount)
        dep_log = f"deposited" + " " + "$" + str_dep
        print_transactions.append(dep_log)
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            str_amount = str(amount)
            trans_log = f"withdrew" + " " + "$" + str_amount
            print_transactions.append(trans_log)
        else:
            print('Insufficient funds')
            print_transactions.append("Insufficient Funds")
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
        interest_str = str(amount)
        interest_log = f"account gained" + amount + "interest"
        print_transactions.append(amount)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transactions     - print transaction history')
    elif command == "transactions":
        tranactions = print_transactions
        print(tranactions)
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
