#Accept a positive integer nn, with n > 1n>1, as input from the user and print all the prime factors of nn in ascending order.

import math
n = int(input())
i = 2
sqrtn = math.sqrt(n)
while i<= sqrtn:
    if n%i==0:
        n = n/i
        print(i)
    else:
        i += 1

if n>2:
    print('%d'%n)
