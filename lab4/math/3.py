import math
n=int(input("Input number of sides:"))
s=int(input("Input the length of a side:"))
area=0.25*n*math.pow(s,2)* (1/math.tan(math.pi/n))
print (int(area))