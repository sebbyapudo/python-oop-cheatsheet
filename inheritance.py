# Object oriented programming in Python
# Inheritance Basics

# Inheriting from an upper level class/ Parent class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')


class Cat(Pet):
    def speak(self):
        print('Meow')


class Dog(Pet):
    def speak(self):
        print('bark')