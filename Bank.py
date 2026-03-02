
# Welcome to your PY Bank 
# To open new account in bank - create_account
# To get bank accounts detsils - get_bank_detailes()
# To diposit ammount - deposit()
# to withdraw ammount - withdraw()


class Bank:
    """Welcome to PY Bank"""

    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self):
        while True:
            name = input("Please enter your name: ")
            balance = int(input("Please enter initial amount you want to deposit: "))

            self.accounts[self.next_account_number] = [name, balance]
            print(f"Account created successfully. Your account number is {self.next_account_number}")

            self.next_account_number += 1

            another = input("Do you want to create another account? (Yes/No): ")
            if another.lower() != "yes":
                print("Thanks for banking with PY Bank.")
                break

    def get_bank_details(self):
        acc_no = int(input("Please enter your account number: "))

        if acc_no in self.accounts:
            name, balance = self.accounts[acc_no]
            print(f"Hello {name}, your account balance is {balance}")
        else:
            print("You do not have an account in PY Bank.")

    def deposit(self):
        acc_no = int(input("Please enter your account number: "))

        if acc_no in self.accounts:
            amount = int(input("Please enter amount to deposit: "))
            self.accounts[acc_no][1] += amount
            print(f"Deposit successful. Current balance: {self.accounts[acc_no][1]}")
        else:
            print("You do not have an account in PY Bank.")

    def withdraw(self):
        acc_no = int(input("Please enter your account number: "))
        
        if acc_no in self.accounts:
            amount = int(input("Please enter amount to withdraw: "))

            if self.accounts[acc_no][1] >= amount:
                self.accounts[acc_no][1] -= amount
                print(f"Withdrawal successful. Current balance: {self.accounts[acc_no][1]}")
            else:
                print("Insufficient balance.")
        else:
            print("You do not have an account in PY Bank.")


my_acct = Bank()
my_acct.create_account()
my_acct.get_bank_details()
my_acct.deposit()
my_acct.withdraw()
