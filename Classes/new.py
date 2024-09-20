user_name = "Joe"
user_input = ""

# Ask for the name until it matches 'Joe'
while user_input != user_name:
    user_input = input("Enter your name: ")
    if user_input != user_name:
        print("Incorrect name, try again.")

# Ask for the password until it matches 'Vinscent01'
password = "Vinscent01"
user_password_input = ""
while user_password_input != password:
    user_password_input = input("Enter your password: ")
    if user_password_input != password:
        print("Incorrect password, try again.")

print("Access Granted")
