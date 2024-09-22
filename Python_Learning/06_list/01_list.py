#List
my_list =["banana", "cherry", "apple"]
print(my_list)

#List allows for different datatypes such as interger, boolean, string and floats
#List also allows duplicate elements
list =[True, 2, 2.5, "Samuel", "Michael", "John", "Michael"]
print(type(list))  #<class "list">
print(list)

# We access elements in the list by indexing and indexing starts from 0
print(list[3]) #This prints Samuel

print(list[-1]) #This prints the last item on the list

# We can iterate over our list using a for loop
for i in list:
    print(i)

# We can also check if an item is present in our list

if "banana" in list:
    print("Yes it exist")
else:
    print("Does not exist")

 # Use Methods for list
print(len(my_list)) #gives the length of the string

#appends a new item at the end of the list
my_list.append("lemon") 
print(my_list)

# To insert a new element in the list using the insert method.
# This requires the index you want to insert and the value you are inserting
my_list.insert(1, "strawberry")
print(my_list)

# To remove items can be done with the pop method
my_list.pop() #This removes the last item on the list  
print(my_list)


# We can pop what we removed into a variable such as
item_removed = my_list.pop()
print(item_removed)



# Using the .extend() method
course = ["Maths", "English", "Geography"]
art_courses = ["Literature", "Fine Arts"]
print(art_courses)
course.extend(art_courses)

# print(course.append("Physics"))
print(course)



love_languages= ["gift", "touch", "services"]
sex_languages =["kiss", "romance"]
love_languages.insert(1, sex_languages)
print(love_languages)

bad_love_languages = ["silent Treatment", "anger", "blocking"]
change = ["money"]
bad_love_languages.extend(change)
print(bad_love_languages)

alpha = "abcdefghijklmnopqrstuvwxyz"
list_alpha = []
list_alpha.extend(alpha)
print(list_alpha)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# alphabet.append('hey', "hdb")
# alphabet.extend(["mee"])

guess: int = 34
print(guess)
print(type(guess))

guess = 32
print(guess)
print(type(guess))


my_man = "tony"
print(type(my_man))



