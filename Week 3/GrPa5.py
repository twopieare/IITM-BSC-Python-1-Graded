def isValid(ph):
    li=[]
    while ph>0:
        li=[ph%10]+li
        ph=ph//10
    n=len(li)
    set1={6,7,8,9}
    if n!=10 or li[0] not in set1:
        print('invalid')
        return
    li1=[0 for i in range(10)] # li1[i] is the frequency of i
    for i in li:
        li1[i]+=1
    for j in li1:
        if j>=7:
            print('invalid')
            return
    i,count=0,1             # the 5 consecutive element cond.,linear search
    while i<n-1:
        if li[i+1]==li[i]:
            count+=1
            if count>5:
                print('invalid')
                return
        else:
            count=1
        i+=1
    print('valid')
    return
ph = int(input())
isValid(ph)
