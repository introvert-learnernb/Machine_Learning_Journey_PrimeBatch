#Classes and Objects in Python

# class Dog:
#     # Class attribute - can be accessed directly using class name
#     species = "Canis familiaris"
#     PI = 3.14
#     # Initializer / Instance attributes
#     # class can have only one __init__ method
#     def __init__(self, name, age):
#         self.name = name  #object attribute - can be accessed using object
#         self.age = age
#         PI = 3.143 #local variable - can be accessed only within this method

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
# # Instantiate the Dog object
# my_dog = Dog("Buddy", 3)
# print(my_dog.description())  # Output: Buddy is 3 years old

# print(Dog.PI)  # Accessing class attribute using class name
# print(my_dog.PI)  # Accessing class attribute using object

# #self keyword refers to the instance of the class i.e. the object itself.
# print(my_dog.speak("Woof Woof"))  # Output: Buddy says Woof Woof

# #Instance and class methods 

# class Product:
    
#     count = 0  # Class attribute to keep track of number of products
    
#     def __init__(self, name, price):
#         self.name = name  # Instance attribute
#         self.price = price  # Instance attribute
#         Product.count += 1  # Increment the product count whenever a new product is created 
        
#     def get_info(self):
#         return f"Product Name: {self.name}, Price: ${self.price}"
    
#     @classmethod
#     def get_product_count(cls):
#         return f"Total Products: {cls.count}"
    
#     @staticmethod
#     def cal_discount(price, discount):
#         return price - (price * discount / 100)
    
# p1 = Product("Laptop", 1200)
# p2 = Product("Smartphone", 800)
# print(p1.get_info())  # Output: Product Name: Laptop, Price: $1200
# print(p2.get_info())  # Output: Product Name: Smartphone, Price: $800
# print(Product.get_product_count())  # Output: Total Products: 2
# discounted_price = Product.cal_discount(1200, 10)
# print(f"Discounted Price: ${discounted_price}")  # Output: Discounted Price  

#Encapsulation in Python
#Private attributes and methods are those that cannot be accessed directly from outside the class. (only accessible within the class)
#Protected attributes and methods are those that should not be accessed directly from outside the class, but can be accessed by subclasses. (conventionally indicated by a single underscore _)
#Public attributes and methods are those that can be accessed from anywhere.
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter method for account number
    def get_account_number(self):
        return self.__account_number

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Method to deposit money - Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: ${amount}. New Balance: ${self.__balance}"
        else:
            return "Deposit amount must be positive."

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: ${amount}. New Balance: ${self.__balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."
        
# Creating an instance of BankAccount
account = BankAccount("123456789", 1000)
print(account.get_account_number())  # Accessing private attribute via getter
print(account.get_balance())  # Accessing private attribute via getter
print(account.deposit(500))  # Depositing money
print(account.withdraw(200))  # Withdrawing money
print(account.get_balance())  # Checking balance after transactions


#Inheritance in Python
class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def get_info(self):
        return f"Vehicle Make: {self._make}, Model: {self._model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.doors = doors

    def get_info(self):
        parent_info = super().get_info()  # Call the method from the parent class
        return f"{parent_info}, Doors: {self.doors}"

# Creating an instance of Car
my_car = Car("Toyota", "Camry", 4)
print(my_car.get_info())  # Output: Vehicle Make: Toyota, Model: Camry, Doors: 4

#Types of Inheritance
#1. Single Inheritance - A class inherits from one parent class.
#2. Multiple Inheritance - A class inherits from more than one parent class.
#3. Multilevel Inheritance - A class inherits from a parent class, which in turn inherits from another parent class.
#4. Hierarchical Inheritance - Multiple classes inherit from a single parent class.

#Example of Multiple Inheritance
class Flyer:
   def __init__(self, wing_span):
       self.wing_span = wing_span
   def fly(self):
       return f"Flying with a wingspan of {self.wing_span} meters."
   
class Swimmer:
    def __init__(self, fin_size):
         self.fin_size = fin_size
    def swim(self):
         return f"Swimming with fins of size {self.fin_size} cm."
     
class Duck(Flyer, Swimmer):
    def __init__(self, wing_span, fin_size):
        Flyer.__init__(self, wing_span)
        Swimmer.__init__(self, fin_size)
        
    def info(self):
        return f"Duck with wingspan {self.wing_span} meters and fin size {self.fin_size} cm."
    
# Creating an instance of Duck
my_duck = Duck(1.5, 20)
print(my_duck.info())  # Output: Duck with wingspan 1.5 meters and fin size 20 cm.
print(my_duck.fly())   # Output: Flying with a wingspan of 1.5 meters.
print(my_duck.swim())  # Output: Swimming with fins of size 20 cm.



#Abstraction in Python - Hiding complex implementation details and showing only the essential features of the object.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): #implementation will be provided by subclasses
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of Rectangle and Circle
rect = Rectangle(5, 10)
circle = Circle(7)
print(f"Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")