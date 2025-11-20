#Calculating final tax rate based on income

# def calculate_tax_rate(income):
#     if income > 70000:
#         tax_rate = 0.25
#     elif income >= 30000 and income <= 70000:
#         tax_rate = 0.15
#     elif income < 30000:
#         tax_rate = 0.05
#     return tax_rate


# salary = float(input("Enter your annual income: "))
# final_tax_rate = calculate_tax_rate(salary)
# print(f"Your final tax rate is: {final_tax_rate * 100}%")


#finding all the even numbers between a and b inclusive

# a = int(input("Enter the starting number (a): "))
# b = int(input("Enter the ending number (b): "))

# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(i, "is an even number.")

# printing out the digits of the number like of 312 print 3 1 2

# number = int(input("Enter a number: "))

# digits = []
# while number > 0:
#     digit = number % 10
#     digits.append(digit)
#     number = number // 10

# print("Digits in order:")
# for digit in reversed(digits):
#     print(digit)


# Counting the number of digits in a number

# number = int(input("Enter a number: "))
# count = 0
# while number > 0:
#     number = number // 10
#     count += 1
    
# print("Number of digits:", count)

# Returning the sum of digits of a number


# number = int(input("Enter a number: "))
# sum_of_digits = 0

# while number > 0:
#     digit = number % 10
#     sum_of_digits += digit
#     number = number // 10
    
# print("Sum of digits:", sum_of_digits)

# Printing numbers between 1 and 100 which are divisible by both 3 and 5 

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# if number is positive or negative (take inputs until user enters 0)

# while True:
#     num = int(input("Enter any number (enter 0 to quit):"))
    
#     if (num == 0):
#         break

# function to perform basic calculator operations

# def calculator(a, b, operation):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Error: Invalid operation"
    
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# op = input("Enter operation (+, -, *, /): ")

# result = calculator(num1, num2, op)
# print("Result:", result)

# Check if a number is prime or not
    
# num = int(input("Enter a number: "))
# flag = 0

# for i in range(2, num):
#     if num % i == 0:
#         flag = 1
#         break

# if (flag == 0):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

# Guess the secret number game

secret_number = 7

while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number.")
        break


        
