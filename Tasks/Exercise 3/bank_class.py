class BankAccount:
    """The __init__ method accepts an argument for the account's balance. It is
    assigned to the __balance attribute"""

    def __init__(self, bal, owner):
        self.__balance = bal
        self.__owner = owner

    # deposit method
    def deposit(self, amount):
        self.__balance += amount

    # the withdrawal method
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    # the get_balance method returns the account balance
    def get_balance(self):
        return self.__balance

    # the get_owner method
    def get_owner(self):
        return self.__owner

    # The __str__ method returns a string
    # indicating  the object's state

    def __str__(self):
        return f"""Balance: {self.__balance}  Owner: {self.__owner}"""
