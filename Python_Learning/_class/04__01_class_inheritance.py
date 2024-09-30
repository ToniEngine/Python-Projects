# Inheritance = it is a mechanism for reusing code


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")
        

class Cat(Mammal):
    def meow(self):
        print("meow")

bingo = Dog()
mickey_mouse = Cat()

bingo.walk()
mickey_mouse.walk()

bingo.bark()
mickey_mouse.meow()