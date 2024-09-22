# Create a variable called my_list an assign it to an empty list
my_list = []

# Add the numbers 1 and 2 inside the list.
my_list =[1,2]

# You can add an item to the end of a list using the append() method.
example_list = [5,6,7,8]
print( example_list)   # Output: [5, 6, 7, 8]
example_list.append(9)
print(example_list)     # Output: [5, 6, 7, 8, 9]

# Try to use the append() method to add 3 to my_list. Then print the list.
my_list.append(3)
print(my_list)

# You can also access a single element to get its value.
# Lists are zero-indexed like strings are. 
# That means that the first element is at index 0, the second element is at index 1 and so on.
# Print the first element of my_list

print(my_list[0])

# Strings are Mutable

example_list[2] ="I am a changed Item"
print(example_list)   #: Output: [5, 6, 'I am a changed Item', 8, 9]


# Change the first element of my_list to 0, then print the list to check the value.
my_list[0] = 0
print(my_list)   # Output: [0, 2, 3]


# The insert method can add an element at any position in a list. 
# The first argument is the position at which the element has to be added, 
# The second argument is the element to add.

your_list = [1,2,4,5,6]
your_list.insert(2,3)
print(your_list)

# Using insert(), add 1 to my_list in the proper position so that it is counting upward, then print the list.
my_list.insert(1,1)
print(my_list)

# The pop() method can be used to remove an element from a list.
#  By default, it removes the last element of the list. 
fruits_list = ["cherry", "lemon", "tomato", "apple", "orange"]
fruits_list.pop()  #: removes the last item in the list ("orange")
print(fruits_list)


# You can pass an index as the argument to the method, and it will remove the element at the given index.
fruits_list.pop(0)
print(fruits_list)  # Output: ['lemon', 'tomato', 'apple'] removes the item at index [0] of the list.