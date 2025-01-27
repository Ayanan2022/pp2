#1
i = 1
while i < 10:
  print(i,end=",") #output 1,2,3,4,5,6,7,8,9,
  i += 1
print("\n")

#break
i = 1
while i < 10:
  print(i,end=",") #output 1,2,3,4,5,
  if i == 5:
    break
  i += 1
print("\n")

#continue
i = 0
while i < 15:
  i += 1
  if i == 5:
    continue
  print(i,end=",") #output 1,2,3,4,6,7,8,9,10,11,12,13,14,15,
print("\n")

#else
i = 1
while i < 20:
  print(i,end=",") #output 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,i is no longer less than 20
  i += 1
else:
  print("i is no longer less than 20")