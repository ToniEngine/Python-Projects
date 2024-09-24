# error handling using try and except

try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid Value")

# The above error is referred to as an exception
# We use try and except blocks to handle exceptions that are raised in our program
 