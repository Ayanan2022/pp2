import re
def find_llun(a):
    pattern=r'\b[a-z]+_[a-z]+\b'
    x=re.findall(pattern,a)
    return x

txt=str(input("txt="))
rslt=find_llun(txt)
print("Output:", rslt)