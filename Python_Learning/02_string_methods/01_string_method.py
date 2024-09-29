name = "Anthony Obot"
print(len(name))   # Prints the length of a string using the len method

 
print(name.find("A")) # Prints the postion of the string in the variable, 
# We were able to find the index of the first character of our name

surname = "obot"
print(surname.capitalize()) # This method capitalises  the first letter of our surname

middle_name = "edet"
print(middle_name.upper()) # This methods capitalises the entire middle name

nick_name = "TONIENINGE"
print(nick_name.lower()) # This makes our nickname to be in lowercase  


print(name.isdigit()) # Checks if the name variable is digit and returns a boolean value

age = "34"
print(age.isdigit())


alphabet= "abcdefghijkl"
print(alphabet.isalpha())  # Checks if it is an alphabetic character, note if there is a space the code would print false



print(nick_name.lower().count("e"))




# We can replace character within our string using the replace method and passing it two arguments
address = "nwaniba"
print(address.replace("b", "d"))  # Outputs: nwanida


prayer = "I am a chosen "
print(prayer *3)

course = 'Python for Beginners'
print(course.replace("Beginners", "Intermediate"))

# Using the in operator
print("Python" in course)

# The find method returns the index of that character but the in operator returns a boolean value

name = "fortune richman"
print(name.title())  # Outputs: Fortune Richman






