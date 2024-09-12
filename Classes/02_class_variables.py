# class variables = Shared among all instance of a class
#   Defined outside the constructor
#   Allow you to share data among all objects created from that class



class Student:

    class_year = 2024 #Class Variable are shared among all instances of the class
    num_student= 0
    def __init__(self, name, age):
        self.name = name
        self.age= age
        Student.num_student += 1

student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)
student3 =Student("Sqiudward", 55)
student4 = Student("Sandy",27)

print(student1.name)
print(student1.age)

print(Student.class_year)
print(Student.class_year)


print(Student.num_student)
print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
