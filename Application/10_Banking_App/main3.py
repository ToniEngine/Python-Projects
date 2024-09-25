class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def show_balance(self):
        print("_____________________________________")
        print(f"       Current Balance: ${self.balance:,.2f}")
        print("|____________________________________|")
        print()

    def deposit(self):
        amount = float(input("How much do you want to deposit? "))
        if amount <= 0:
            print("Invalid amount, amount should be greater than 0")
        else:
            self.balance += amount
            print(f"${amount:,.2f} has been successfully added to your account.")
            self.show_balance()

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        elif amount <= 0:
            print("Invalid amount. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount:,.2f}.")
            self.show_balance()

    def transfer(self):
        transfer_account_num = input("Enter account number: ")
        if len(transfer_account_num) != 10:
            print("Invalid account number. Please enter a 10-digit account number.")
        else:
            bank_name = input("Enter Bank Name: ")
            amount = float(input("Enter the amount to transfer: "))

            if amount > self.balance:
                print("Insufficient balance for the transfer.")
            elif amount <= 0:
                print("Invalid transfer amount. Transfer failed.")
            else:
                self.balance -= amount
                print(f"Successfully transferred ${amount:,.2f} to account {transfer_account_num} at {bank_name}.")
                self.show_balance()


class BankingApp:
    def __init__(self):
        self.account = BankAccount()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.show_menu()
            choice = input("Please select an option (1-5): ")
            self.handle_choice(choice)

    def show_menu(self):
        print("====================================")
        print("Welcome to Opay Banking Application")
        print("Enter 1: Show Balance")
        print("Enter 2: Deposit")
        print("Enter 3: Withdraw")
        print("Enter 4: Transfer")
        print("Enter 5: Exit")
        print("====================================")

    def handle_choice(self, choice):
        if choice == "1":
            self.account.show_balance()
        elif choice == "2":
            self.account.deposit()
        elif choice == "3":
            self.account.withdraw()
        elif choice == "4":
            self.account.transfer()
        elif choice == "5":
            self.is_running = False
            print("Thank you for banking with us!")
        else:
            print("Invalid entry, please select a valid option.")


# Main program
app = BankingApp()
app.run()
