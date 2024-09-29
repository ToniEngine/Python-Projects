#type annotations
#If you declare age as an integer with a specific value like age: int = 42,
#it means you are explicitly setting the variable age to the integer value 42.
# Here's what this line of code does: : 
"""int: This part indicates the type annotation, 
specifying that age should be of type int, which means it should hold integer values."""
while True:
    age: int = 26
    print("Guess my age")
    guess: int =int(input("What is your guess? "))
    if guess == age:
        print("Your guess was correct!")
        break
    else:
        print("Sorry!, Worng Guess") 
        continue       


name: str = "Hello Richman"

