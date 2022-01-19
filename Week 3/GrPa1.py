'''
Accept a positive integer nn as input and print the sum of the first nn terms of the series given below:

1+ (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4) + \cdots1+(1+2)+(1+2+3)+(1+2+3+4)+⋯
Just to be clear, the first term in the series is 11, the second term is (1 + 2)(1+2) and so on.
'''

n = int(input())
sum = 1
lst = [1]*n
for i in range(1,n):
    lst[i]=lst[i-1]+i+1
    sum += lst[i]
print(sum)
