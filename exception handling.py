a = int(input("Enter the 1st Number :"))
b = int(input("Enter the 2nd Number :"))

try:
    c = a/b
    print(c)
    print("Success !!")
except ZeroDivisionError:
    print("Can't divide with zero...")
    
print("Program Exit")