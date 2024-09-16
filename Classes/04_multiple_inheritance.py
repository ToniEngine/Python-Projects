# Multiple Inheritance =    inherit from more than one parent class
#                           C(A, B)


#Mulit_level Inheritance =   inherits from a parent whivh inherits from another parent
#                                C(B) <- B(A) <- A


class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()