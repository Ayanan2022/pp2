import re
def a_b(s):
    pattern=r'^a.*b$'
    x=re.findall(pattern,s)
    return x

txt=str(input("txt:"))
rslt=a_b(txt)
print("Output",rslt)