n=int(input("n="))
def gnrt(a):
    cnt=1
    while cnt<=a:
        if cnt%3==0 or cnt%4==0:
            yield cnt
        cnt+=1

rslt=gnrt(n)
for i in range(n+1):
    print(next(rslt)) 