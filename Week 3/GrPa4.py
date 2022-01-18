#Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. 
#You can assume that the string will only contain letters.

i = input()
j = i.lower()
asc = ''.join(sorted(j))
print(asc)
