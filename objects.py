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
    def __init__(self, name):
        self.name = name

    def add_number(self, x):
        return x + 5

    def bark(self):
        print('Woof')


d1 = Dog("Seb")
d2 = Dog('Njenga')

print(d1.name)
print(d2.name)
