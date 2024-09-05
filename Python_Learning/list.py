#List
my_list =["banana", "cherry", "apple"]
print(my_list)

#List allows for different datatypes such as interger, boolean, string and floats
#List also allows duplicate elements
list =[True, 2, 2.5, "Michael", "Michael", "John"]
print(list)

#We access elements in the list by indexing and indexing starts from 0
print(list[3]) #This prints Michael

print(list[-1]) #This prints the last item on the list

#We can iterate over our list using a for loop
for i in list:
    print(i)

# We can also check if an item is present in our list

if "banana" in list:
    print("Yes it exist")
else:
    print("Does not exist")
 #Use Methods for list
print(len(my_list)) #gives the length of the string

#appends a new item at the end of the list
my_list.append("lemon") 
print(my_list)

# To insert a new element in the list using the insert method
my_list.insert(1, "strawberry")
print(my_list)

# To remove items can be done with the pop method
my_list.pop() #This removes the last item on the list  
print(my_list)


# We can pop what we removed into a variable such as
item_removed = my_list.pop()
print(item_removed)


