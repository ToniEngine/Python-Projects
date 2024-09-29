
price_house = 100000
good_credit = True
bad_credit = False


if good_credit:
    down_payment = price_house * 0.1
    print(f"You have a good credit and your down payment is ${down_payment}")
elif bad_credit:
    down_payment = price_house * 0.2
    print(f"You have a bad credit and your down payment is ${down_payment}")
else:
    print("You can not purchase this house")
 
