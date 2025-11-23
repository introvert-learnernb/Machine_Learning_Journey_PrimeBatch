#strings

# first_string = "Hello"
# second_string = "World"

# Concatenate strings
# full_string = first_string + " " + second_string

# print("Concatenated String:", full_string)

# indexing in strings
# print("First character of first_string:", first_string[0])
# print("Last character of second_string:", second_string[-1])

#strings are immutable : any certain character within a string cannot be changed directly
# first_string[0] = 'h'  # This will raise an error

# string Slicing

# sliced_string = full_string[0:5]  # 'Hello' // 0 to 4 index
# print("Sliced String (0-5):", sliced_string)

# new_sliced_string = full_string[6:]  # 'World' // 6 to end
# print("Sliced String (6-end):", new_sliced_string)

# Reversing a string using slicing
# reversed_string = full_string[::-1]
# print("Reversed String:", reversed_string)

#fstrings

# name = "Alice"
# age = 30
# greeting = f"My name is {name} and I am {age} years old."
# print(greeting)

#data types like tuple, list, set, dictionary

#list - ordered, mutable, allows duplicates , different data types

# my_list = [1, 2, 3, "Hello", 4.5, "World"]
# print("Original List:", my_list)

# my_list.append("New Item")
# print("List after appending an item:", my_list)

# my_list[0] = 10
# print("List after modifying first element:", my_list)

#slicing can be done in lists too
# sliced_list = my_list[1:4]
# print("Sliced List (1-4):", sliced_list)

# reversed_list = my_list[::-1]
# print("Reversed List:", reversed_list)

#insert at specific index
# my_list.insert(2, "Inserted Item")
# print("List after inserting an item at index 2:", my_list)

#sort - only works if all elements are of same data type
# num_list = [5, 2, 9, 1, 6]

# num_list.sort()
# print("Sorted Number List:", num_list)

# num_list.reverse()
# print("Reversed Number List:", num_list)

#remove element from list
# num_list.remove(9)
# print("Number List after removing 9:", num_list)

#looping in list 

# x = 5
# idx = 0

# for item in my_list:
#     if item == x:
#         print(f"Item {x} found at index {idx}")
#         break
#     idx += 1


#Tuple - ordered, immutable, allows duplicates , different data types

# tup = (1, 2, 3, "Hello", 4.5, "World")
# print("Original Tuple:", tup)

# tup[0] = 10  # This will raise an error

# new_tup = (3)
# print(type(new_tup))  # <class 'int'>

# correct_tup = (3,)
# print(type(correct_tup))  # <class 'tuple'>

#index method in tuple

# tup = (1,2,4,3,2)
# index_of_3 = tup.index(3)
# print("Index of 3 in tuple:", index_of_3)


# #count method in tuple
# count_of_2 = tup.count(2)
# print("Count of 2 in tuple:", count_of_2)

#dictionary - unordered, mutable, key-value pairs, keys are unique

# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "numbers" : [1,2,3,4,5] 
# }

# print("Original Dictionary:", my_dict)

# # Accessing values
# print("Name:", my_dict["name"])
# print("Age:", my_dict.get("age")) # if the key doesn't exits, it returns None instead of raising an error
# print("Numbers:", my_dict["numbers"])

# #changing value of dictionary
# my_dict["age"] = 31
# print("Dictionary after changing age:", my_dict)

# #dictionary methods 

# #returning all keys
# keys = my_dict.keys()
# print("Dictionary Keys:", keys)

# #returning all values
# values = my_dict.values()
# print("Dictionary Values:", values)

# #returning all key-value pairs
# items = my_dict.items()
# print("Dictionary Items:", items)

# #adding new key-value pair
# my_dict["profession"] = "Engineer"
# print("Dictionary after adding profession:", my_dict)

# my_dict.update({"hobby": "Painting"})
# print("Dictionary after adding hobby using update():", my_dict)

# #removing key-value pair
# removed_value = my_dict.pop("city")
# print("Removed Value (city):", removed_value)

# #sets - unordered, mutable, no duplicates , different data types

# my_set = {1,2,2,2,2,3,"Hello",4.5,"World"}
# print("Original Set:", my_set)

# #Adding and removing elements in set

# my_set.add("New Item")
# print("Set after adding an item:", my_set)

# my_set.remove(2)
# print("Set after removing 2:", my_set)

# my_set.discard(10)  # Does not raise an error if element not found
# print("Set after discarding 10 (not present):", my_set)

# my_set.pop()  # Removes and returns an arbitrary element
# print("Set after popping an element:", my_set)

# new_set = {3,4,5,"Hello"}

# #union
# union_set = my_set.union(new_set)
# print("Union of sets:", union_set)

# #intersection
# intersection_set = my_set.intersection(new_set)
# print("Intersection of sets:", intersection_set)

# #difference
# difference_set = my_set.difference(new_set)
# print("Difference of sets (my_set - new_set):", difference_set)


