n=int(input("n="))

def evn():
    cnt=0
    while cnt<=n:
        if cnt%2==0:
            yield cnt
        cnt+=1
rslt=evn()
for i in rslt:
    print(i,end=",")