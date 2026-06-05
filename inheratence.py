class bank_ac:
    def __init__(self,account_no,account_holder,bal):
        self.account_no=account_no
        self.account_holder=account_holder
        self.bal=bal
    def deposite(self,amount):
        self.bal+=amount
        print(f"deposite successfully ₹{amount}")
    def withdraw(self,amount):
        if amount >self.bal:
            print("invalid amount")
        self.bal-=amount
        print(f"withdraw successfully ₹{amount}")
    def balance(self):
        print(f"current balance ₹{self.bal}")
    def view_details(self):
        print(f"account number:{self.account_no}")
        print(f"account holder:{self.account_holder}")
        print(f"account number:{self.bal}")
class savings_ac(bank_ac):
    def __init__(self,account_no,account_holder,bal,interest):
        super().__init__(account_no,account_holder,bal)
        self.interest=interest
    def cal_interest(self):
        interest=self.bal*self.interest/100
        return interest
    def add_interest(self):
        interest=self.cal_interest()
        self.bal+=interest
        print(f"interest added ₹{interest}")
    
class current_account(bank_ac):
    def __init__(self,account_no,account_holder,bal,overdrift_limit):
        super().__init__(account_no,account_holder,bal)
        self.overdrift_limit=overdrift_limit
    def withdraw(self,amount):
        if amount <=self.bal+self.overdrift_limit:
            self.bal-=amount
            print(f"withdraw successfully ₹{amount}")
        else:
            print("over drifted limited accessed")

s=savings_ac("ac101","narsi",5000,5)
s.view_details()
s.deposite(2000)
s.withdraw(1500)
s.add_interest()
s.balance()

c=current_account("ac101","narsi",5000,1000)            
c.view_details()
c.deposite(1000)
c.withdraw(7000)
c.balance()    

