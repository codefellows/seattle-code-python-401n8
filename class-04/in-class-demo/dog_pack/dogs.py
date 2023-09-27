from abc import ABC


class Mammals:
    pass


class Dog(ABC):
    """
    Base class for different dogs, each having their own breed.
    """

    # Dunder init, defines the "Instance Variables"
    # It's like the constructor method in JavaScript
    # `self` refers to the instance in Python
    def __init__(self, name="unknown"):
        self.name = name
        self.furry = True
        self.legs = 4


class Lab(Dog):
    # class variables
    scientific_name = "Canis lupus familiaris"  # Lab.scientific_name

    # static methods don't refer to the instance!
    @staticmethod
    def bark():
        return "Arf!"

    # class method
    @classmethod
    def give_scientific_name(cls):  # Lab.give_scientific_name()
        return cls.scientific_name

    # the string representation of my object
    # used in print() and str()
    # __str__ is user friendly
    def __str__(self):
        return f"I'm a lab! My name is {self.name}"

    # also returns a string
    # the formula for creating the object
    # __repr__ is developer friendly
    def __repr__(self):
        return f'Lab("{self.name}")'


class Husky(Dog):
    def bark(self):
        return f"Growl! I'm {self.name}!"


# This is an example of multiple inheritance
# Order matters for MRO: Method Resolution Order
class LabHuskyMix(Lab, Husky):
    pass


# A collection of Dogs
class DogPack:
    """
    DogPack is a collection of Dog instances
    """
    def __init__(self, members=None, name="unknown"):
        self.members = members or []
        self.name = name

