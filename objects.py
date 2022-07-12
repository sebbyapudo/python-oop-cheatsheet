# Object Oriented programming in Python
# Defining objects

# x = 5
# print(type(x))

#  Accessing methods
# string = 'Hello'
# print(string.upper())

# Creating classes
# class Dog:
#     # Constructor / Dunder methods in py
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#
# d1 = Dog("Seb", 21)
# d1.set_age(22)
# d2 = Dog('Njenga', 20)
#
# print(d1.get_age())
# print(d2.get_age())


# An Example to Show how different classes can interact with each other

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student('Seb', 21, 91)
s2 = Student('Jasto', 19, 98)
s3 = Student('Byrone', 19, 96)

course = Course('CompScience', 2)
course.add_student(s1)
course.add_student(s2)

print(course.students[0].name + ':', course.students[0].age)
print(course.get_average_grade())






