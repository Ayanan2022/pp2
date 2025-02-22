import re

s=str(input("s:"))

res = re.sub(r'_([a-z])', lambda match: match.group(1).upper(),s)
print(res)
