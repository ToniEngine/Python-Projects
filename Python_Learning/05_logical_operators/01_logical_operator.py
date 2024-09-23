# logical operators (and, or, not) = to check if two or more conditional statements are True

temp = int(input("What is the temperature outside?: "))

if temp >=0 and temp <=30:  # Both conditions has to be true
    print("The temperature is good today!")
    print("Go Outside")
elif temp <0 or temp > 30: # One of the conditions must be True and the entire statement is True
    print("The temperature is bad today!")
    print("Stay inside")


