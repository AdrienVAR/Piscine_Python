class Account(object):
    ID_COUNT = 1
    value = 0 #
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    def transfer(self, amount):
        self.value += amount

#kwargs? == #add value = 0 in class Account?
#hasattr?
#ID_COUNT before init = static in C?


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        self.account.append(account)
    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True is success, False is an error occured
        """
        if origin == Account and dest == Account and type(amount) is int or float and amount > 0:
            if origin.value > amount and (dest.value + amount) > 0 :
                origin.value -= amount
                dest.value += amount
                return True
        return Fasle
    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True is success, False is an error occured
        """

if __name__ == "__main__":
    client1 = Account("client1")
    client2 = Account("client2")
    client1.transfer(1000)
    client2.transfer(250)
    JPMorgan = Bank()
    JPMorgan.transfer(client1, client2, 200)
    print(client1.value)
    print(client2.value)