import re
s=str(input("s:"))

print(re.fullmatch('a{1}b{2,3}',s))
print(re.search('a{1}b{2,3}',s))