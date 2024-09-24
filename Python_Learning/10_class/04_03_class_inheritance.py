class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def run(self):
        print(f"{self.name} is running")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking Whuw! Whuw!")

dog1 = Dog("Bingo", 10)
dog1.bark()
dog1.run()
# print(dog1.name())
