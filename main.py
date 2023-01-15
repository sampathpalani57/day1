class Account():     # todo this is fucntion
    type_of_account = 'saving'
    def __init__(self, acc_name, acc_no):
        self. acc_name = acc_name
        self. acc_no = acc_no
        self.acc_balance = 0

    def display(self):
        print("the account name:", self.acc_name)
        print("the account number:", self.acc_no)
        print("the account balance:", self.acc_balance)

    def credit(self, deposit):
        self.acc_balance = self.acc_balance + deposit
        print("the account balance is:", self.acc_balance)

    def debit(self, withdrow):
        self.acc_balance = self.acc_balance - withdrow
        print("the with draw details is:", self.acc_balance)

obj = Account('sampath', 1000)
obj.display()
obj.credit(5)


