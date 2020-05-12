#Introduction to interactive user input
#the input() function accepts string values from the user

print("How old are you?", end=' ')
age = input()
print("How tall are you? (cm)", end=' ')
height = input()
print("How much do you weigh? (lbs)", end= ' ')
weight = input()

print(f"So you are, {age} years old, {height} centimeters tall, and {weight} pounds heavy.")

print("\nLets do a little addition.\nGive me two numbers: ")
a = int(input())
print("and?")
b = int(input())

c = a + b
print(f"Alright, so {a} + {b} = {c}")