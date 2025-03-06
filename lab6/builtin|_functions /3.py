s=str(input())

def palindrom(a):
    return a=="".join(reversed(a))

rslt=palindrom(s)
print(rslt)