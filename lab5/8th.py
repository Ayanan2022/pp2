import re
def reg(s):
    patt = r'^[a-zA-Z]+$'
    if re.search(patt , s):
        return True
    else:
        return False
s = str(input())
t = ''
if reg(s):
    t = ' '.join(s.upper())
    print(t)
else:
    print('no')
