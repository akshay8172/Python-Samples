# Initialize key value pair.
user_number = input("Enter the number :")
numbers = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five"
}
output = ""
for user_numbers in user_number:
    output += numbers.get(user_numbers, "!") + " "
print(output)
