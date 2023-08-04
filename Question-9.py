# Write a python script to check if a string contains only characters of the alphabet.

print()
string = input("Enter a string: ")
print()

if string.isalpha():
    print(f"The '{string}' contains characters of the alphabet only")
else:
    print(f"The '{string}' doesn't contains characters of the alphabet only")
print()