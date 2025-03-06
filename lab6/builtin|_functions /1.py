from functools import reduce

def ans(a):
    mult=reduce(lambda x,y: x*y , a)
    print(mult)
    
n=int(input())
a=[]
for i in range (n):
    b=int(input())
    a.append(b)

ans(a)