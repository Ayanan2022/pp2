mydict={
    "brand": "bmw",
    "model": "x5",
    "year": 2023 ,
    "colors": ["black", "white", "grey"]
}

print(mydict) #output {'brand': 'bmw', 'model': 'x5', 'year': 2023, 'colors': ['black', 'white', 'grey']}
print(len(mydict)) #output 4
print(type(mydict)) #output <class 'dict'>

x = mydict.get("model")
y = mydict.keys()
z = mydict.values()
w = mydict.items()
print(x) #output x5
print(y) #output dict_keys(['brand', 'model', 'year', 'colors'])
print(z) #output dict_values(['bmw', 'x5', 2023, ['black', 'white', 'grey']])
print(w) #output dict_items([('brand', 'bmw'), ('model', 'x5'), ('year', 2023), ('colors', ['black', 'white', 'grey'])])

#change && add
mydict["year"]=2024
mydict.update({"year": 2025})

#remove
mydict.pop("color")
mydict.popitem() 
mydict.clear()