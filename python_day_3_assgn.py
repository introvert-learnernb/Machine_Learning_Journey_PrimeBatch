#Check whether the given string is a palindrome or not

# str = input("Enter the string :")
# reversed_string = str[::-1]


# if (str == reversed_string):
#     print(f"The string '{str}' is a palindrome.")
 
# # Calculating average of numbers in a list   

# list_of_num = [1,2,4,5,7,8,9,10]

# sum = 0
# for num in list_of_num:
#     sum += num

# count = len(list_of_num)

# average = sum / count

# print(f"The average of the numbers in the list is: {average}")

#Taking 2 lists as input from user and combining them removing duplicates and sorting in descending order
# list1 = []
# list2 = []

# while True:
#     num = int(input("Enter nums of list1 : (enter 0 to exit)"))
#     if num == 0:
#         break
#     list1.append(num)

# while True:
#     num = int(input("Enter nums of list2 : (enter 0 to exit)"))
#     if num == 0:
#         break
#     list2.append(num)

# combined_set = set(list1 + list2)
# combined_list = list(combined_set)
# combined_list.sort(reverse=True)
# print("Combined List:", combined_list)

#splitting a tuple into even and odd numbers

# tup_total = (1,2,3,4,5,6,7,8,9,10)
# tup_even = ()
# tup_odd = ()

# for num  in tup_total:
#     if num % 2 == 0:
#         tup_even += (num,)
#     else:
#         tup_odd += (num,)
        
# print("Even Tuple:", tup_even)
# print("Odd Tuple:", tup_odd)


# #Dictionary having student name as keys and their marks as values 

# dict = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 90
# }

# while True:
#     char = input("MENU : \n A - Add Student \n B - Update Marks \n C - Search for Student \n D - Display All Student and Marks \t")
    
#     match(char):
#         case 'A':
#             student = input("Enter Student Name :")
#             marks = int(input("Enter Student Marks :"))
#             dict.update({student:marks})
#             print("Student Added Successfully")
#         case 'B':
#             student = input("Enter Student Name to Update Marks :")
#             if student in dict:
#                 marks = int(input("Enter New Marks :"))
#                 dict[student] = marks
#                 print("Marks Updated Successfully")
#             else:
#                 print("Student Not Found")
#         case 'C':
#             student = input("Enter Student Name to Search :")
#             if student in dict:
#                 print(f"{student} : {dict[student]}")
#             else:
#                 print("Student Not Found")
#         case 'D':
#             for student, marks in dict.items():
#                 print(f"{student} : {marks}")

# # Create a dictionary from a list of words where each word is a key and its length is the value
# words =["apple","banana","kiwi","cherry","mango"]

# dict = {
#     word: len(word) for word in words
# }

# print("Dictionary of words and their lengths:", dict)

# #program that takes string from a user and counts the number of spaces in it

# count = 0
# str = input("Enter a string :")
# for char in str:
#     if char == ' ':
#         count += 1
# print(f"Number of spaces in the string: {count}")

# #check whether two lists have any common elements

# list1 =[1,2,3,4] 
# list2 =[3,4]


# int_set = set(list1).intersection(set(list2))

# if len(int_set) == 0:
#     print("No common elements")
# else:
#     print("Common elements found:", int_set)

# #Create a list of duplicate elements from a given list of integers
# list1 = [1,2,2,2,3,3,4,5]
# new_list = []

# for item in list1:
#     if list1.count(item) > 1:
#         if item not in new_list:
#             new_list.append(item)
            
# print("duplicate elements:", set(new_list))

str = input("Enter a string :")
count = 0
for char in str:
    if str.count(char) == 1:
        count += 1
        print(char)
        
print(f"Number of unique characters in the string: {count}")