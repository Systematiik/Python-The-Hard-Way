name = 'Zed A. Shaw'
age = 35

height = 74 #inches
height_cm = height * 2.54

weight = 180 #pounds
weight_kg = 180 / 2.2

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")

print(f"He's {height} inches tall. \nIn centimeters, about, {round(height_cm)}.")
print(f"He's {weight} pounds heavy. \nIn kilograms, about, {round(weight_kg)}.")

print("Actrually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this adds Zed's age, height, and weight together
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")