'''
Given an integer n, perform the following conditional actions:
If n is odd, print "Weird".
If n is even and in the inclusive range of 2 to 5, print "Not Weird".
If n is even and in the inclusive range of 6 to 20, print "Weird".
If n is even and greater than 20, print "Not Weird".
'''

while True:
    user_input = int(input("Enter a number ").strip())
    if user_input % 2 != 0:
        print("This is an Odd Number and it is Weird")
    elif user_input >= 2 and user_input <= 5:
        print("This is even within the range of (2-5) and is Not Weird")
    elif user_input >= 6 and user_input<=20:
        print("This is an even number and is within the range of (6-20) and it is Weird")
    elif user_input > 20:
        print("This is even and it is greater than 20 it is Not Weird")