#print function and string 
print("Hello, World!")

#variables 
my_name = "Neev"
my_age = 22

print("My name is", my_name, "and I am", my_age, "years old.")  #indentation matters in python

#data types
my_integer = 10
my_float = 20.5
my_string = "Python is fun!"
my_boolean = True
print(type(my_integer))  # <class 'int'>
print(type(my_float))    # <class 'float'>
print(type(my_string))   # <class 'str'>
print(type(my_boolean))  # <class 'bool'>

#single line comment
''' 
multi-line 
comment

'''

#snake_case  (all letters are lowercase with underscores between words)
#camelCase  (first letter of the first word is lowercase, and the first letter of each subsequent word is uppercase)
#PascalCase (first letter of each word is uppercase, with no underscores)

#basic arithmetic operations
a = 15
b = 4
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

#Relational operators
x = 10
y = 20

print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x > y:", x > y)     # False
print("x < y:", x < y)     # True
print("x >= y:", x >= y)   # False
print("x <= y:", x <= y)   # True

#Assignment operators

c = 5
c += 3  # c = c + 3
c -= 2  # c = c - 2
c *= 4  # c = c * 4
c /= 2  # c = c / 2

print("Final value of c:", c)

#Logical operators
p = True
q = False

print("p and q:", p and q)  # False
print("p or q:", p or q)    # True
print("not p:", not p)      # False
print("not q:", not q)      # True

#operators precedence

# Parentheses
result = (2 + 3) * 4
print("Result with parentheses:", result)  # 20

# Exponentiation
result = 2 + 3 ** 2 * 4
print("Result with exponentiation:", result)  # 38

# Multiplication and Division
result = 20 / 4 * 2 + 3
print("Result with multiplication and division:", result)  # 13.0

# Addition and Subtraction
result = 10 - 2 + 5
print("Result with addition and subtraction:", result)  # 13

#logical operators precedence
a = True
b = False
c = True
result = not a or b and c  # 'not' has higher precendence than 'and' has higher precedence than 'or'
print("Result of logical operators precedence:", result)  # True

#type conversion
num_str = "100"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float
print("String to Integer:", num_int)
print("String to Float:", num_float)
int_to_str = str(num_int)  # Convert integer to string
print("Integer to String:", int_to_str)


#user input

a = input("Enter a number: ")  # input() returns a string
b = input("Enter another number: ")

avg = (int(a) + int(b)) / 2  # Convert inputs to integers for calculation
print("The average of", a, "and", b, "is:", avg)