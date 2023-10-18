'''# Find the largest number in a list

numbers = [9,8,7,10,22,3]
max_value = numbers[0]
for number in numbers :
    if number > max_value:
        max_value = number
print(max_value)

numbers = [1,1,2,2,3,4,5,6,6,7,3,0,9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)


list1 = [10, 20, 4, 45, 99,123456]
list1.sort()
print("Largest element is:", list1[-1])
'''

# 2D Array
'''matrix = [
    [2,4,6,],
    [8,10,12],
    [14,16,18]
]

matrix [1] [1] = 0
print(matrix[1][1])

for rows in matrix:
    for item in rows:
        if item == 2:
            print(f'zero found at {rows} th row')
   
   
# accept some list from user and accept a key to delete the number. If the number is present in the list delete it and print the new list.         
flag = False
user_input = input("Enter the list :")
user_list = user_input.split()
print(user_list)
key_to_delete = input("Enter the number you want to delete :")
for lists in user_list:
    if lists == key_to_delete:
        flag = True
        user_list.remove(lists)
if not False:
    print(f"New list after deleting the key is {user_list} ")
else:
    print('Number doesnot exist!')
    
    
answer = input("Do you want to delete the complete list ? Y/N").lower()
if answer == 'y':
    user_list.clear()
    print("List deletd")
else:
    print("Ok daa")

#Write a program to remove the duplicates in a list.

user_input = input("Enter the list please :")
user_list = user_input.split()
print(f"The lis is {user_list}")

new_list = []
for user_lists in user_list:
    if user_lists not in new_list:
        new_list.append(user_lists)
print(new_list)

# Unpacking 
tuples = (1,2,3,4,5)
a,b,c,d,e = tuples
print(f"The values are {a},{b},{c},{d},{e}")'''
        