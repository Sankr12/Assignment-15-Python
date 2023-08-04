# Write a python script to determine whether a string contains a specific substring.

string = input("Enter a string: ")
substring = input("Enter a substring you want to check that string contains: ")

if substring in string:
    print(f"The string contains the substring '{substring}'.")
else:
    print(f"The string doesn't contains the substring '{substring}'.")