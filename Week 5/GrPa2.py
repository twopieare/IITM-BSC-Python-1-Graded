'''
A perfect number is a positive integer that is equal to the sum of all its divisors excluding itself. For example, 66 is a perfect number as 6 = 1 + 2 + 36=1+2+3.

Write a function named is_perfect that accepts a positive integer nn as argument and returns True if it is perfect, and False otherwise.
'''

def is_perfect(n):
    """
    determine if a number is perfect or not

    Argument:
        n: int
    Return:
        result: bool
    """
    factorSum = 0
    for x in range(1,n):
        if n%x==0 :
            factorSum += x
    if factorSum == n :
        return True
    else:
        return False
print(is_perfect(int(input())))
