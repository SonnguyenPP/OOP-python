
class Student:
    class_year = 2024
    num_student = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1
        
student1 = Student("son", 30)
student2 = Student("lan", 35)
student3 = Student("Vu",30)
student4 = Student("Nam",32)


print(f"Class{Student.class_year} {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)




