# We accept user input in python by using the input() function

# name = input("What is your name? ")
# print(f"Hello {name}")

# age = int(input("What is your age? "))
# # print("Your are "  + str(age) + " years old.")
# print(f"You are {age} years old")


# You cannot perform maths on a string.


user_name = input("What is your name? ")
user_age = int(input("How old are you? "))
user_height =float(input("What is your height in cm? "))
# user_age += 1
new_age = user_age + 1
print(f"Hello {user_name}, You would become {new_age} years old in a year time and your height is {user_height}cm")
# print("Hello " + user_name + ","+ " You would become " + str(new_age) + "years old in a year time and your height is " + str(user_height) +"cm")