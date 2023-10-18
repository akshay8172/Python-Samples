'''list_of_data = []
number = int(input("Enter the Number :"))
print("Enter the elements..")
for i in range(0,number):
    elements = input()
    list_of_data.append(elements)
print(list_of_data)'''


#    xxxxx
#    xx
#    xxxxx
#    xx
#    xx

'''numbers = [7,2,7,2,2]
for x in numbers:
    print('*' * x)'''
    
numbers = [7,2,7,2,2]
for times in numbers:
    output = ''
    for times in range(times):
        output += '*'
    print(output)