class bankac:
    def __init__(self,ac_no,pin,balance=0):
        self.__ac_no=ac_no
        self.__pin=pin
        self.__balance=balance
        self.__transaction_history=[]
    def deposit(self,amount):
        if amount <=0:
            print("invalid amount")
            return
        self.__balance+=amount
        self.__transaction_history.append(f"deposited₹{amount}")
        print(f"{amount}₹deposited successfully")
    def withdraw(self,amount,pin):
        if pin != self.__pin:
            print("invalid pin")
            return
        if amount < 0:
            print("invaid amoumt")
            return
        if amount > self.__balance:
            print("insufficient fund")
            return
        self.__balance-=amount
        self.__transaction_history.append(f"withdraw₹{amount}")
        print(f"{amount}₹withdraw successfully")
    def check_bal(self,pin):
        if pin != self.__pin:
            print("invalid pin")
            return
        print(self.__balance,"balance amount")
    def change_pin(self,old_pin,new_pin):
        if old_pin != self.__pin:
            print("invalid pin")
            return
        self.__pin=new_pin
        print("pin changed")
    def view_tr(self,pin):
        if pin != self.__pin:
            print("invalid pin")
            return
        print(" transaction history")
        print("------------------------")
        if not self.__transaction_history:
            print("no transaction found")
            return
        for trans in self.__transaction_history:
            print(trans)
        
a=bankac("ac101",2727,10000)
a.deposit(5000)
a.withdraw(5000,2727)
a.check_bal(2727)
a.change_pin(2727,7272)
a.deposit(1000)
a.view_tr(7272)
