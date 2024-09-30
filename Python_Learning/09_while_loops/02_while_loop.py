# whiel loop = a statement that will execute it's block of code,
#              as long as its condition remains True


name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)