class Account:
    def __init__(self, acc_no, acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def get_acc_no(self):
        return self.__acc_no
    
    def get_acc_pass(self):
        return self.__acc_pass
    
    def reset_pass(self, new_pass):
        self.__acc_pass = new_pass
        print("Password reset successful")

acc1 = Account("SBIN0001234", "siddhesh@123")
print(acc1.get_acc_no())   # ✅ SBIN0001234
print(acc1.get_acc_pass()) # ✅ siddhesh@123
acc1.reset_pass("siddhesh@456") # ✅ Password reset successful