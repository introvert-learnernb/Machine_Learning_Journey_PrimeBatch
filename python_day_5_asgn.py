# # file io assgn

# with open("names.txt","w") as f:
#     for i in range(5):
#         name = input(f"Enter name {i+1}: ")
#         f.write(name + '\n')
        
# with open("names.txt","r") as f:
#     for line in f:
#         print(line.strip())
        
# # 2. 

# with open("log.txt",'w') as f:
#     f.write('Program' + '\n')

# with open("log.txt",'a') as f:
#     f.write('Program Run successfully')
    
# with open("log.txt","r") as f:
#     for line in f:
#         print(line.strip())

#3. 

# l1 = [5, 10, 15, 20, 25]
# l2 = [item for item in l1 if item > 15]
# print(l2)

# import json 
# cities = {
#     "KTM":2000,
#     "MNR":1000,
#     "PKR":500
# }

# with open("cities.json","w") as f:
#     json.dump(cities,f,indent=4)
    
# with open("cities.json","r") as f:
#     ncs = json.load(f)
    
# print(ncs)

# nc = input("Enter new city :")
# np = int(input("Enter new population :"))

# ncs.update({nc:np})
# print(ncs)

# with open("cities.json","w") as f:
#     json.dump(ncs,f,indent=4)


# try catch

try:
    with open('new.txt','r') as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print('file not found!!')
else:
    print('file read properly!!')
finally:
    print('I will run anyway...')





           
        
        

        
