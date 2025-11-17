#1. User Input as string and output

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello, " + name + "! You are " + age + " years old.")


#2. Number as input and arithmetic operation on them
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# sum_result = num1 + num2
# print("The sum of", num1, "and", num2, "is:", sum_result)

# diff_result = num1 - num2
# print("The difference when", num2, "is subtracted from", num1, "is:", diff_result)

# prod_result = num1 * num2
# print("The product of", num1, "and", num2, "is:", prod_result)

# div_result = num1 / num2
# print("The division of", num1, "by", num2, "gives:", div_result)

#3. Ask the user to enter two integers and one float .Convert them all to floats and print their average

# int1 = int(input("Enter first integer: "))
# int2 = int(input("Enter second integer: "))
# flt = float(input("Enter a float number: "))
# average = (float(int1) + float(int2) + flt) / 3
# print("The average of", int1, ",", int2, "and", flt, "is:", average)

#4. Take user input as string and convert it to integer, float and back to string and print all the values

# user_input = input("Enter a value: ")
# as_int = int(user_input)
# as_float = float(user_input)
# as_str = str(user_input)

# print("As Integer:", as_int)
# print("As Float:", as_float)
# print("As String:", as_str)

#5. Evaluate an expression and explain how operator precedence works in that expression

# x = 10 + 3 * 2 ** 2   # ** > * > + (operator precedence)
# print("The result of the expression 10 + 3 * 2 ** 2 is:", x)

#6. Swapping values of two variables using a temporary variable

# a = input("Enter value for a: ")
# b = input("Enter value for b: ")

# print("Before swapping: a =", a, ", b =", b)

# temp = a
# a = b
# b = temp

# print("After swapping: a =", a, ", b =", b)

#7. Conversion of temperature from Celsius to Fahrenheit and vice versa

# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(celsius, "Celsius is equal to", fahrenheit, "Fahrenheit")


#8. Calculate the area of circle given its radius

# import math
# radius = float(input("Enter the radius of the circle: "))
# area = math.floor(math.pi * radius ** 2)
# print("The area of the circle with radius", radius, "is:", area)

#9. Calculate simple interest given principal, rate of interest and time
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest (in %): "))
# time = float(input("Enter the time (in years): "))
# simple_interest = (principal * rate * time) / 100
# print("The simple interest is:", simple_interest)

#10. Take float number as input and print its integer part and decimal part separately

# num = float(input("Enter a float number: "))
# integer_part = int(num)
# decimal_part = num - integer_part
# print("Integer part:", integer_part)
# print("Decimal part:", round(decimal_part,2))  # rounding to avoid floating point precision issues
