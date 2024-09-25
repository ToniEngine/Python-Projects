def show_balance(balance):
    print("_____________________________________")
    print(f"       Curent Balance: ${balance:,.2f}")
    print("|____________________________________|")
    # print(f"Your balance is ${balance:.2f}")
    # return balance

def deposit(balance):
    amount = float(input("How much do you want to deposit? "))
    if amount <=0:
        print("Invalid amount, amount should be greater than 0")
        return balance
    elif amount > 0:
        balance = balance + amount
        # print(balance)
        print(f"${amount:,.2f} has been successfully added to your account.")
        print(" _____________________________________")
        print(f" |Current Balance: ${balance:,.2f}             |")
        print(" |____________________________________|")
        print()
        return balance
    else:
        print("Invalid Entry")
        
        

def withdraw(balance):
    amount = float(input("Enter amount to withdraw..... "))
    balance = balance - amount
    print(f"You have successfully withdrawn ${amount:,.2f} and current balance is ${balance:,.2f}")
    return balance

def transfer(balance):
    transfer_account_num =""
    withdrawal = True
    while withdrawal:
        transfer_account_num = (input("Enter account number "))
        if len(transfer_account_num) != 10:
            print("Invalid account number")
        elif len(transfer_account_num) == 10:
            bank_name = input("Enter Bank Name>> ")
            withdraw(balance)# Error 1
            return withdraw(balance) # Error 2
        quit() # Error 3




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
    # print("======================================")
    choice = input("Please select an option above:(1-5) ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance = deposit(balance)
        
    elif choice == "3":
        balance = withdraw(balance)
    
    elif choice == "4":
        # print("Use Withdrawal option, Transfer option currently on maintenance")
        balance = transfer(balance)

    elif choice== "5":
        is_running = False
    else:
        print("Invalid Entry")
print("==========================================")
print("Thank you for banking with us")

        