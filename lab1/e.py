#String (all topics)

a="Hello, kbtu24bd "
#slicing
print(a[:10])
print(a[3:8])
print(a[: :-1])

#modify
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("l", "a"))
print(a.split(","))

#concatenate
name="Ayana "
fam="Nauryzbayeva"
print(name+fam)

#format
day=24
month="April"
print(f"I will be 18 in {day} {month} ")

price = 899
t = f"The price is {price:.2f} tenge"
print(t)

example = f"The price is {899 * 4} tenge"
print(example)

#escape characters
txt="My name is Ayana \n I am from \'Almaty \' \n I'm studing in\tKBTU" #and we another ch.
print(txt)
