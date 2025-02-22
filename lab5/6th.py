import re

def rep(s):
    pattern=r'[ ,.]'
    x=re.sub(pattern,":",s)
    return x

txt=str(input("txt:"))
rslt=rep(txt)
print(rslt)