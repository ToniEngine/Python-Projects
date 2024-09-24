
def show_balance(balance):
    # balance = balance + amount
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount = float(input("How much do you want to deposit? "))
    if amount <= 0:
        print(f"Invalid amount entry")
        return 0
    else:
        print(f"${amount:.2f} has been successfully added to your account")
        return amount

def withdraw(balance):
    withdraw_amount = float(input("Enter amount to withdraw..... "))
    if withdraw_amount <= 0:
        print("Please enter a valid amount")
        return 0
    elif withdraw_amount > balance:
        print("Insufficient Funds")
        return 0
    else:
        print(f"You have withdrawn ${withdraw_amount} from your account")
        return withdraw_amount

def transfer():
    pass

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Welcome to MoniePoint Banking Application")
        print("==========================================")
        print("Enter 1: Show Balance")
        print("Enter 2: Deposit")
        print("Enter 3: Withdraw")
        print("Enter 4: Transfer")
        print("Enter 5: Exit")

        user_input = input("Please select an option above:(1-5) ")
        if user_input == "1":
            show_balance(balance)
        elif user_input =="2":
            balance += deposit()
        elif user_input  == "3":
            balance -= withdraw(balance)
        elif user_input == "4":
            transfer()
        elif user_input == "5":
            is_running = False
        else:
            print("Invalid Input")
    print("==========================================")
    print("Thank you for banking with us")
if __name__ =="__main__":
    main()