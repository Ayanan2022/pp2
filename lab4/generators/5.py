n=int(input("n="))

def nbr(a):
    cnt=0
    while cnt<=a:
        yield a
        a-=1

rslt=nbr(n)
for i in rslt:
    print(i)