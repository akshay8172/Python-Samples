#Prime or Not
"""
def primeOrNot(number):
    if number>1:
        for i in range(2, int(number**0.5) +1):
            if number %i == 0:
                return False
        return True
    
result = primeOrNot(7)
print(result)"""

#Leap Year Or Not

'''def leapYearOrNot(year):
    if (year % 4 ==0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False
    
year = 2029    
result=leapYearOrNot(year)

if result:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")'''
        
       
#Palindrome Or Not 

'''def palindrome(strin):
    left = 0
    right = len(strin) - 1
    while left < right:
        if strin[left] != strin[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

my_string = 'malayalam'
result = palindrome(list(my_string))
if result:
    print("Palindrome")
else:
    print("Not palindrome")'''

#Panagram Or Not

'''def is_pangram(sentence):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())

    return alphabet_set.issubset(sentence_set)

input_sentence = "The quick brown fox jumps over the lazy dog"
result = is_pangram(input_sentence)

if result:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")'''


# Least Non Negative value
"""def least_non_negative_number(my_list):
    non_negative = [num for num in my_list if num >= 0]
    if non_negative:
        return min(non_negative)
    else:
        return None

my_list = [ -1, 10, 9]
least_non_negative = least_non_negative_number(my_list)
print(least_non_negative)"""

# Fibonacci Series in Python Using For Loop
# initialize two variables, with value 0
'''a, b = 0, 1
series_length = 19

for i in range(series_length):
    print(a)
    a, b = b, a + b
'''

    
#Reverse a string    
    
'''string = "AKSHAY"
listed = list(string)
left = 0
right = len(listed)-1
while left<right:
    listed[left], listed[right] = listed[right],  listed[left]
    left +=1
    right -=1

string = ''.join(listed)
print(string)'''


#Count the occurrence of each character in a string
'''string = "geeksforgeeks
character_to_count = "e"
result = string.count(character_to_count)

'''

#Remove duplicate elements from a list
'''def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(original_list)
print("Original List:", original_list)
print("List after removing duplicates:", result_list)'''

#Print natural numbers upto a limit
'''limit = int(input("Enter Number greater than 0 : ")) 
if limit>0:
    for i in range(0, limit+1):
        print(i)
else:
    print("Enter Number greater than zero")'''

#Factorial 
'''def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = 5
result = factorial_iterative(number)
print(f"The factorial of {number} is: {result}")'''


#Largest Element in a list
'''numbers = [5, 12, 8, 999, 25, 3, 18]
largest_element = 0

for num in numbers:
    if num > largest_element:
        largest_element = num

print("The largest element in the list is:", largest_element)
'''

#Armstrong Number
'''num=int(input("Enter a the number :"))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
    
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")'''
    
#Find the common elements between two lists.   
def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

# Test the function
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)




