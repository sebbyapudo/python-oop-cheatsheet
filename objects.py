# Object Oriented programming in Python
# Defining objects

# x = 5
# print(type(x))

#  Accessing methods
# string = 'Hello'
# print(string.upper())

# Creating classes
class Dog:

    def add_number(self, x):
        return x + 5

    def bark(self):
        print('Woof')


d1 = Dog()
d1.bark()
print(d1.add_number(2))