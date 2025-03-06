s=str(input())

cnt_u=0
cnt_l=0
def upper(a):
    global cnt_u,cnt_l
    for i in range(len(a)):
        if a[i].isupper():
            cnt_u+=1
        else:
            cnt_l+=1
    return cnt_u,cnt_l
            
        
rslt=upper(s)
print(rslt)