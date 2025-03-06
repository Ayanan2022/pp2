n = int(input())
arr = []

for i in range(n):
    a = input().lower()  
    if a=="true" and a==1:
        arr.append(True)
    if a=="false" and a==0:
        arr.append(False)
    else:
        print("invalid sentence")

    
tup = tuple(arr)
print(all(tup))
