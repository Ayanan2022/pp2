#1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#2
day = input("Enter the day of the week: ").lower()
if day == "monday":
    print("Start of the work week!")
elif day == "friday":
    print("Almost the weekend!")
elif day == "sunday":
    print("Relax, it's the weekend!")
else:
    print("It's a regular weekday.")

#3
temperature = int(input("Enter the temperature in Celsius: "))
is_raining = input("Is it raining (yes/no)? ").lower()

if temperature > 30 and is_raining == "no":
    print("It's a hot and dry day.")
elif temperature > 30 and is_raining == "yes":
    print("It's a hot and rainy day.")
elif temperature <= 30 and is_raining == "yes":
    print("It's a cool and rainy day.")
else:
    print("It's a cool and dry day.")

