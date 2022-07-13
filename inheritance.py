# Object oriented programming in Python
# Inheritance Basics

# Inheriting from an upper level class/ Parent class
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f'I am {self.name} and I am {self.age} years old')
#
# # Adding extra attributes to a lower level class
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def speak(self):
#         print('Meow')
#
#     def show(self):
#         print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')
#
#
# class Dog(Pet):
#     def speak(self):
#         print('bark')
#
#
# d1 = Dog('Bolingo', 1)
# d1.show()
# c1 = Cat('Garfield', 5, 'Gold')
# c1.show()


# Class Methods and Class Attributes
class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


p1 = Person('Seb')
print(p1.number_of_people)
p2 = Person('Jasto')
print(p2.number_of_people)





