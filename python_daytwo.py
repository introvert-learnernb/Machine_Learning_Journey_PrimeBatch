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


i = 1

while i <= 10:
    print("Hello, World!", i)
    i += 1
    
print("After loop , i =", i)