# # Create bank account class with deposit and withdraw & check balance methods

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute

#     # Getter method for account number
#     def get_account_number(self):
#         return self.__account_number

#     # Getter method for balance
#     def get_balance(self):
#         return self.__balance

#     # Method to deposit money - Setter method
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"Deposited: ${amount}. New Balance: ${self.__balance}"
#         else:
#             return "Deposit amount must be positive."

#     # Method to withdraw money
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             return f"Withdrew: ${amount}. New Balance: ${self.__balance}"
#         else:
#             return "Insufficient funds or invalid withdrawal amount."
        
# # Creating an instance of BankAccount
# account = BankAccount("123456789", 1000)
# print(account.get_account_number())  # Accessing private attribute via getter
# print(account.get_balance())  # Accessing private attribute via getter
# print(account.deposit(500))  # Depositing money
# print(account.withdraw(200))  # Withdrawing money


# # Create a Class called Book with attributes title, author, and list of reviews and add methods add a new review, count reviews, display all reviews
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.reviews = []  # List to store reviews

#     # Method to add a new review
#     def add_review(self, review):
#         self.reviews.append(review)
#         return "Review added."

#     # Method to count reviews
#     def count_reviews(self):
#         return len(self.reviews)

#     # Method to display all reviews
#     def display_reviews(self):
#         return self.reviews if self.reviews else "No reviews available."
    
# # Creating an instance of Book
# my_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
# print(my_book.add_review("A fascinating exploration of the American Dream."))  # Adding a
# # review
# print(my_book.add_review("Beautifully written with complex characters."))  # Adding another review
# print(f"Total Reviews: {my_book.count_reviews()}")  # Counting reviews
# print("All Reviews:", my_book.display_reviews())  # Displaying all reviews

## Encapsulation Assignment
# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks
    
#     def get_name(self):
#         return self.__name
    
#     def get_roll_no(self):
#         return self.__roll_no
    
#     def get_marks(self):
#         return self.__marks
    
#     def set_marks(self, marks):
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks
#             return "Marks updated."
#         else:
#             return "Invalid marks. Please enter a value between 0 and 100."
    
#     def set_roll_no(self, roll_no):
#         if roll_no >= 1 and roll_no <= 100:
#             self.__roll_no = roll_no
#             return "Roll number updated."
#         else:
#             return "Invalid roll number. Please enter a value between 1 and 100."
    
#     def set_name(self, name):
#         if name == "":
#             return "Name cannot be empty."
#         else:
#             self.__name = name
#             return "Name updated."
        
        
        
# # Creating an instance of Student
# student = Student("Alice", 10, 85)
# print(student.get_name())  # Accessing private attribute via getter
# print(student.get_roll_no())  # Accessing private attribute via getter
# print(student.get_marks())  # Accessing private attribute via getter

# print(student.set_marks(90))  # Updating marks
# print(student.get_marks())  # Accessing updated marks via getter

# print(student.set_roll_no(15))  # Updating roll number
# print(student.get_roll_no())  # Accessing updated roll number via getter

# print(student.set_name("Bob"))  # Updating name
# print(student.get_name())  # Accessing updated name via getter
    

# ## Function Overriding Assignment

# class Shape:
#     def area(self):
#         return "Area of shape"
    
# class Circle(Shape):
#     def area(self, radius):
#         return 3.14 * radius * radius
    
# class Rectangle(Shape):
#     def area(self, length, width):
#         return length * width
    
# class Triangle(Shape):
#     def area(self, base, height):
#         return 0.5 * base * height
    
# # Creating instances of each shape
# circle = Circle()
# rectangle = Rectangle()
# triangle = Triangle()

# print(f"Circle Area: {circle.area(5)}")  # Output: Circle Area: 78.5
# print(f"Rectangle Area: {rectangle.area(4, 6)}")  # Output : Rectangle Area: 24
# print(f"Triangle Area: {triangle.area(3, 8)}")  # Output : Triangle Area: 12.0


# ## Inheritance Assignment

# class Vehicle:
#     def __init__(self, brand, model):
#         self._brand = brand
#         self._model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand,model)
#         self._seats = seats
        
#     def info(self):
#         print(f'Car of {self._brand}, {self._model} has {self._seats} seats')
        
# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self._engine_cc = engine_cc
        
#     def info(self):
#         print(f'Bike of {self._brand}, {self._model} has {self._engine_cc} cc engine')
        
# car = Car('Tata','brezza','4')
# bike = Bike('Hero','Xpulse','180')
# car.info()
# bike.info()


# ## Abstraction Assignment 
# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self): #implementation will be provided by subclasses
#         pass
    
# class Intern(Employee):
#     def __init__(self, work_hours, rate):
#         self.work_hours = work_hours
#         self.rate = rate

#     def calculate_salary(self): #implementation will be provided by subclasses
#         return self.work_hours * self.rate
   
# class FullTimeEmployee(Employee):
#     def __init__(self, work_hours, rate):
#         self.work_hours = work_hours
#         self.rate = rate

#     def calculate_salary(self): #implementation will be provided by subclasses
#         return self.work_hours * self.rate * 1.5

# class ContractEmployee(Employee):
#     def __init__(self, work_hours, rate):
#         self.work_hours = work_hours
#         self.rate = rate

#     def calculate_salary(self): #implementation will be provided by subclasses
#         return self.work_hours * self.rate * 1.2

# # Creating instances of Rectangle and Circle
# intern = Intern(4,20)
# int_sal = intern.calculate_salary()
# print(int_sal)

# fullTimeEmployee = FullTimeEmployee(6,49)
# ful_sal = fullTimeEmployee.calculate_salary()
# print(ful_sal)

# contractemp = ContractEmployee(5,34)
# cont_sal = contractemp.calculate_salary()
# print(cont_sal)

# class Person:
#     def __init__(self, name, age = 18, address = 'mnr'):
#         self._name = name
#         self._age = age
#         self._address = address
    
#     def info(self):
#         print(f'I am {self._name} and i am {self._age} yrs old and have address {self._address}')
        
# person = Person('Neev')
# person2 = Person('Manish',22)
# person3 = Person('Bibek',22, 'ktm')

# person.info()
# person2.info()
# person3.info()

## instance and class attributes

# class Player:
#     player_count = 0 # class attribute
    
#     def __init__(self,name,level):
#         self.name = name #instance attribute
#         self.level = level
#         Player.player_count += 1
        
#     def info(self):
#         print(f'I am {self.name}, I am Cricket Player and I play at {self.level} level')

#     def total_count():
#         print(Player.player_count)
        
# p1 = Player('rimal','national')
# p1.info()
# p2 = Player('rajat','international')
# p2.info()
# p3 = Player('darshan','national')
# p3.info()
# Player.total_count()

# ## Multiple Inheritance 

# class Herbivore:
#     def __init__(self, veggies):
#         self.veggies = veggies 
        
# class Carnivore:
#     def __init__(self, chickens):
#         self.chickens = chickens
        
# class Omnivore:
#     def __init__(self, omni):
#         self.omni = omni
        
# class Bear(Herbivore,Carnivore, Omnivore):
#     def __init__(self, veggies, chickens, omni):
#         Herbivore.__init__(self,veggies)
#         Carnivore.__init__(self,chickens)
#         Omnivore.__init__(self, omni)
        
#     def info(self):
#         print(f"I eat {self.veggies} veggies, {self.chickens} chickens, {self.omni} omnis")
        
# h = Herbivore(2)
# c = Carnivore(4)
# o = Omnivore(6)
# bear = Bear(4,2,6)
# bear.info()



# Class for Users
class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


# Class for Messages
class Message:
    def __init__(self, sender, content):
        self.sender = sender  # User object
        self.content = content

    def display(self):
        print(f"{self.sender}: {self.content}")


# Class for ChatRoom
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []       # list of User objects
        self.messages = []    # list of Message objects

    # User joins the chat
    def join(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user} joined {self.room_name}.")

    # User leaves the chat
    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user} left {self.room_name}.")

    # Sending a message
    def send_message(self, user, content):
        if user in self.users:
            msg = Message(user, content)
            self.messages.append(msg)
        else:
            print(f"{user} is not in the chatroom!")

    # Viewing chat history
    def show_history(self):
        print(f"\n--- Chat History of {self.room_name} ---")
        for msg in self.messages:
            msg.display()
        print("--- End of Chat ---\n")


# Example Usage
u1 = User("Alice")
u2 = User("Bob")
chat = ChatRoom("Friends")

chat.join(u1)
chat.join(u2)

chat.send_message(u1, "Hi Bob!")
chat.send_message(u2, "Hello Alice! How are you?")
chat.send_message(u1, "I'm good, thanks!")

chat.show_history()

chat.leave(u2)

    

