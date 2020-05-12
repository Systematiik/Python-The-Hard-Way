# Writing a script that accepts arguments from another file
# When executing a py file with argv, you must pass arguments in in order to work
# ex:
## python ex13.py animbals cannibals tangibles
### Output
## Your first variable is:  animals
## Your second variable is:  cannibals
## Your third variable is:  tangibles

from sys import argv
script, first, second, third = argv

print("The script is called", script)
print("Your first variable is: ", first, )
print("Your second variable is: ", second)
print("Your third variable is: ", third)

animal = input("Name an animal: ")

print(animal)