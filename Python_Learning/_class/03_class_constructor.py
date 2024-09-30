


class Point:
    def __init__(self, x, y):    # Constructor
        self.x =x
        self.y =y

point = Point(10,20)
point.x =11
print(point.x)
print(point.y)





class Person:
    def __init__(self, name):
        self.name =name

    def talk(self):
        print(f"Hi, I am {self.name}")
         
chatbot1 = Person("John Smith")
chatbot1.talk()

# Note each object is a different instance of our Person class
chatbot2 = Person("Jane Doe")
chatbot2.talk()

