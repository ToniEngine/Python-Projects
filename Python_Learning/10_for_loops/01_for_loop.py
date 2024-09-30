# We use a for loop to iterate over a category of item and do something with it

for item in "Python":
    print(item)
# print(item)

# Looping over a list of names
for item in ["Mosh", "John", "Sarah"]:
    print(item)

# Looping over a list of numbers
for item in [2,4,6,8]:
    print(item)

print("")
# Looping over a large list of numbers using the range() function
for item in range(10):
    print(item)


print("")
for item in range(1, 20+1):
    print(item)

print("")  # The range() function optionally takes a step
for item in range(1,20,2): # This Print all the odd numbers in the range of 1-20
    print(item)