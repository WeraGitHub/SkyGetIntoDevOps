from account import Account


# SavingAccount inherits from Account
class SavingAccount(Account):

    def __init__(self, opening_amount, interest_rate):
        super().__init__(opening_amount)
        self._interest_rate = interest_rate

    # data - getters and setters
    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, interest_rate):
        self._interest_rate = interest_rate

