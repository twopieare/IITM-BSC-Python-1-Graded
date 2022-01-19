'''
A bot starts at the origin — (0, 0)(0,0) — and can make the following moves:

(1) UP
(2) DOWN
(3) LEFT
(4) RIGHT
Each move has a magnitude of 1 unit. Accept the sequence of moves made by the bot as input. The first entry in the sequence is always START while the last entry in the sequence is always STOP. A sample sequence is given below:

START
UP
RIGHT
LEFT
LEFT
DOWN
UP
STOP

Print the Manhattan distance of the bot from the origin. If the bot is at the position (x, y)(x,y), then its Manhattan distance from the origin is given by the equation:

D = |x| + |y|D=∣x∣+∣y∣
'''


st = input()
lcount = 0 
rcount = 0
ucount = 0
dcount = 0
while st != "END":
    stli = input()
    if stli=="LEFT":
        lcount += 1
    elif stli=="RIGHT":
        rcount += 1
    elif stli=="UP":
        ucount += 1
    elif stli=="DOWN":
        dcount += 1
    else:
        break
answer = abs(lcount - rcount) + abs(ucount - dcount)
print(answer)
