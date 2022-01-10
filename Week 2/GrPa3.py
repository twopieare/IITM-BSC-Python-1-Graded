#Accept a string as input and print the vowels present in the string in alphabetical order. 
#If the string doesn't contain any vowels, then print the string none as output. 
#Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.

string1 = str(input())
string = string1.lower()
#ans = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0} 
arr = [0,0,0,0,0]
l = len(string1)
for i in range(0,l):
    if (string[i] == 'a'):
        arr[0] += 1
    if (string[i] == 'e'):
        arr[1] += 1
    if (string[i] == 'i'):
        arr[2] += 1
    if (string[i] == 'o'):
        arr[3] += 1
    if (string[i] == 'u'):
        arr[4] += 1
out = ""
if(arr[0] > 0):
    out = out + 'a'
if(arr[1] > 0):
    out = out + 'e'
if(arr[2] > 0):
    out = out + 'i'
if(arr[3] > 0):
    out = out + 'o'
if(arr[4] > 0):
    out = out + 'u'
if(arr[0] == 0 and arr[1] == 0 and arr[2] == 0 and arr[3] == 0 and arr[4] == 0):
    print("none")
print(out)
    
