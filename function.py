'''def greet(name):
    print(f"hii {name}")
    
    
greet("Akshay")
greet("babu")

try:
    age = int(input("Age :"))
    income = 20000
    Risk = income/age
    print(Risk)
except ZeroDivisionError:
    print("Age cannot be Zero.")'''
    
    
def sum(a, b):
    return a + b

# Use int() to convert input strings to integers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

# Call the sum function and print the result
result = sum(a, b)
print("The sum is:", result)

