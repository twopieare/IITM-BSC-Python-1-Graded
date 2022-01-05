#Accept two positive integers x and y as input. Print the number of digits in xy. You should be able to solve this problem using the concepts covered in week-1.

x = int(input())
y = int(input())
powerr = int(x**y)
count = 0
while(powerr>0):
    count=count+1
    powerr = powerr//10
print(count)
