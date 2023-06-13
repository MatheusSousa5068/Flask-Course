class Account:
    def __init__(self, owner: str, balance: float) -> None:
        self.__owner = owner
        self.__balance = balance

    def deposit(self, value: float) -> str:
        self.__balance += value
        return f'Deposit done successfully'
        

    def withdraw(self, value: float) -> str:
        if value > self.__balance:
            return f'Error! You may not withdraw higher values than your balance\nYour current balance is ${self.__balance}'
        
        self.__balance -= value
        return f'Withdraw done successfully'

    @property
    def owner(self) -> str:
        return self.__owner
    
    @property
    def balance(self) -> str:
        return self.__balance
    

    def __str__(self) -> str:
        return f'Owner: {self.owner}, balance: {self.balance}'
    
if __name__ == "__main__":
    a1 = Account('Lucas', 1000)

    print(a1)

    print(a1.deposit(1000))
    print(a1.balance)
    print(a1.withdraw(500))
    print(a1.withdraw(1500))
    print(a1.owner)
