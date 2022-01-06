#Accept three positive integers as input and check if they form the sides of a right triangle. 
#Print YES if they form one, and NO if they do not. The input will have three lines, with one integer on each line. 
#The output should be a single line containing one of these two strings: YES or NO.

a = int(input())
b = int(input())
c = int(input())
if(a+b <= c or b+c <= a or a+c <= b):
    print("NO")
else:
    print("YES")
