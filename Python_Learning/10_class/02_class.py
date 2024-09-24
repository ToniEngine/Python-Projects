# We use classes to define new types to model real concepts
# Classes uses the pascal naming convention
# Classes simply defines the blueprint or template for creating objects
# An object is an instance of a class
# A method is a function inside a class
# A constructor is a function that gets called at the time of creating an object



class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

# Creating an object

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

# Each object is a different instance of a Point Class
point2 = Point()
point2.x = 1

print(point2.x)

 