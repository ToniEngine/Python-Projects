# Object Orientated Programming in Python

x = 1
print(type(x))  # Output: <class 'int'>
y = "Hello World"
print(type(y))  # Output: <class 'str'>
z = True
print(type(z)) # Output: <class 'bool'>
a = 3.14
print(type(a))  # Output: <class 'float'>


def greet_me():
    print("hello Toni")


print(type(greet_me))  # Output: <class 'function'>


# Methods
string = "hello"
print(string.upper())  # Output: "HELLO"


# Classes

class Dog:                  #Created a class called Dog
    # def __init__(self):
    def add_one(self, x):
        return x + 1
    

    def bark(self):
        print("bark")
    def meow(self):
        return "meow"
# A method is a function that goes inside a class


d= Dog()  #Instantiating by creating a new instance of the class Dog  i.e 
print(type(d))  # Output: <class '__main__.Dog'>
d.bark()




d.meow()
print(d.add_one(3))
 
        