import math
n=int(input("n="))

def sqrt():
    for cnt in range(n+1):
        a=math.pow(cnt,2)
        yield a

rslt=sqrt()
for i in rslt:
    print(i)