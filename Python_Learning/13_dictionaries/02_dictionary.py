'''A dictionary is another built-in data type in Python. 
A dictionary is a collection of data in the form of key-value pairs. 
Dictionaries are defined with curly braces ({}) and they contain key-value pairs separated by commas. 
Each key is followed by a colon (:) and the value:'''

# Note that each key should be unique

{'amount': 50.0, 'category': 'Food'}
# Printing an empty dictionary
empty_dict ={}
print(empty_dict)

# Using the dict() function
empty_dict_1 =dict()
print(empty_dict_1)


customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True,
    "height": 30.5
}

# We can access items in the dictionary using square brackets
print(customer["name"])

# If you pass a key that does not exist, you get KeyError
# print(customer["fname"])
# The keys are case sensitive

# We can use the .get() method to access the values, if it does not exist we can pass it a default value
print(customer.get("sname", "Doe")) # It returns None is no default value is passed into it


