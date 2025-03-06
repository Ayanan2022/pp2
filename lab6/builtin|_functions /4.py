import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000) 
    return math.sqrt(number)

num = int(input("Enter a number: "))  
delay = int(input("Enter delay in milliseconds: ")) 

result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")
