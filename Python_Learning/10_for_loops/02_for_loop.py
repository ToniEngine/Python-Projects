# A for loop in python is used to iterate over an iterable like a list, dictionary, string, or range
"""The code repeatedly asks the user to input a number and then prints the squares of all non-negative 
integers up to that number. After each calculation, it prompts the user whether they want to continue. 
If the user responds "yes," the process repeats. If the user responds "no" or anything else, the program exits.
"""
while True:
    user_input = int(input("Enter a number "))

    for i in range(user_input + 1): # Loop through numbers from 0 to n+1
        square = i*i         #  # Calculate square of i
        print(f"The square of {i} is {square}")
    end = input("Do you want to calculate the squares for another range of numbers? (yes/no) ")
    if end.lower() == "yes":
        continue
    else:
        quit()



