# Write a python string to reverse a string. ("iNeuron")

print()
# String varable contains string value
string = "iNeuron"

# Reverse String
print(string[::-1])
print()

# we can do this also
temp=''
for i in string:
    temp = i+temp
print(temp)