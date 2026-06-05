class BankAccount:

    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        self.__transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0")
            return

        self.__balance += amount
        self.__transaction_history.append(f"Deposited ₹{amount}")

        print(f"₹{amount} deposited successfully")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Invalid PIN")
            return

        if amount <= 0:
            print("Withdrawal amount must be greater than 0")
            return

        if amount > self.__balance:
            print("Insufficient Balance")
            return

        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawn ₹{amount}")

        print(f"₹{amount} withdrawn successfully")

    def check_balance(self, pin):
        if pin != self.__pin:
            print("Invalid PIN")
            return

        print(f"Current Balance: ₹{self.__balance}")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("Incorrect Old PIN")
            return

        self.__pin = new_pin
        print("PIN changed successfully")

    def view_transactions(self, pin):
        if pin != self.__pin:
            print("Invalid PIN")
            return

        print("\nTransaction History")
        print("-------------------")

        if not self.__transaction_history:
            print("No transactions found")
        else:
            for transaction in self.__transaction_history:
                print(transaction)

account = BankAccount("ACC101", 1234, 10000)

account.deposit(5000)

account.withdraw(2000, 1234)

account.check_balance(1234)

account.change_pin(1234, 5678)

account.check_balance(5678)

account.deposit(1000)

account.view_transactions(5678)
