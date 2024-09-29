# Strings in Python

course = 'Python for Beginners'
       #  0123456789
course1 = "Python's course for Beginners"

course2 = 'Pythons\'s course for Intermediate' # Using the escape charatcer \'

course3 = "Python's course for \"Beginners\""
print(course)
print(course1)
print(course2)
print(course3)



email_messages = '''
Hi Vincent,

I hope this email finds you well?
I am writing to inform you about the updates in our recent products.

Thanks and have a nice day

Regards
John Doe


'''

print(email_messages)



# We can use square brackets to access the characters at a given index
print(course[0])

# We can use a negative index to get the last character
print(course[-1])

# String Slicing
message = "I am Happy"
print(message[0:]) # Prints From the start to the end of the string

name = "Jennifer"
print(name[1:-1])   # Output: ennife

