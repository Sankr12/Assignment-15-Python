# Write a python script to check if a string contains only numbers.

string = input("Enter a string: ")

if string.isdigit():
    print(f"The '{string}' contains digit only")
else:
    print(f"The '{string}' doesn't contains digit only")