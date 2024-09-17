class Account:
    def __init__(self,initial_Balance=0.0) :
        self.balnce=initial_Balance
    def deposit(self,amount)  :
        self.balnce+=amount
        return f'Deposit successful: Your new balance is ${self.balance:.2f}'
    def withdrowl(self,amount):
        if self.balance<amount:
            raise KeyError
        else:
            self.balnce-=amount
            return f'withdrow succesful:your current balance is ${self.balnce:.2f}'
       


