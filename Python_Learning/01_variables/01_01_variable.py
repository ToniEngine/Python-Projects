#  Variables are used to temporarily store data in the computer memory
#  Variable is a container for a value. It behaves as the value it contains
x = "Bro"   # String Datatype
y =21       # Integer Datatype
z = False   # Boolean Datatype


# A string is a series of characters
name = "Anthony Obot"
print("Hello " + name)

# Checking the datatype of a variable using the type function type()

# Strings as a datatype
first_name = "Anthony"
last_name = "Obot"
full_name= first_name + " " + last_name
print(type(first_name))
print(f"Hello ", full_name) # using the f-string



#Int Data type for storing integers and floats

age = 21
print(type(age))  # <class "int" >
age = age + 1 # alternatively age += 1
print(age)

#float datatype (stores decimal or floating point number)
height = 250.5
print(type(height))   #<class "float">

#typecasting coverts the data type of a value to another value
print("Your age is: " + str(age))

print(f"Your age is: ", age)
print(f"Your Height is ", height ,"cm")

#Boolean Datatype: Datatype value that only stores True or False
human = False
print(human)
print(type(human)) #<class "bool">




price = 10
price = 20   # You can reassign a new value to a variable
print(price)


# Note that python is a case sensitive language
 

#  Complex Numbers
num = 2 +3j
print(type(num))



