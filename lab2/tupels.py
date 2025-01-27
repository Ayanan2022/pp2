mytuple=("kbtu","sdu","narhoz","mnu","nu")
print(mytuple) #Output ('kbtu', 'sdu', 'narhoz', 'mnu', 'nu')

#len
print(len(mytuple)) #Output 5

trueT=("kbtu",)
fallT=("kbtu")
print(type(trueT),type(fallT)) #Output <class 'tuple'> <class 'str'>

maketuple=tuple(("alma","nan","sut"))
print(maketuple) #Output ('alma', 'nan', 'sut')

t = ("apple", "banana", "cherry", "melon", "mango")
print(t[-5:-3]) #Output ('apple', 'banana')

#update tuple
x = ("kbtu","sdu","narhoz","mnu","nu")
y = list(x)
y.append("aitu")
x = tuple(y)
print(x) #Output ('kbtu', 'sdu', 'narhoz', 'mnu', 'nu', 'aitu')

#unpack tuple
unik = ("kbtu","sdu","narhoz","mnu","nu")
(a, *b, c) = unik
print(a) #Output kbtu
print(b) #Output ['sdu', 'narhoz', 'mnu']
print(c) #Output nu

#join
city=("Almaty","Astana","Aktau","Oral")
unik = ("kbtu","sdu","narhoz","mnu","nu")
vmeste=city+unik
print(vmeste) #Output ('Almaty', 'Astana', 'Aktau', 'Oral', 'kbtu', 'sdu', 'narhoz', 'mnu', 'nu')


