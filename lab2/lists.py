mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))



#List Items - Data Types
list1 = ["beshbarmak", "baursak", "kymyz","alma"] #str
list2 = [888,777,555,666] #int
list3 = [True, False, False] #bool
list4 = ["abc", 34, True, 40, "male"]

print(type(list1))
# <class 'list'>

a = list(("apple", "banana", "cherry")) 
print(a)
#['apple', 'banana', 'cherry']



#Access list items
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

slice1 = my_list[2:5]
slice2 = my_list[:4] 
slice3 = my_list[6:] 
slice4 = my_list[-3:]  
slice5 = my_list[-4:-1]  
slice6 = my_list[1:8:2] 
slice7 = my_list[::3]  
reversed_list = my_list[::-1]

print(slice1) #Output: [2, 3, 4]
print(slice2) #Output: [0, 1, 2, 3]
print(slice3) #Output: [6, 7, 8, 9]
print(slice4) #Output: [7, 8, 9]
print(slice5) #Output: [6, 7, 8]
print(slice6) #Output: [1, 3, 5, 7]
print(slice7) #Output: [0, 3, 6, 9]
print(reversed_list) #Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



#Change list items
my_fruits = ["pear", "grape", "melon"]
my_fruits[1] = "blueberry"
print(my_fruits)  # Output: ['pear', 'blueberry', 'melon']

my_fruits = ["pear", "grape", "melon", "peach", "plum", "papaya"]
my_fruits[1:3] = ["blueberry", "blackberry"]
print(my_fruits)  # Output: ['pear', 'blueberry', 'blackberry', 'peach', 'plum', 'papaya']

my_fruits = ["pear", "grape", "melon"]
my_fruits[1:2] = ["blueberry", "blackberry"]
print(my_fruits)  # Output: ['pear', 'blueberry', 'blackberry', 'melon']

my_fruits = ["pear", "grape", "melon"]
my_fruits[1:3] = ["blackberry"]
print(my_fruits)  # Output: ['pear', 'blackberry']

my_fruits = ["pear", "grape", "melon"]
my_fruits.insert(2, "blackberry")
print(my_fruits)  # Output: ['pear', 'grape', 'blackberry', 'melon']



#Add lists items
b = [888,777,555,666,777]
b.append(111)
b.insert(0,999)
print(b) #Output: [999, 888, 777, 555, 666, 777, 111]

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']



#Remove List Items
vegetables = ["carrot", "potato", "tomato", "broccoli", "cucumber", "spinach"]

vegetables.remove("broccoli")
print("After remove:", vegetables)  # Output: ['carrot', 'potato', 'tomato', 'cucumber', 'spinach']

popped_item = vegetables.pop(2)
print("Popped item:", popped_item)  # Output: tomato
print("After pop:", vegetables)  # Output: ['carrot', 'potato', 'cucumber', 'spinach']

del vegetables[1]
print("After del (index 1):", vegetables)  # Output: ['carrot', 'cucumber', 'spinach']

del vegetables[1:2]
print("After del (slice 1:2):", vegetables)  # Output: ['carrot', 'spinach']



#loop lists
nauryzbayeva = ["ayana", "bayana", "dayana"]
for x in nauryzbayeva:
  print(x,end=" ")

for i in range(len(nauryzbayeva)):
  print(nauryzbayeva[i] , end=" ")

kbtu = ["24bd", "25bd", "26bd"]
i = 0
while i < len(kbtu):
  print(kbtu[i], end=" ")
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x , end=" ") for x in thislist]

#Output: ayana bayana dayana ayana bayana dayana 24bd 25bd 26bd apple banana cherry 


#sort
my=[10,15,9,55,88]
my.sort()
print(my) #Output [9, 10, 15, 55, 88]

#revesre sort
my1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
my1.sort(reverse = True)
print(my1) #Output ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#join
my2=my1+my
print(my2) #Output ['pineapple', 'orange', 'mango', 'kiwi', 'banana', 9, 10, 15, 55, 88]
my.extend(my1)
print(my) #Output [9, 10, 15, 55, 88, 'pineapple', 'orange', 'mango', 'kiwi', 'banana']
for x in my1:
  my.append(x)
print(my) #Output [9, 10, 15, 55, 88, 'pineapple', 'orange', 'mango', 'kiwi', 'banana', 'pineapple', 'orange', 'mango', 'kiwi', 'banana']

