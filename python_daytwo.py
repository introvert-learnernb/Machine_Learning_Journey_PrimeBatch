#conditional statements 

# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")
    
#odd or even

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(number, "is an even number.")
# else:
#     print(number, "is an odd number.")


#Nesting

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if (username == "admin"):
#     if (password == "password123"):
#         print("Access granted.")
#     else:
#         print("Incorrect password.")


#Handling Multiple Cases 

# color = input("Enter a color (red, blue, green): ").lower()

# match color:
#     case "red":
#         print("You chose red.")
#     case "blue":
#         print("You chose blue.")
#     case "green":
#         print("You chose green.")
#     case _:
#         print("Color not recognized.")


#loops  


# i = 1

# while i <= 10:
#     print("Hello, World!", i)
#     i += 1
    
# print("After loop , i =", i)


#multiplication table for any number n

# n = int(input("Enter a number to generate its multiplication table: "))

# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1
# print("Multiplication table for", n, "completed.")

#break and continue

#break exits from loop
#continue skips the current iteration and moves to the next one

# for i in range(1, 11):
#     if i == 5:
#         print("Skipping number 5")
#         continue
#     if i == 8:
#         print("Stopping the loop at number 8")
#         break
#     print("Current number:", i)
    
#for loop
#range function - range(start, stop, step)  - range(n) 0 to n-1 - range(1,n) 1 to n-1 - range(1,n,2) 1 to n-1 with step 2


# for i in range(1, 11):
#     print("Hello, World!", i)
    
#counting number of i's in Application word

# count = 0
# for char in "Application":
#     if char == 'i':
#         count += 1
# print("Number of 'i's in 'Application':", count)

#counting number of vowels in a string

# count = 0
# for char in "Education":
#     if char.lower() in 'aeiou':
#         count += 1
# print("Number of vowels in 'Education':", count)

#sum of first n natural numbers

# n = int(input("Enter a positive integer n to calculate the sum of first n natural numbers: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
    
# print("The sum of first", n, "natural numbers is:", sum)

#functions 

# def avg(a,b,c = 3): #non-default parameter should come before default parameter
#     return (a + b + c) / 3

# print(avg(10, 20))

#lambda function 
#why lambda function - to create small anonymous functions at runtime without using def keyword
#lambda is fast why because it is optimized for performance and used for simple operations
#lambda is optimized for performance how ? - it avoids the overhead of function calls and is implemented in C internally

# square = lambda x: x * x
# print(square(5))

#Calculating factorial using function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print("The factorial of", num, "is:", result)