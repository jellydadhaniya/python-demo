import datetime

print("Welcome to the Interactive Personal Data Collector!")

name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height in meters:"))
number = int(input("Enter your favourite number:"))

print("Thank you! Here is the information we collected:")

print(f"Name: {name} (Type: {type(name)}, memory address:{id(name)} )")
print(f"Age: {name} (Type: {type(age)}, memory address:{id(age)} )")
print(f"Height: {height} (Type: {type(height)}, memory address:{id(height)} )")
print(f"Number: {number} (Type: {type(number)}, memory address:{id(number)} )")

current_year= datetime.datetime.now().year
birth_year = current_year - age

print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")
print("Thank you for using the Personal Data Collector. Goodbye!")
