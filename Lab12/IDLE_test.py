class BankAccount:
    def __init__(self, default_value: float = 200.00):
        self.balance = default_value

    def __str__(self):
        return f'Default value equals: '

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.balance += 1
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance: float = 0.99):
        BankAccount.__init__(self)
        self.
        
