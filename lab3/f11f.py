def palin():
    a = str(input())
    a = a.lower()
    a.replace(" ","")
    if a == a[::-1]:
        return True

if palin():
    print("yes")
else:
    print("no")