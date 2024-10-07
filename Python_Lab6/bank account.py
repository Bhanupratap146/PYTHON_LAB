class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}.")

# Example usage:
account = BankAccount("Ram", 100)  # Creating a bank account with an initial balance of $100

# Checking balance
account.check_balance()

# Depositing money
account.deposit(50)

# Withdrawing money
account.withdraw(30)

# Attempting to withdraw more than the balance
account.withdraw(150)

# Checking balance again
account.check_balance()
