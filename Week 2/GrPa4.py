#You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. 
#If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order.
#The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person. 
#For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. 
#Your output should be the name of the younger of the two.


from datetime import *
#person 1 details
name1 = input()
d1, m1, y1 = [int(x) for x in input().split('-')]
b1 = date(y1, m1, d1)
#person 2 details
name2 = input()
d2, m2, y2 = [int(x) for x in input().split('-')]
b2 = date(y2, m2, d2)
#compare
if b1 == b2:
    if(name1>name2):
        print(name2)
    else:
        print(name1)
elif b1 > b2:
    print(name1)
else:
    print(name2)
