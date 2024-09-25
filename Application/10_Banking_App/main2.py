def show_balance(balance):
    print("_____________________________________")
    print(f"       Current Balance: ${balance:,.2f}")
    print("|____________________________________|")
    print()

def deposit(balance):
    amount = float(input("How much do you want to deposit? "))
    if amount <= 0: 
        print("Invalid amount, amount should be greater than 0")
        return balance
    else:
        balance += amount
        print(f"${amount:,.2f} has been successfully added to your account.")
        print(" _____________________________________")
        print(f" |Current Balance: ${balance:,.2f}             |")
        print(" |____________________________________|")
        print()
        return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    
    # Check for insufficient balance
    if amount > balance:
        print("Insufficient balance. Withdrawal failed.")
        return balance
    elif amount <= 0:
        print("Invalid amount. Withdrawal failed.")
        return balance
    else:
        balance -= amount
        print(f"You have successfully withdrawn ${amount:,.2f}.")
        print(f"Current balance: ${balance:,.2f}")
        return balance

def transfer(balance):
    transfer_account_num = ""
    while True:
        transfer_account_num = input("Enter account number: ")
        if len(transfer_account_num) != 10:
            print("Invalid account number. Please enter a 10-digit account number.")
        else:
            bank_name = input("Enter Bank Name: ")
            amount = float(input("Enter the amount to transfer: "))
            
            if amount > balance:
                print("Insufficient balance for the transfer.")
                return balance
            elif amount <= 0:
                print("Invalid transfer amount. Transfer failed.")
                return balance
            else:
                balance -= amount
                print(f"Successfully transferred ${amount:,.2f} to account {transfer_account_num} at {bank_name}.")
                print(f"Current balance: ${balance:,.2f}")
                return balance

# Main loop
balance = 0
is_running = True

while is_running:
    print("====================================")
    print("Welcome to Opay Banking Application")
    print("Enter 1: Show Balance")
    print("Enter 2: Deposit")
    print("Enter 3: Withdraw")
    print("Enter 4: Transfer")
    print("Enter 5: Exit")
    choice = input("Please select an option (1-5): ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance = deposit(balance)
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        balance = transfer(balance)
    elif choice == "5":
        is_running = False
        print("Thank you for banking with us!")
    else:
        print("Invalid entry, please select a valid option.")
    print("====================================")
