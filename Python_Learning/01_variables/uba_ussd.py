def bankapp():
    print("1:Buy Airtime")
    print("2:Buy Data")
    print("3:Transfer")
    print("4:Pay Bills")
    print("5: Check Balance")
    print("6: Click Credit")
    print("7: Enquiries")
    print("8: Account Opening")
    print("9: Next")
    user_input =input("Enter your choice(1-9) ")

    def buy_airtime():
        print("1: Airtime-Self")
        print("2: Airtime-Others")
        print("00: Back")
        print("0: Main")

        def airtime_self():
            pin = (input("Please Enter your pin "))
            if len(pin) != 4:
                print("Incorrect Pin")
            else:
                print("Access Granted")
        user_input = input("Select an option ")
        if user_input == "1":
            airtime_self()
        elif user_input == "2":
            pass
        elif user_input == "00":
            pass
        elif user_input == "0":
            pass
        else:
            print("Invalid Entry")


    def buy_data():
        pass
    def transfer():
        pass
    def pay_bills():
        pass
    def check_balance():
        pass
    def click_credit():
        pass
    def enquiries():
        pass    
    def account_opening():
        pass
    def next():
        pass

    if user_input == "1":
        buy_airtime()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    elif user_input == "6":
        pass
    elif user_input == "7":
        pass
    elif user_input == "8":
        pass
    elif user_input == "9":
        pass
    else:
        print("Invalid Entry")






user_input = input("Enter Banking Code ")

if user_input == "*919#":
    bankapp()
else:
    print("Enter Correct Banking Code (*919#)")