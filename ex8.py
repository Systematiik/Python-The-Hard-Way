"""
    formatter is a variable, and the .format is a function
"""

formatter = "{} {} {} {}"

#using .format allows the user to in put variables into the curly brackets
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "My name is Jeremy.",
    "I am learning Python.",
    "I learned some Java and Javascript.",
    "I am unofficially and HTML engineer."
))