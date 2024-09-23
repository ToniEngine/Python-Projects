# Variable is a container for a value. It behaves as the value it contains
x = "Bro"
y =21
z = False

# A string is a series of characters
name = "Anthony Obot"
print("Hello " + name)

#checking the datatype of a variable using the type function type()
#strings as a datatype
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

#typecasting coverst the data type of a value to another value
print("Your age is: " + str(age ))

print(f"Your age is: ", age)
print(f"Your Height is ", height ,"cm")

#Boolean Datatype: Datatype value that only stores True or False
human = False
print(human)
print(type(human)) #<class "bool">






