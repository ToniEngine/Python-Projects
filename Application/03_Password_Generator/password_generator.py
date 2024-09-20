#Password Generator Project
'''This Program Generates a random password for the user'''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers =["0","1","2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Hello welcome to the MyPassword generator app")
user_name = input("What is your name? ").title()
print(f"Hello! {user_name}, Please follow the prompt below.......")
# print()
level = str(input(f"Hi!, {user_name} What Kind of password do you want? 'Easy' or 'Hard'\n")).lower()

def easy_password():
    no_of_letter =int(input("How many letters do you want in your password?\n"))
    no_of_symbol =int(input("How many symbols do you want in your password?\n"))
    no_of_numbers =int(input("How many numbers do you want in your password?\n"))
     #Easy Password
    password = ""
    for char in range(1, no_of_letter +1):
       #range actually gonna be from 1-4
       random_letter = random.choice(letters) #returns a randomly selected element from a non-empty sequence
       password += random_letter
       

    for char in range(1, no_of_symbol):
        random_symbol = random.choice(symbols)
        password += random_symbol
    
    for char in range(1, no_of_numbers):
        random_number = random.choice(numbers)
        password += random_number

    print(f"Your Password is: {password}" )

def hard_password():
    no_of_letter =int(input("How many letters do you want in your password?\n"))
    no_of_symbol =int(input("How many symbols do you want in your password?\n"))
    no_of_numbers =int(input("How many numbers do you want in your password?\n"))

    #Hard Password
    password_list = []
    for char in range(1, no_of_letter +1 ):
        password_list.append(random.choice(letters))
        
    for char in range(1, no_of_symbol +1 ):
        random_symbol = random.choice(symbols)
        password_list += random_symbol
    for char in range(1, no_of_numbers +1 ):
        random_number = random.choice(numbers)
        password_list += random_number

    new_password =random.shuffle(password_list)
    print(new_password)
        
def pws():
    ...
    
if level == "easy":
    easy_password()
elif level == "hard":
    hard_password()
else:
    print("You have to select a level")
    






