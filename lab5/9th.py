import re

def ins(s):
    ptrn=r'[A-Z]'
    t=""
    for i in range(len(s)):
        if re.match(ptrn,s[i]):
            t+=" "+s[i]
        else:
            t+=s[i]
    print(t)

s=str(input("s:"))
ins(s)