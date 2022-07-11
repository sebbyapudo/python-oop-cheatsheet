# Object Oriented programming in Python
# Defining objects

# x = 5
# print(type(x))

#  Accessing methods
# string = 'Hello'
# print(string.upper())

# Creating classes
class Dog:
    # Constructor / Dunder methods in py
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d1 = Dog("Seb", 21)
d1.set_age(22)
d2 = Dog('Njenga', 20)

print(d1.get_age())
print(d2.get_age())
