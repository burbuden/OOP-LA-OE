print ("OE#6\nArdent Azrael Sayson\nBSIT2B\n")

class BankAccount:
    def __init__(self, accountnum, balance):
        self.__accountnum=accountnum
        self.__balance=balance
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("INVALID" * 10)
        
    def withdraw(self,wamount):
        if wamount > 0 and wamount < self.__balance:
            self.__balance -= wamount
        else:
            print("CANNOT HAVE DEBT " *3)
            
    # def bal_inva_chk(self):
    #     if self.balance < withdraw:
    #         print("CANNOT HAVE DEBT")
    #     else:
    #         pass
                
    def display_info(self):
        print (f"Account Number: {self.__accountnum}\nCurrent Balance: {self.__balance}")
        
    def disp_bal(self):
        print (f"Current Balance: {self.__balance}")
        
    def get_account_num(self):
        return self.__accountnum
        
    def get_balance(self):
        return self.__balance
        
    def set_new_balance(self,newamount):
        if newamount > 0:
            self.__balance = newamount
        else:
            print("INVALID " * 10)
    def protected_bal_check(self, passw):
        if passw == "PASSWORD":
            print (self.__balance)
        else:
            print ("Please don't peek into someone's bank info.")
            
ardent = BankAccount("0509 2003 0998", 0)

ardent.display_info()
ardent.deposit(float(input("Please input value to deposit: ")))
ardent.display_info()
ardent.withdraw(float(input("Please input value to withdraw: ")))
ardent.display_info()

ardent.withdraw(float(input("Please input value to withdraw: ")))
ardent.display_info()

print (ardent.get_account_num())
print (ardent.get_balance())

ardent.set_new_balance(float(input("Please input new balance for this account: ")))
ardent.display_info()
#print (ardent.__accountnum)
#print (ardent.__balance)

ardent.protected_bal_check(input("Please input passkey: "))

