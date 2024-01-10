# Write a python script to get the count of total number of characters in string = "iNeuron"

string = "iNeuron"
b=0

for i in string:
    b=b+1

print("\nCharacters in {}:".format(string),b,"\n")


# we can do this also 
print(len(string))