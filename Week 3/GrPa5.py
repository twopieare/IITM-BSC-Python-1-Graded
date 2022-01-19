contact = input()
together = 0
totalcount = 0
flag = 1
if((contact[0]=='6' or contact[0]=='7' or contact[0]=='8' or contact[0]=='9') and len(contact)==10):
    for i in range(1,10):
        if(contact[i-1]==contact[i]):
            together += 1
            if(together>5):
                flag = 0
if flag==1:
    print("valid")
else:
    print("invalid")
