class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Debited:", amount)
    
    def credit(self, amount):
        self.balance += amount
        print("Credited:", amount)
    
    def get_balance(self):
        return self.balance
    

acc1 = Account(5000, "SBIN0001234")
c1 = int(input("Enter the amount to be credited: "))
acc1.credit(c1)
d1 = int(input("Enter the amount to be debited: "))
acc1.debit(d1)
print("The balance in the account is:", acc1.get_balance())
