import re

s1 =str(input("s:"))
s2 = re.sub(r'([a-z])([A-Z])', r'\1_\2', s1).lower()

#Camel case is a writing style in which multiple words are concatenated into a single string, Snake case is another writing style where words are separated by underscores (_) and all letters are lowercase. 

print(s2)
