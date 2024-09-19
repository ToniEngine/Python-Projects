# object = A bundle of related attributes (variables) and methods (functions)
#  You need a class to create many objects
# class = (blueprint) used to design the structures and layout of a class


from car import Car


fortune_car = Car("Benz_AMG 300", 2026, "Gray", False)
Tony_car = Car("Lexus RX 350", 2020, "Gray", False)
print(fortune_car.model)
print(Tony_car.year)

fortune_car.drive()

Tony_car.start()
Tony_car.drive()

# car1 =Car("Mustang", 2024, "Red", False)
# print(car1)
# print(car1.model)
# print(car1.color)
# print(car1.year)

# car2 =Car("BMW", 2025, 'White', True)
# print(car2.for_sale, car2.model)

# car3 =Car("Dodge", 2026, "Green", True)
# print(car3.model)

# car1.start()
# car2.start()
# car3.start()
# print(" ")
# car1.drive()
# car2.drive()
# car3.drive()
# print(" ")
# car1.stop()
# car2.stop()
# car3.stop()
# print(" ")

# car1.describe()
# car2.describe()
# car3.describe()

our_car =Car("")
