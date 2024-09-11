
#A function that when called with the arguments passed into it, greets the user with his name and ask about the user location
# def greet_with_location(name, location):
#     print(f"Hello, {name}")
#     print(f"Hi, {name}, how is it in {location}")

# greet_with_location("Anthony", "Abuja") 


#Using Keywords arguments 
#greet_user(name="Antoine", location="Chicago")
def greet_user(name, location):
     print(f"Hello, {name}")
     print(f"Hi, {name}, how is the weather condition in {location}")

greet_user(location="Chicago", name="Antoine")

