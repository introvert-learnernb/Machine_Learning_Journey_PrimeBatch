## read, write 
# basic_io.py
# Demonstrates text file write, append, read, and line-by-line iteration.
# path = "D:\ML_Learning\Prime_Batch\temp.txt"

# def write_text_file(path):
#     # Use a context manager so the file is always closed.
#     with open(path, "w", encoding="utf-8") as f:
#         f.write("Line 1\n")
#         f.write("Line 2\n")
#         f.write("Line 3\n")

# def append_text_file(path):
#     with open(path, "a", encoding="utf-8") as f:
#         f.write("Appended line\n")

# def read_entire_file(path):
#     with open(path, "r", encoding="utf-8") as f:
#         return f.read()

# def read_line_by_line(path):
#     with open(path, "r", encoding="utf-8") as f:
#         for i, line in enumerate(f, start=1):
#             print(f"{i}: {line.rstrip()}")  # rstrip to remove trailing newline for display

# def safe_open_example(path):
#     try:
#         with open(path, "r", encoding="utf-8") as f:
#             return f.read()
#     except FileNotFoundError:
#         print("File not found:", path)
#     except OSError as e:
#         print("OS error:", e)

# if __name__ == "__main__":
#     filename = "notes.txt"
#     write_text_file(filename)
#     append_text_file(filename)
#     full = read_entire_file(filename)
#     print("Full file content:\n", full)
#     print("Reading line by line:")
#     read_line_by_line(filename)


# # try , catch , else, finally 

# def divide_by_user_input():
#     s = input("Enter a number to divide 10 by: ")
#     try:
#         # Try to convert input and do the division
#         n = int(s)
#         result = 10 / n
#     except ValueError:
#         # Handles non-integer input (e.g., "abc")
#         print("Error: you must enter a valid integer.")
#     except ZeroDivisionError:
#         # Handles division by zero
#         print("Error: cannot divide by zero.")
#     else:
#         # Runs only if no exception was raised in the try block
#         print("Success: 10 divided by", n, "is", result)
#     finally:
#         # Always runs, used for cleanup or final logging
#         print("Finally: done (this always runs).")

# if __name__ == "__main__":
#     divide_by_user_input()


# list_comprehension_simple.py
# Simple demonstrations of Python list comprehensions.

# def basic_mapping():
#     # Square numbers 0..9
#     squares = [x * x for x in range(10)]
#     print("squares:", squares)

# def filtering():
#     # Even numbers from 0..9
#     evens = [x for x in range(10) if x % 2 == 0]
#     print("evens:", evens)

# def nested_loops():
#     # Cartesian product of ranges
#     pairs = [(x, y) for x in range(3) for y in range(2)]
#     print("pairs:", pairs)

# def conditional_expression():
#     # Use inline if/else to produce different items
#     labels = [("even" if x % 2 == 0 else "odd") for x in range(6)]
#     print("labels:", labels)

# def flatten_matrix():
#     # Flatten a 2D list (matrix) into a single list
#     matrix = [[1, 2, 3], [4, 5, 6]]
#     flat = [n for row in matrix for n in row]
#     print("flat:", flat)

# def transform_strings():
#     fruits = ["apple", "banana", "cherry"]
#     upper = [s.upper() for s in fruits]
#     print("upper:", upper)

# if __name__ == "__main__":
#     basic_mapping()
#     filtering()
#     nested_loops()
#     conditional_expression()
#     flatten_matrix()
#     transform_strings()


## JSON MODULE .........

import json 

data = { "name": "John", "age": 25, "marks": [85, 90, 92] }
json_string = json.dumps(data) 
print(json_string)

json_data = '{"name": "John", "age": 25}' 
python_obj = json.loads(json_data)
print(python_obj["name"])

with open("data.json","r") as f:
    data = json.load(f)
    
print(data)

data = {"name": "Aisha", "city": "Delhi"} 
with open("data.json", "w") as f: 
    json.dump(data, f, indent=4)