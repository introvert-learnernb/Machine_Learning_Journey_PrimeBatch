#strings

first_string = "Hello"
second_string = "World"

# Concatenate strings
full_string = first_string + " " + second_string

print("Concatenated String:", full_string)

# indexing in strings
print("First character of first_string:", first_string[0])
print("Last character of second_string:", second_string[-1])

#strings are immutable : any certain character within a string cannot be changed directly
# first_string[0] = 'h'  # This will raise an error

# string Slicing

sliced_string = full_string[0:5]  # 'Hello' // 0 to 4 index
print("Sliced String (0-5):", sliced_string)

new_sliced_string = full_string[6:]  # 'World' // 6 to end
print("Sliced String (6-end):", new_sliced_string)

# Reversing a string using slicing
reversed_string = full_string[::-1]
print("Reversed String:", reversed_string)

#fstrings

name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
print(greeting)



