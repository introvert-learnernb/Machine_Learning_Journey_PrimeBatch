#Classes and Objects in Python

class Dog:
    # Class attribute - can be accessed directly using class name
    species = "Canis familiaris"
    PI = 3.14
    # Initializer / Instance attributes
    # class can have only one __init__ method
    def __init__(self, name, age):
        self.name = name  #object attribute - can be accessed using object
        self.age = age
        PI = 3.143 #local variable - can be accessed only within this method

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
# Instantiate the Dog object
my_dog = Dog("Buddy", 3)
print(my_dog.description())  # Output: Buddy is 3 years old

print(Dog.PI)  # Accessing class attribute using class name
print(my_dog.PI)  # Accessing class attribute using object

#self keyword refers to the instance of the class i.e. the object itself.
print(my_dog.speak("Woof Woof"))  # Output: Buddy says Woof Woof

#Instance and class methods 

class Circle:
    # Class attribute
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    # Instance method - can access both instance and class attributes
    def area(self):
        return Circle.pi * (self.radius ** 2)

    # Class method - can only access class attributes
    @classmethod
    def circle_info(cls):
        return f"A circle is a shape with all points the same distance from its center. Value of pi is approximately {cls.pi}."