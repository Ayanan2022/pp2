unik={"kbtu","sdu","narhoz","mnu","nu","sdu"}
print(unik) #Output {'nu', 'sdu', 'kbtu', 'mnu', 'narhoz'}

#access
print('kbtu' in unik) #Output True
print('kbtu' not in unik) #Output False
for i in unik:
    print(i,end=" ") #output mnu nu kbtu narhoz sdu

#add
city=("Almaty","Astana","Aktau","Oral")
unik.add("aitu")
print(unik) #Output {'narhoz', 'kbtu', 'mnu', 'nu', 'sdu', 'aitu'}
unik.update(city) 
print(unik) #Output {'Astana', 'narhoz', 'Almaty', 'Oral', 'aitu', 'Aktau', 'nu', 'kbtu', 'mnu', 'sdu'}

#remove
unik.remove("narhoz")
print(unik) #output {'Oral', 'nu', 'Astana', 'Aktau', 'kbtu', 'mnu', 'Almaty', 'sdu', 'aitu'}
unik.discard("sdu")
print(unik) #output {'Oral', 'nu', 'Astana', 'Aktau', 'kbtu', 'mnu', 'Almaty', 'aitu'}
unik.pop()
print(unik) #output {'nu', 'Astana', 'Aktau', 'kbtu', 'mnu', 'Almaty', 'aitu'}
unik.clear()
print(unik) #output set()

#loop
for x in city:
    print(x,end=" ") #output Almaty Astana Aktau Oral

#join
set1={"kbtu","sdu","narhoz","mnu","nu","sdu"}
set2={24,25,26,27,28}
set3={"Ayana","Saniya","Kamshat","Elza"}
set5={"kbtu","apple","banana","ai"}
set4=set1.union(set2,set3) # "set4 = set1 | set2 | set3" same
print(set4) #output {26, 'narhoz', 'Kamshat', 'Ayana', 'sdu', 'Saniya', 'Elza', 'nu', 24, 'kbtu', 'mnu', 27, 28, 25}

set1.update(set2)
print(set1) #output {'kbtu', 'narhoz', 'mnu', 'nu', 'sdu', 24, 25, 26, 27, 28}

set6=set1.intersection(set5) #set6 = set1 & set5 only with sets
print(set6) #output {'kbtu'} 

set1.intersection_update(set5)
print(set1) #output {'kbtu'}

set1={"kbtu","sdu","narhoz","mnu","nu","sdu"}
set5={"kbtu","apple","banana","ai"}
set7=set1.difference(set5) #set7=set1-set5 onty sets with sets
print(set7) #output {'narhoz', 'mnu', 'sdu', 'nu'}

set1.difference_update(set5)
print(set1) #output {'narhoz', 'sdu', 'nu', 'mnu'}

set1={"kbtu","sdu","narhoz","mnu","nu","sdu"}
set5={"kbtu","apple","banana","ai"}
set8=set1.symmetric_difference(set5) #set8=set1 ^ set 5 only sets with sets
print(set8) #output {'ai', 'narhoz', 'apple', 'nu', 'sdu', 'mnu', 'banana'}

set1.symmetric_difference_update(set5)
print(set1) #output {'mnu', 'ai', 'narhoz', 'apple', 'nu', 'sdu', 'banana'}




