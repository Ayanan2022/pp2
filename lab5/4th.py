import re
def upper_lower(s):
    pattern=r'\b[A-Z][a-z]+\b'
    x=re.findall(pattern,s)
    return x

txt=str(input("txt:"))
rslt=upper_lower(txt)

print("Output:",rslt)